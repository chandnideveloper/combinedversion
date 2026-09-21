import os
import gc
import uvicorn
from fastapi import FastAPI, Depends, Header
from fastapi.responses import JSONResponse
from typing import Optional

# Production-ready imports
from app.api.schemas import TmdlRequest 
from app.core.logging_utils import set_log_token
from app.core.auth.bearer_validator import validate_auth

from app.agents.folder_agent import FolderAgent
from app.agents.file_agent import FileAgent
from app.agents.coordinatoragent import CoordinatorAgent

from app.core_logic.tmdlgenerator import TmdlGenerator
from app.core_logic.reportgenerator import ReportGenerator

app = FastAPI(title="Tableau to Fabric Autonomous Migration Agent")
print("FASTAPI APP INITIALIZED - PORT 7001")

# 1. Initialize logic engines first
file_agent = FileAgent("FileAgent")
folder_agent = FolderAgent("FolderAgent")

tmdl_generator = TmdlGenerator(file_agent, folder_agent)
report_generator = ReportGenerator(file_agent)

# 2. Initialize the Orchestrator with the logic engines
coordinator = CoordinatorAgent(
    "Coordinator", 
    folder_agent, 
    report_generator, 
    tmdl_generator
)

def _is_auth_token_error(error_msg: str) -> bool:
    """True for Fabric/auth failures that should not trip the SK circuit breaker (use HTTP 401)."""
    msg = (error_msg or "").lower()
    markers = (
        "401",
        "unauthorized",
        "authentication",
        "not authenticated",
        "fabric access token",
        "expired or is invalid",
        "provide a fresh token",
        "app-only token",
    )
    return any(m in msg for m in markers)

@app.post("/migrate", dependencies=[Depends(validate_auth)])
async def run_migration(
    req: TmdlRequest,
    token: str = Depends(validate_auth)
):
    print(f"DEBUG: [main] RECEIVED MIGRATION REQUEST for project_id={getattr(req, 'project_id', 'Unknown')}")
    """
    Triggers the autonomous migration workflow. 
    Security is enforced via the validate_auth dependency.
    """
    # Track request context
    req.token = token
    set_log_token(token)

    req_file_agent = None
    req_folder_agent = None
    req_tmdl_generator = None
    req_report_generator = None
    req_coordinator = None
    result = {"status": "error", "message": "Migration did not produce a result"}

    try:
        # Initialize separate agents/generators for this request to avoid state contamination
        req_file_agent = FileAgent("FileAgent")
        req_folder_agent = FolderAgent("FolderAgent")
        req_tmdl_generator = TmdlGenerator(req_file_agent, req_folder_agent)
        req_report_generator = ReportGenerator(req_file_agent)
        
        req_coordinator = CoordinatorAgent(
            "Coordinator", 
            req_folder_agent, 
            req_report_generator, 
            req_tmdl_generator
        )
        
        # Execute the workflow
        result = await req_coordinator.select_app_by_name(req)
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"ERROR: [main] Migration run failed: {str(e)}\n{error_details}")
        result = {
            "status": "error",
            "message": f"Migration run failed: {str(e)}",
            "details": error_details
        }
    finally:
        # Release request-scoped objects (captured PBIP files can be large) to reduce memory pressure
        try:
            if req_coordinator is not None:
                rg = getattr(req_coordinator, "report_generator", None)
                tg = getattr(req_coordinator, "tmdl_generator", None)
                for agent_holder in (rg, tg):
                    if agent_holder is None:
                        continue
                    fa = getattr(agent_holder, "file_agent", None)
                    if fa is not None and hasattr(fa, "clear_captured_files"):
                        fa.clear_captured_files()
                    elif fa is not None and hasattr(fa, "captured_files"):
                        fa.captured_files.clear()
        except Exception:
            pass
        req_coordinator = None
        req_tmdl_generator = None
        req_report_generator = None
        req_file_agent = None
        req_folder_agent = None
        gc.collect()
    
    # Return proper HTTP status codes based on the result
    if result.get("status") == "error":
        error_msg = result.get("message", "")
        
        # Auth/token failures → 401 so SK circuit breaker treats the service as alive
        if _is_auth_token_error(error_msg):
            return JSONResponse(status_code=401, content=result)
        
        # All other errors return HTTP 500
        return JSONResponse(status_code=500, content=result)
    
    return result

import httpx
from app.core.config import Config

@app.get("/api/records/generation_results", dependencies=[Depends(validate_auth)])
async def get_generation_results(
    run_id: str,
    project_id: str,
    workbook_id: str,
    token: str = Depends(validate_auth)
):
    """
    Fetches the generation results from the Cosmos DB API.
    Proxies the request to the underlying Cosmos DB GET /api/records/generation endpoint.
    """
    base_url = Config.COSMOS_DB_API_URL.rstrip('/')
    api_url = f"{base_url}/api/records/generation"
    
    params = {
        "run_id": run_id,
        "project_id": project_id,
        "workbook_id": workbook_id
    }
    
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(api_url, params=params, headers=headers)
            if resp.status_code == 200:
                try:
                    return resp.json()
                except Exception:
                    return JSONResponse(status_code=500, content={"message": "Invalid JSON returned from Cosmos DB."})
            elif resp.status_code == 404:
                return JSONResponse(status_code=404, content={"detail": "Not Found"})
            else:
                return JSONResponse(status_code=resp.status_code, content={"message": f"Error fetching from Cosmos DB ({resp.status_code}): {resp.text}"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Internal proxy error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)