import os
import uuid
import logging
import httpx
import requests
import datetime
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv

# Ensure environment variables are loaded (for MONGO_API_URL)
load_dotenv(override=True)

logger = logging.getLogger(__name__)
_TELEMETRY_POOL = ThreadPoolExecutor(max_workers=4, thread_name_prefix="agent-activity-telemetry")

def get_mongo_api_url(source_type: str = "unknown") -> str:
    """Fetch MONGO_API_URL from env based on source_type, stripping any trailing slash."""
    if source_type == "tableau":
        url = os.getenv("TABLEAU_MONGO_API_URL", "https://rizio6jk6d4psp4xzqzy2pl4nm0eibme.lambda-url.ap-southeast-2.on.aws")
    else:
        url = os.getenv("MONGO_API_URL", "http://127.0.0.1:8005")
    return url.rstrip("/")

class UnifiedLogger:
    def __init__(self, source_type: str = "unknown"):
        self.source_type = source_type
        self.agent_name = f"{source_type.capitalize()} Generation Agent"
        self.base_url = get_mongo_api_url(source_type)

    # ---------------------------------------------------------
    # AGENT ACTIONS (High-level statuses, e.g. "Generating PBIR")
    # ---------------------------------------------------------
    async def log_action_async(self, run_id: str, project_id: str, workbook_id: str, summary: str, status: str = "running", project_name: str = "Unknown") -> None:
        payload = self._build_action_payload(run_id, project_id, workbook_id, summary, status, project_name)
        if self.source_type == "tableau":
            try:
                from app.tableau.core.config import mongo_db
                if mongo_db is not None:
                    # Direct insert to agent_action
                    await mongo_db["agent_action"].insert_one(payload)
                    return
            except Exception as e:
                logger.error(f"[UnifiedLogger] Direct mongo insert failed for action: {e}")

        url = f"{self.base_url}/api/records/activities"
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(url, json=payload, timeout=5.0)
                resp.raise_for_status()
        except Exception as e:
            logger.error(f"[UnifiedLogger] Failed to log async action to {url}: {e}")

    def log_action_sync(self, run_id: str, project_id: str, workbook_id: str, summary: str, status: str = "running", project_name: str = "Unknown") -> None:
        payload = self._build_action_payload(run_id, project_id, workbook_id, summary, status, project_name)
        if self.source_type == "tableau":
            def _do_mongo():
                try:
                    from app.tableau.core.config import sync_mongo_db
                    if sync_mongo_db is not None:
                        sync_mongo_db["agent_action"].insert_one(payload)
                        return
                except Exception as e:
                    logger.error(f"[UnifiedLogger] Direct mongo insert failed for sync action: {e}")
            _TELEMETRY_POOL.submit(_do_mongo)
            return

        url = f"{self.base_url}/api/records/activities"
        def _do_post():
            try:
                res = requests.post(url, json=payload, timeout=(1, 3))
                res.raise_for_status()
            except Exception as e:
                logger.error(f"[UnifiedLogger] Failed to log sync action to {url}: {e}")
        _TELEMETRY_POOL.submit(_do_post)

    def _build_action_payload(self, run_id, project_id, workbook_id, summary, status, project_name):
        return {
            "id": str(uuid.uuid4()),
            "run_id": run_id or "unknown",
            "project_id": project_id or "unknown",
            "workbook_id": workbook_id or "unknown",
            "project_name": project_name,
            "agent_name": self.agent_name,
            "activity_summary": summary,
            "status": status,
            "source_type": self.source_type,
            "type": "agent_activity",
            "created_at": datetime.datetime.utcnow().isoformat()
        }

    # ---------------------------------------------------------
    # AGENT LOGS (Deep technical traces, errors, info messages)
    # ---------------------------------------------------------
    def _get_trace_url(self):
        """Tableau uses /api/records/logs, Qlik uses /agent-logs."""
        if self.source_type == "tableau":
            return f"{self.base_url}/api/records/logs"
        return f"{self.base_url}/agent-logs"

    async def log_trace_async(self, run_id: str, project_id: str, workbook_id: str, message: str, level: str = "INFO", details: str = None, project_name: str = "Unknown") -> None:
        payload = self._build_trace_payload(run_id, project_id, workbook_id, message, level, details, project_name)
        if self.source_type == "tableau":
            try:
                from app.tableau.core.config import mongo_db
                if mongo_db is not None:
                    # Direct insert to agent_log
                    await mongo_db["agent_log"].insert_one(payload)
                    return
            except Exception as e:
                logger.error(f"[UnifiedLogger] Direct mongo insert failed for trace: {e}")

        url = self._get_trace_url()
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(url, json=payload, timeout=5.0)
                resp.raise_for_status()
        except Exception as e:
            logger.error(f"[UnifiedLogger] Failed to log async trace to {url}: {e}")

    def log_trace_sync(self, run_id: str, project_id: str, workbook_id: str, message: str, level: str = "INFO", details: str = None, project_name: str = "Unknown") -> None:
        payload = self._build_trace_payload(run_id, project_id, workbook_id, message, level, details, project_name)
        if self.source_type == "tableau":
            def _do_mongo():
                try:
                    from app.tableau.core.config import sync_mongo_db
                    if sync_mongo_db is not None:
                        sync_mongo_db["agent_log"].insert_one(payload)
                        return
                except Exception as e:
                    logger.error(f"[UnifiedLogger] Direct mongo insert failed for sync trace: {e}")
            _TELEMETRY_POOL.submit(_do_mongo)
            return

        url = self._get_trace_url()
        def _do_post():
            try:
                res = requests.post(url, json=payload, timeout=(1, 3))
                res.raise_for_status()
            except Exception as e:
                logger.error(f"[UnifiedLogger] Failed to log sync trace to {url}: {e}")
        _TELEMETRY_POOL.submit(_do_post)

    def _build_trace_payload(self, run_id, project_id, workbook_id, message, level, details, project_name):
        return {
            "id": str(uuid.uuid4()),
            "run_id": run_id or "unknown",
            "workspace_id": project_id or "unknown",
            "app_id": workbook_id or "unknown",
            "project_name": project_name,
            "agent_name": self.agent_name,
            "log_level": level,
            "message": message,
            "details": details or "",
            "source_type": self.source_type,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }

# For backwards compatibility during transition
async def log_activity_async(run_id: str, project_id: str, workbook_id: str, summary: str, project_name: str = "Unknown", source_type: str = "legacy") -> None:
    await UnifiedLogger(source_type).log_action_async(run_id, project_id, workbook_id, summary, project_name=project_name)

def log_activity_sync(run_id: str, project_id: str, workbook_id: str, summary: str, project_name: str = "Unknown", source_type: str = "legacy") -> None:
    UnifiedLogger(source_type).log_action_sync(run_id, project_id, workbook_id, summary, project_name=project_name)
