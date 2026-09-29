import os
import re
import time
import uuid
import hashlib
from datetime import datetime
from functools import wraps
from typing import Any, Optional, List, Dict

import json
from fastapi import FastAPI, Query, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from pymongo import MongoClient, ReturnDocument
import certifi
import gridfs

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "QT2F")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable is required and was not set")

app = FastAPI(
    title="MongoDB Microservice API - VL Migration Engine",
    version="2.0.0",
    description="Unified persistence and secret management service replacing Azure Cosmos DB and Azure Key Vault"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.get("/health")
@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "mongodb-microservice"}

# MongoDB Client Initialization
try:
    client = MongoClient(MONGO_URI, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=15000, connectTimeoutMS=15000)
except Exception:
    client = MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True, serverSelectionTimeoutMS=15000, connectTimeoutMS=15000)
db = client[MONGO_DB_NAME]

# GridFS-backed general file store -- used in place of Azure Blob Storage
# for binary artifacts (e.g. uploaded/downloaded Tableau .twbx workbooks)
# that can exceed MongoDB's 16MB per-document limit for a normal collection.
fs = gridfs.GridFS(db, collection="files")

# -------------------- MONGODB COLLECTIONS --------------------
parsing_container = db["parsing"]
mapping_container = db["mapping"]
assessment_container = db["assessment"]
report_generation_container = db["report_generation"]
validation_container = db["validation"]
qlik_container = db["qlik_server_details"]
secrets_container = db["secrets"]
agent_log_container = db["agent_logs"]
agent_action_container = db["agent_actions"]
api_error_container = db["api_error_logs"]
app_error_container = db["app_error_logs"]
run_history_container = db["run_history"]
semantic_kernel_container = db["semantic_kernel_results"]
settings_container = db["settings"]
user_active_container = db["user_active_connections"]
interactive_statuses_container = db["interactive_statuses"]
run_assessment_status_container = db["run_assessment_status"]
app_metadata_container = db["app_metadata"]
counters_container = db["counters"]

# -------------------- RETRY LOGIC --------------------
def retry_db_operation(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            last_error = None
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except HTTPException:
                    raise
                except Exception as e:
                    last_error = e
                    attempts += 1
                    if attempts == max_attempts:
                        raise RuntimeError(f"MongoDB operation failed after {max_attempts} attempts: {str(e)}")
                    time.sleep(delay * (2 ** attempts))
            raise last_error
        return wrapper
    return decorator

# -------------------- HELPER UTILITIES --------------------
def model_to_dict(model_obj: Any, exclude_unset: bool = True) -> Dict[str, Any]:
    """Helper to convert Pydantic models to dict across v1 and v2."""
    if hasattr(model_obj, "model_dump"):
        return model_obj.model_dump(exclude_unset=exclude_unset)
    elif hasattr(model_obj, "dict"):
        return model_obj.dict(exclude_unset=exclude_unset)
    return dict(model_obj)

def sanitize_numbers(data: Any) -> Any:
    """Converts integers that exceed 8-byte signed int limit to float or str."""
    if not isinstance(data, (dict, list)):
        if isinstance(data, int) and (data > 9223372036854775807 or data < -9223372036854775808):
            return str(data)
        return data
    return data

def sanitize_document(doc: Any) -> Any:
    """Removes MongoDB internal '_id' field before returning JSON responses."""
    if isinstance(doc, list):
        for item in doc:
            if isinstance(item, dict) and "_id" in item:
                item.pop("_id", None)
        return doc
    elif isinstance(doc, dict):
        doc.pop("_id", None)
        return doc
    return doc

def find_by_identifier(collection, identifier: str, workspace_id: Optional[str] = None, run_id: Optional[str] = None) -> List[Dict]:
    """Find documents matching identifier across app_id, run_id, folder_name, or id sorted by latest first."""
    raw = str(identifier).strip()
    id_variants = list({
        raw,
        re.sub(r"[\s_]+", "-", raw),
        re.sub(r"[-_]+", " ", raw),
        re.sub(r"[\s\-]+", "_", raw),
    })
    base_or = [
        {"run_id": {"$in": id_variants}},
        {"app_id": {"$in": id_variants}},
        {"folder_name": {"$in": id_variants}},
        {"id": {"$in": id_variants}}
    ]
    query: Dict[str, Any] = {"$or": base_or}
    if workspace_id:
        ws_raw = str(workspace_id).strip()
        query["workspace_id"] = {"$in": list({ws_raw, re.sub(r"[\s_]+", "-", ws_raw), re.sub(r"[-_]+", " ", ws_raw)})}
    if run_id:
        r_raw = str(run_id).strip()
        query["run_id"] = {"$in": list({r_raw, re.sub(r"[\s_]+", "-", r_raw), re.sub(r"[-_]+", " ", r_raw)})}

    docs = list(collection.find(query).sort("_id", -1))
    if not docs and (workspace_id or run_id):
        fallback_docs = list(collection.find({"$or": base_or}).sort("_id", -1).limit(1))
        docs = fallback_docs
    return sanitize_document(docs)

def generate_connection_id(env_type: str = "cloud", url: str = "", connection_name: str = "") -> str:
    """Generate a deterministic connection ID from env_type + url + connection_name."""
    clean_env = (env_type or "cloud").strip().lower()
    clean_url = (url or "").strip().rstrip("/").lower()
    clean_name = (connection_name or "").strip().lower()
    raw = f"{clean_env}:{clean_url}:{clean_name}"
    return f"conn-{hashlib.sha256(raw.encode()).hexdigest()[:12]}"

# -------------------- DATA MODELS --------------------
class SecretData(BaseModel):
    name: str
    value: str
    description: Optional[str] = None

class ParsingData(BaseModel):
    id: Optional[str] = None
    folder_name: Optional[str] = None
    app_id: Optional[str] = None
    space_id: Optional[str] = None
    workspace_id: Optional[str] = None
    app_name: Optional[str] = None
    run_id: Optional[str] = None
    parsing_result: Any = None

class MappingData(BaseModel):
    id: Optional[str] = None
    folder_name: Optional[str] = None
    app_id: Optional[str] = None
    space_id: Optional[str] = None
    workspace_id: Optional[str] = None
    app_name: Optional[str] = None
    run_id: Optional[str] = None
    mapping_result: Any = None

class AssessmentData(BaseModel):
    id: Optional[str] = None
    folder_name: Optional[str] = None
    app_id: Optional[str] = None
    space_id: Optional[str] = None
    workspace_id: Optional[str] = None
    app_name: Optional[str] = None
    run_id: Optional[str] = None
    assessment_result: Any = None

class ReportGenerationData(BaseModel):
    id: Optional[str] = None
    folder_name: Optional[str] = None
    app_id: Optional[str] = None
    space_id: Optional[str] = None
    workspace_id: Optional[str] = None
    app_name: Optional[str] = None
    run_id: Optional[str] = None
    report_result: Any = None

class ValidationData(BaseModel):
    id: Optional[str] = None
    folder_name: Optional[str] = None
    app_id: Optional[str] = None
    space_id: Optional[str] = None
    workspace_id: Optional[str] = None
    app_name: Optional[str] = None
    run_id: Optional[str] = None
    validation_result: Any = None

class QlikServerData(BaseModel):
    id: Optional[str] = None
    connection_id: Optional[str] = None
    server_url: Optional[str] = None
    qlik_url: Optional[str] = None
    qlik_tenant_url: Optional[str] = None
    tenant_url: Optional[str] = None
    connection_name: Optional[str] = None
    env_type: Optional[str] = "cloud"
    user_id: Optional[str] = None
    user_email: Optional[str] = None
    api_key: Optional[str] = None
    qlik_api_key: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class QlikServerUpdate(BaseModel):
    server_url: Optional[str] = None
    qlik_url: Optional[str] = None
    qlik_tenant_url: Optional[str] = None
    tenant_url: Optional[str] = None
    connection_name: Optional[str] = None
    env_type: Optional[str] = None
    user_id: Optional[str] = None
    user_email: Optional[str] = None
    api_key: Optional[str] = None
    qlik_api_key: Optional[str] = None
    updated_at: Optional[str] = None

class UserActiveConnection(BaseModel):
    connection_id: str
    connection_name: Optional[str] = None
    env_type: Optional[str] = "cloud"

class AgentLog(BaseModel):
    run_id: Optional[str] = None
    workspace_id: Optional[str] = None
    app_id: Optional[str] = None
    agent_name: Optional[str] = None
    log_level: Optional[str] = "INFO"
    message: Optional[str] = ""
    details: Optional[Any] = None
    correlation_id: Optional[str] = None
    function_name: Optional[str] = None
    timestamp: Optional[str] = None

class AgentAction(BaseModel):
    id: Optional[str] = None
    project_name: Optional[str] = None
    app_name: Optional[str] = None
    run_no: Optional[str] = None
    run_id: Optional[str] = None
    status: Optional[str] = "success"
    email_id: Optional[str] = None
    user_email: Optional[str] = None
    created_at: Optional[str] = None
    timestamp: Optional[str] = None
    ts: Optional[Any] = None
    payload: Optional[Dict[str, Any]] = {}
    agent_name: Optional[str] = None
    activity_summary: Optional[str] = None
    action: Optional[str] = None
    details: Optional[Any] = None
    project_id: Optional[str] = None
    workspace_id: Optional[str] = None
    workbook_id: Optional[str] = None
    app_id: Optional[str] = None
    correlation_id: Optional[str] = None
    type: Optional[str] = "agent_activity"

class ApiErrorLog(BaseModel):
    service_name: Optional[str] = None
    endpoint: Optional[str] = None
    status_code: Optional[int] = 500
    error_message: Optional[str] = None
    correlation_id: Optional[str] = None
    timestamp: Optional[str] = None

class AppErrorLog(BaseModel):
    app_name: Optional[str] = None
    platform: Optional[str] = None
    screen_name: Optional[str] = None
    error_message: Optional[str] = None
    correlation_id: Optional[str] = None
    timestamp: Optional[str] = None

class RunHistory(BaseModel):
    id: Optional[str] = None
    folder_name: Optional[str] = None
    app_name: Optional[str] = None
    app_id: Optional[str] = None
    space_id: Optional[str] = None
    workspace_id: Optional[str] = None
    run_id: Optional[str] = None
    user_email: Optional[str] = None
    timestamp: Optional[str] = None
    parsing_status: Optional[str] = None
    parsing_message: Optional[str] = None
    mapping_status: Optional[str] = None
    mapping_message: Optional[str] = None
    assessment_status: Optional[str] = None
    assessment_message: Optional[str] = None
    report_generation_status: Optional[str] = None
    report_generation_message: Optional[str] = None
    devops_fabric_sync_status: Optional[str] = None
    devops_fabric_sync_message: Optional[str] = None
    # Which Qlik connection this run used, and the resolved tenant/server URL
    # it points at -- previously accepted nowhere on this model, so callers
    # that sent it (queue_handler.py) had it silently dropped by pydantic.
    connection_id: Optional[str] = None
    server_url: Optional[str] = None
    # The orchestrator's request payload always carries source_type ("qlik"
    # vs "tableau") and branches its own request shapes on it, but this
    # model had nowhere to accept it - a run's persisted record could not
    # answer "was this a Qlik or Tableau migration" without inspecting other
    # fields, and downstream storage fan-out logic could not branch on it
    # either.
    source_type: Optional[str] = None

class SemanticKernelData(BaseModel):
    id: Optional[str] = None
    run_id: Optional[str] = None
    workspace_id: Optional[str] = None
    app_id: Optional[str] = None
    email_id: Optional[str] = None
    user_email: Optional[str] = None
    project_name: Optional[str] = None
    source_type: Optional[str] = None
    type: Optional[str] = "semantic_kernel_result"
    status: Optional[Any] = None
    total_apps: Optional[int] = 0
    total_migrated: Optional[int] = 0
    total_failed: Optional[int] = 0
    total_cancelled: Optional[int] = 0
    total_pending: Optional[int] = 0
    total_ran_till_parsing: Optional[int] = 0
    total_generation_completed: Optional[int] = 0
    total_validation_skipped: Optional[int] = 0
    run_no: Optional[str] = None
    execution_level: Optional[str] = None
    workspace_type: Optional[str] = None
    app_type: Optional[str] = None
    start_date_time: Optional[str] = None
    end_date_time: Optional[str] = None
    time_duration: Optional[str] = None
    time_elapsed: Optional[str] = None
    deployment_type: Optional[str] = None
    payload: Optional[Any] = None

class InteractiveStatusRequest(BaseModel):
    status: str

class RunAssessmentStatusRequest(BaseModel):
    status: Optional[str] = None
    email_id: Optional[str] = None

class DeploymentTypeSettingUpdate(BaseModel):
    deployment_type: str

class TimezoneSettingUpdate(BaseModel):
    timezone: str

class AzureDevOpsSettingsRequest(BaseModel):
    azure_devops_org: Optional[str] = ""
    azure_devops_project: Optional[str] = ""
    azure_devops_repo: Optional[str] = ""
    azure_devops_branch: Optional[str] = "main"
    azure_devops_pat: Optional[str] = None

class AzureDevOpsSettingsUpdate(BaseModel):
    azure_devops_org: Optional[str] = None
    azure_devops_project: Optional[str] = None
    azure_devops_repo: Optional[str] = None
    azure_devops_branch: Optional[str] = None
    azure_devops_pat: Optional[str] = None

class GitSettingsRequest(BaseModel):
    git_org: Optional[str] = ""
    git_repo: Optional[str] = ""
    git_branch: Optional[str] = "main"
    git_pat: Optional[str] = None

class GitSettingsUpdate(BaseModel):
    git_org: Optional[str] = None
    git_repo: Optional[str] = None
    git_branch: Optional[str] = None
    git_pat: Optional[str] = None


# -------------------- HEALTH CHECK --------------------
@app.get("/")
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "az-repo-mongodb-vl",
        "database": MONGO_DB_NAME,
        "features": [
            "parsing", "mapping", "assessment", "report_generation", "validation",
            "qlik_connections", "secrets_store", "agent_logs", "agent_actions",
            "run_history", "semantic_kernel", "system_settings", "counters"
        ]
    }


# ==============================================================================
# 1. SECRETS MANAGEMENT (Replacing Azure Key Vault)
# ==============================================================================
@app.get("/secrets/{name}")
@retry_db_operation()
def get_secret(name: str):
    """Retrieve secret value by name (replaces Key Vault get_secret)"""
    if not name:
        raise HTTPException(status_code=400, detail="Secret name is required")
    doc = secrets_container.find_one({"$or": [{"name": name}, {"id": name}]})
    if not doc:
        raise HTTPException(status_code=404, detail=f"Secret '{name}' not found")
    return {
        "name": doc.get("name", name),
        "value": doc.get("value", ""),
        "version": doc.get("version"),
        "updated_at": doc.get("updated_at")
    }

@app.post("/secrets")
@retry_db_operation()
def set_secret(data: SecretData):
    """Store or update a secret value in MongoDB"""
    now = datetime.utcnow().isoformat()
    version = str(uuid.uuid4())
    item = {
        "id": data.name,
        "name": data.name,
        "value": str(data.value),
        "description": data.description,
        "version": version,
        "enabled": True,
        "updated_at": now
    }
    secrets_container.replace_one({"id": data.name}, item, upsert=True)
    return {"message": f"Stored secret '{data.name}'", "version": version}

@app.delete("/secrets/{name}")
@retry_db_operation()
def delete_secret(name: str):
    """Delete a secret from MongoDB"""
    res = secrets_container.delete_one({"$or": [{"name": name}, {"id": name}]})
    if res.deleted_count == 0:
        return {"status": "success", "message": f"Secret '{name}' was not found or already deleted"}
    return {"status": "success", "message": f"Deleted secret '{name}'"}


# ==============================================================================
# 2. QLIK SERVER DETAILS & CREDENTIAL RESOLUTION
# ==============================================================================
@app.get("/qlik")
@retry_db_operation()
def get_all_qlik_details(env_type: Optional[str] = None, connection_id: Optional[str] = None, user_id: Optional[str] = None):
    """Fetch all saved Qlik server connections (secrets never returned)"""
    query: Dict[str, Any] = {}
    if env_type:
        query["env_type"] = env_type
    if connection_id:
        query["$or"] = [{"id": connection_id}, {"connection_id": connection_id}]
    if user_id:
        query["$or"] = [{"user_id": user_id}, {"user_email": user_id}]

    items = list(qlik_container.find(query).sort("updated_at", -1))
    return [
        {
            "id": item.get("id"),
            "connection_id": item.get("connection_id") or item.get("id"),
            "server_url": item.get("server_url") or item.get("qlik_url") or item.get("qlik_tenant_url", ""),
            "connection_name": item.get("connection_name", ""),
            "env_type": item.get("env_type", "cloud"),
            "user_id": item.get("user_id"),
            "user_email": item.get("user_email"),
            "created_at": item.get("created_at", ""),
            "updated_at": item.get("updated_at", "")
        }
        for item in sanitize_document(items)
    ]

@app.get("/qlik/{id}")
@retry_db_operation()
def get_qlik_details_by_id(id: str):
    """Fetch single Qlik server connection by id or connection_id"""
    doc = qlik_container.find_one({"$or": [{"id": id}, {"connection_id": id}]})
    if not doc:
        raise HTTPException(status_code=404, detail=f"No Qlik server entry found for id '{id}'")
    doc = sanitize_document(doc)
    return {
        "id": doc.get("id"),
        "connection_id": doc.get("connection_id") or doc.get("id"),
        "server_url": doc.get("server_url") or doc.get("qlik_url") or doc.get("qlik_tenant_url", ""),
        "connection_name": doc.get("connection_name", ""),
        "env_type": doc.get("env_type", "cloud"),
        "user_id": doc.get("user_id"),
        "user_email": doc.get("user_email"),
        "created_at": doc.get("created_at", ""),
        "updated_at": doc.get("updated_at", "")
    }

@app.post("/qlik")
@app.post("/qlik/{id}")
@retry_db_operation()
def upsert_qlik_details(data: QlikServerData, id: Optional[str] = None):
    """Create or upsert Qlik connection and securely store API key in MongoDB secrets collection"""
    target_url = (data.qlik_url or data.server_url or data.qlik_tenant_url or data.tenant_url or "").strip().rstrip("/")
    if not target_url:
        raise HTTPException(status_code=400, detail="server_url (or qlik_tenant_url / qlik_url) is required")

    api_key = (data.qlik_api_key or data.api_key or "").strip()
    conn_name = (data.connection_name or "").strip()
    env_type = (data.env_type or "cloud").strip().lower()
    user_id = (data.user_id or data.user_email or "").strip()
    user_email = (data.user_email or (data.user_id if "@" in str(data.user_id) else None) or "").strip()

    conn_id = id or data.connection_id or data.id or generate_connection_id(env_type, target_url, conn_name)
    now = datetime.utcnow().isoformat()

    # 0. Clean previous connection(s) and secrets for this user/email
    if user_email or user_id:
        user_queries = []
        if user_email:
            user_queries.extend([{"user_email": user_email}, {"user_id": user_email}])
        if user_id and user_id != user_email:
            user_queries.extend([{"user_id": user_id}, {"user_email": user_id}])
        if user_queries:
            old_conns = list(qlik_container.find({"$or": user_queries}))
            for oc in old_conns:
                oc_id = oc.get("id") or oc.get("connection_id")
                if oc_id and oc_id != conn_id:
                    secrets_container.delete_many({"$or": [{"id": f"{oc_id}-api-key"}, {"connection_id": oc_id}]})
                    qlik_container.delete_many({"$or": [{"id": oc_id}, {"connection_id": oc_id}]})

    # 1. Store API key in secrets collection
    if api_key:
        secret_name = f"{conn_id}-api-key"
        secrets_container.replace_one(
            {"id": secret_name},
            {
                "id": secret_name,
                "name": secret_name,
                "value": api_key,
                "connection_id": conn_id,
                "version": str(uuid.uuid4()),
                "enabled": True,
                "updated_at": now
            },
            upsert=True
        )

    # 2. Store metadata in qlik_server_details
    existing = qlik_container.find_one({"$or": [{"id": conn_id}, {"connection_id": conn_id}]})
    created_at = existing.get("created_at", now) if existing else (data.created_at or now)

    item = {
        "id": conn_id,
        "connection_id": conn_id,
        "server_url": target_url,
        "connection_name": conn_name,
        "env_type": env_type,
        "user_id": user_id or (existing.get("user_id") if existing else None),
        "user_email": user_email or (existing.get("user_email") if existing else None),
        "created_at": created_at,
        "updated_at": data.updated_at or now
    }

    qlik_container.replace_one({"id": conn_id}, item, upsert=True)

    # 3. If user_id or user_email is provided, automatically record this connection as active for this user
    effective_user = user_email or user_id
    if effective_user:
        active_record = {
            "id": effective_user,
            "user_id": effective_user,
            "user_email": user_email,
            "active_connection_id": conn_id,
            "connection_id": conn_id,
            "connection_name": conn_name,
            "server_url": target_url,
            "updated_at": now
        }
        user_active_container.replace_one({"id": effective_user}, active_record, upsert=True)
        if user_email and user_id and user_id != user_email:
            active_record_alt = dict(active_record)
            active_record_alt["id"] = user_id
            user_active_container.replace_one({"id": user_id}, active_record_alt, upsert=True)

    return item

# ==============================================================================
# 2.1 USER-SPECIFIC ACTIVE CONNECTION ENDPOINTS
# ==============================================================================
@app.post("/users/{user_id}/active-connection")
@retry_db_operation()
def set_user_active_connection(user_id: str, data: UserActiveConnection):
    """Persist the active connection ID for a specific user."""
    if not user_id:
        raise HTTPException(status_code=400, detail="user_id is required")
    conn_id = data.connection_id.strip()
    
    # Verify connection exists in qlik_server_details
    conn_doc = qlik_container.find_one({"$or": [{"id": conn_id}, {"connection_id": conn_id}]})
    server_url = conn_doc.get("server_url") if conn_doc else ""
    connection_name = data.connection_name or (conn_doc.get("connection_name") if conn_doc else "")

    now = datetime.utcnow().isoformat()
    record = {
        "id": user_id,
        "user_id": user_id,
        "active_connection_id": conn_id,
        "connection_id": conn_id,
        "connection_name": connection_name,
        "server_url": server_url,
        "updated_at": now
    }
    user_active_container.replace_one({"id": user_id}, record, upsert=True)
    return {"status": "success", "message": f"Active connection set to '{conn_id}' for user '{user_id}'", "data": sanitize_document(record)}

@app.get("/users/{user_id}/active-connection")
@retry_db_operation()
def get_user_active_connection(user_id: str):
    """Retrieve the saved active connection details for a specific user."""
    record = user_active_container.find_one({"id": user_id})
    if not record:
        # Fallback: check if the user has any connection in qlik_server_details
        user_conn = qlik_container.find_one({"$or": [{"user_id": user_id}, {"user_email": user_id}]})
        if user_conn:
            conn_id = user_conn.get("connection_id") or user_conn.get("id")
            return {
                "status": "success",
                "user_id": user_id,
                "connection_id": conn_id,
                "active_connection_id": conn_id,
                "connection_name": user_conn.get("connection_name", ""),
                "server_url": user_conn.get("server_url", ""),
                "is_fallback": True
            }
        raise HTTPException(status_code=404, detail=f"No active connection found for user '{user_id}'")

    conn_id = record.get("active_connection_id") or record.get("connection_id")
    # Enrich with latest server_url from connection record
    conn_doc = qlik_container.find_one({"$or": [{"id": conn_id}, {"connection_id": conn_id}]})
    server_url = conn_doc.get("server_url") if conn_doc else record.get("server_url", "")
    connection_name = conn_doc.get("connection_name") if conn_doc else record.get("connection_name", "")

    return {
        "status": "success",
        "user_id": user_id,
        "connection_id": conn_id,
        "active_connection_id": conn_id,
        "connection_name": connection_name,
        "server_url": server_url,
        "updated_at": record.get("updated_at")
    }

@app.get("/users/{user_id}/connections")
@retry_db_operation()
def get_user_connections(user_id: str):
    """List all connections belonging to a particular user."""
    items = list(qlik_container.find({"$or": [{"user_id": user_id}, {"user_email": user_id}]}).sort("updated_at", -1))
    return sanitize_document(items)

@app.delete("/users/{user_id}/active-connection")
@retry_db_operation()
def clear_user_active_connection(user_id: str):
    """Clear the active connection for a user."""
    user_active_container.delete_one({"id": user_id})
    return {"status": "success", "message": f"Active connection cleared for user '{user_id}'"}

@app.patch("/qlik/{id}")
@retry_db_operation()
def patch_qlik_details(id: str, data: QlikServerUpdate):
    """Partially update Qlik connection and rotate API key in secrets collection if provided"""
    existing = qlik_container.find_one({"$or": [{"id": id}, {"connection_id": id}]})
    if not existing:
        raise HTTPException(status_code=404, detail=f"No Qlik server entry found for id '{id}'")

    now = datetime.utcnow().isoformat()
    target_url = data.qlik_url or data.server_url or data.qlik_tenant_url or data.tenant_url
    if target_url is not None:
        existing["server_url"] = target_url.strip().rstrip("/")
    if data.connection_name is not None:
        existing["connection_name"] = data.connection_name.strip()
    if data.env_type is not None:
        existing["env_type"] = data.env_type.strip().lower()
    if data.user_email is not None:
        existing["user_email"] = data.user_email.strip()
    if data.user_id is not None:
        existing["user_id"] = data.user_id.strip()
    existing["updated_at"] = data.updated_at or now

    # Clean legacy keys
    existing.pop("qlik_url", None)
    existing.pop("qlik_tenant_url", None)

    # Rotate secret in secrets collection if provided
    api_key = data.qlik_api_key or data.api_key
    if api_key:
        secret_name = f"{id}-api-key"
        secrets_container.replace_one(
            {"id": secret_name},
            {
                "id": secret_name,
                "name": secret_name,
                "value": api_key.strip(),
                "connection_id": id,
                "version": str(uuid.uuid4()),
                "enabled": True,
                "updated_at": now
            },
            upsert=True
        )

    doc_id = existing.get("id", id)
    qlik_container.replace_one({"id": doc_id}, existing, upsert=True)

    # Update active connection for this user
    effective_user = existing.get("user_email") or existing.get("user_id")
    if effective_user:
        active_record = {
            "id": effective_user,
            "user_id": effective_user,
            "user_email": existing.get("user_email"),
            "active_connection_id": id,
            "connection_id": id,
            "connection_name": existing.get("connection_name", ""),
            "server_url": existing.get("server_url", ""),
            "updated_at": now
        }
        user_active_container.replace_one({"id": effective_user}, active_record, upsert=True)

    return sanitize_document(existing)

@app.delete("/qlik/{id}")
@retry_db_operation()
def delete_qlik_details(id: str):
    """Delete Qlik connection metadata and its associated secret"""
    qlik_container.delete_many({"$or": [{"id": id}, {"connection_id": id}]})
    secrets_container.delete_many({"$or": [{"id": f"{id}-api-key"}, {"name": f"{id}-api-key"}, {"connection_id": id}]})
    return {"status": "success", "message": f"Deleted Qlik server entry for id '{id}'"}

@app.get("/qlik/by-email/{email}")
@app.get("/connections/by-email/{email}")
@retry_db_operation()
def get_connection_by_email(email: str):
    """Retrieve active connection ID and metadata for a user email."""
    if not email:
        raise HTTPException(status_code=400, detail="email parameter is required")
    clean_email = email.strip()
    # 1. Check user_active_connections
    active = user_active_container.find_one({"$or": [{"id": clean_email}, {"user_id": clean_email}, {"user_email": clean_email}]})
    conn_id = active.get("active_connection_id") or active.get("connection_id") if active else None

    # 2. Check qlik_server_details
    if not conn_id:
        doc = qlik_container.find_one({"$or": [{"user_email": clean_email}, {"user_id": clean_email}]})
        if not doc:
            raise HTTPException(status_code=404, detail=f"No connection found for email '{clean_email}'")
        conn_id = doc.get("connection_id") or doc.get("id")

    conn_doc = qlik_container.find_one({"$or": [{"id": conn_id}, {"connection_id": conn_id}]})
    if not conn_doc:
        raise HTTPException(status_code=404, detail=f"Connection document '{conn_id}' not found")

    conn_doc = sanitize_document(conn_doc)
    return {
        "status": "success",
        "user_email": clean_email,
        "connection_id": conn_id,
        "id": conn_id,
        "connection_name": conn_doc.get("connection_name", ""),
        "server_url": conn_doc.get("server_url", ""),
        "env_type": conn_doc.get("env_type", "cloud"),
        "created_at": conn_doc.get("created_at", ""),
        "updated_at": conn_doc.get("updated_at", "")
    }


# ==============================================================================
# 3. SYSTEM SETTINGS & RUN COUNTER & PIPELINE MODES
# ==============================================================================
@app.api_route("/api/records/next-run-no", methods=["GET", "POST"])
@retry_db_operation()
def get_next_run_no():
    """Atomic global incremental run counter (e.g., R-15)"""
    counter_doc = counters_container.find_one_and_update(
        {"_id": "run_counter"},
        {"$inc": {"seq": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER
    )
    run_val = counter_doc.get("seq", 1)
    run_no_str = f"R-{run_val}" if not str(run_val).startswith("R-") else str(run_val)
    return {"run_no": run_no_str, "count": run_val, "next_run_no": run_no_str}

@app.get("/settings")
@app.get("/api/records/settings")
@retry_db_operation()
def get_all_settings():
    """Returns all app settings as a key/value dictionary"""
    items = list(settings_container.find({}))
    settings_dict = {}
    for item in items:
        k = item.get("key") or item.get("id")
        if k:
            settings_dict[k] = item.get("value")
    if "timezone" not in settings_dict:
        settings_dict["timezone"] = "UTC"
    if "deployment_type" not in settings_dict:
        settings_dict["deployment_type"] = "Azure DevOps"
    return {"settings": settings_dict}

# --- Deployment Type Setting ---
@app.get("/deployment_type")
@app.get("/api/records/deployment_type")
@retry_db_operation()
def get_deployment_type_setting():
    doc = settings_container.find_one({"$or": [{"key": "deployment_type"}, {"id": "deployment_type"}]})
    if not doc:
        return {"deployment_type": "Azure DevOps", "value": "Azure DevOps"}
    val = doc.get("value", "Azure DevOps")
    return {"deployment_type": val, "value": val, "id": "deployment_type"}

@app.post("/deployment_type")
@app.post("/api/records/deployment_type")
@app.patch("/deployment_type")
@app.patch("/api/records/deployment_type")
@retry_db_operation()
def upsert_deployment_type_setting(data: DeploymentTypeSettingUpdate):
    now = datetime.utcnow().isoformat()
    record = {
        "id": "deployment_type",
        "key": "deployment_type",
        "value": data.deployment_type,
        "type": "setting",
        "updated_at": now
    }
    settings_container.replace_one({"id": "deployment_type"}, record, upsert=True)
    return record

@app.delete("/deployment_type", status_code=204)
@app.delete("/api/records/deployment_type", status_code=204)
@retry_db_operation()
def delete_deployment_type_setting():
    settings_container.delete_one({"id": "deployment_type"})
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- Timezone Setting ---
@app.get("/settings/timezone")
@app.get("/api/records/timezone")
@retry_db_operation()
def get_timezone_setting():
    doc = settings_container.find_one({"$or": [{"key": "timezone"}, {"id": "timezone"}]})
    if not doc:
        return {"timezone": "UTC", "value": "UTC"}
    val = doc.get("value", "UTC")
    return {"timezone": val, "value": val, "id": "timezone"}

@app.post("/settings/timezone")
@app.post("/api/records/timezone")
@app.patch("/settings/timezone")
@app.patch("/api/records/timezone")
@retry_db_operation()
def upsert_timezone_setting(data: TimezoneSettingUpdate):
    now = datetime.utcnow().isoformat()
    record = {
        "id": "timezone",
        "key": "timezone",
        "value": data.timezone.strip(),
        "type": "setting",
        "updated_at": now
    }
    settings_container.replace_one({"id": "timezone"}, record, upsert=True)
    return record

@app.delete("/settings/timezone", status_code=204)
@app.delete("/api/records/timezone", status_code=204)
@retry_db_operation()
def delete_timezone_setting():
    settings_container.delete_one({"id": "timezone"})
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- Azure DevOps Deployment Settings ---
@app.get("/deployment/azure-devops")
@app.get("/deployment/azure-devops/{id}")
@app.get("/api/records/deployment/azure-devops")
@app.get("/api/records/deployment/azure-devops/{id}")
@retry_db_operation()
def get_azure_devops_settings(id: Optional[str] = None):
    doc = settings_container.find_one({"$or": [{"id": "azure_devops_settings"}, {"key": "azure_devops_settings"}]})
    if not doc:
        raise HTTPException(status_code=404, detail="Azure DevOps settings not found")
    return {
        "id": doc.get("id", "azure_devops_settings"),
        "key": doc.get("key", "azure_devops_settings"),
        "type": "setting",
        "azure_devops_org": doc.get("azure_devops_org", ""),
        "azure_devops_project": doc.get("azure_devops_project", ""),
        "azure_devops_repo": doc.get("azure_devops_repo", ""),
        "azure_devops_branch": doc.get("azure_devops_branch", "main"),
        "token_id": doc.get("token_id"),
        "updated_at": doc.get("updated_at")
    }

@app.post("/deployment/azure-devops")
@app.post("/deployment/azure-devops/{id}")
@app.put("/deployment/azure-devops")
@app.put("/deployment/azure-devops/{id}")
@app.patch("/deployment/azure-devops")
@app.patch("/deployment/azure-devops/{id}")
@app.post("/api/records/deployment/azure-devops")
@app.post("/api/records/deployment/azure-devops/{id}")
@app.put("/api/records/deployment/azure-devops")
@app.put("/api/records/deployment/azure-devops/{id}")
@app.patch("/api/records/deployment/azure-devops")
@app.patch("/api/records/deployment/azure-devops/{id}")
@retry_db_operation()
def save_azure_devops_settings(data: AzureDevOpsSettingsRequest, id: Optional[str] = None):
    existing = settings_container.find_one({"$or": [{"id": "azure_devops_settings"}, {"key": "azure_devops_settings"}]}) or {}
    token_id = existing.get("token_id")
    now = datetime.utcnow().isoformat()

    if data.azure_devops_pat and data.azure_devops_pat.strip():
        if not token_id:
            token_id = f"token-{uuid.uuid4().hex[:12]}"
        secrets_container.replace_one(
            {"id": token_id},
            {"id": token_id, "name": token_id, "value": data.azure_devops_pat.strip(), "updated_at": now},
            upsert=True
        )

    record = {
        "id": "azure_devops_settings",
        "key": "azure_devops_settings",
        "type": "setting",
        "azure_devops_org": data.azure_devops_org if data.azure_devops_org is not None else existing.get("azure_devops_org", ""),
        "azure_devops_project": data.azure_devops_project if data.azure_devops_project is not None else existing.get("azure_devops_project", ""),
        "azure_devops_repo": data.azure_devops_repo if data.azure_devops_repo is not None else existing.get("azure_devops_repo", ""),
        "azure_devops_branch": data.azure_devops_branch or existing.get("azure_devops_branch", "main"),
        "updated_at": now,
        "token_id": token_id
    }
    settings_container.replace_one({"id": "azure_devops_settings"}, record, upsert=True)
    return record

@app.delete("/deployment/azure-devops", status_code=204)
@app.delete("/deployment/azure-devops/{id}", status_code=204)
@app.delete("/api/records/deployment/azure-devops", status_code=204)
@app.delete("/api/records/deployment/azure-devops/{id}", status_code=204)
@retry_db_operation()
def delete_azure_devops_settings(id: Optional[str] = None):
    doc = settings_container.find_one({"$or": [{"id": "azure_devops_settings"}, {"key": "azure_devops_settings"}]})
    if doc and doc.get("token_id"):
        secrets_container.delete_one({"id": doc["token_id"]})
    settings_container.delete_one({"$or": [{"id": "azure_devops_settings"}, {"key": "azure_devops_settings"}]})
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- Git Deployment Settings ---
@app.get("/deployment/git")
@app.get("/deployment/git/{id}")
@app.get("/api/records/deployment/git")
@app.get("/api/records/deployment/git/{id}")
@retry_db_operation()
def get_git_settings(id: Optional[str] = None):
    doc = settings_container.find_one({"$or": [{"id": "git_settings"}, {"key": "git_settings"}]})
    if not doc:
        raise HTTPException(status_code=404, detail="Git settings not found")
    return {
        "id": doc.get("id", "git_settings"),
        "key": doc.get("key", "git_settings"),
        "type": "setting",
        "git_org": doc.get("git_org", ""),
        "git_repo": doc.get("git_repo", ""),
        "git_branch": doc.get("git_branch", "main"),
        "token_id": doc.get("token_id"),
        "updated_at": doc.get("updated_at")
    }

@app.post("/deployment/git")
@app.post("/deployment/git/{id}")
@app.put("/deployment/git")
@app.put("/deployment/git/{id}")
@app.patch("/deployment/git")
@app.patch("/deployment/git/{id}")
@app.post("/api/records/deployment/git")
@app.post("/api/records/deployment/git/{id}")
@app.put("/api/records/deployment/git")
@app.put("/api/records/deployment/git/{id}")
@app.patch("/api/records/deployment/git")
@app.patch("/api/records/deployment/git/{id}")
@retry_db_operation()
def save_git_settings(data: GitSettingsRequest, id: Optional[str] = None):
    existing = settings_container.find_one({"$or": [{"id": "git_settings"}, {"key": "git_settings"}]}) or {}
    token_id = existing.get("token_id")
    now = datetime.utcnow().isoformat()

    if data.git_pat and data.git_pat.strip():
        if not token_id:
            token_id = f"token-{uuid.uuid4().hex[:12]}"
        secrets_container.replace_one(
            {"id": token_id},
            {"id": token_id, "name": token_id, "value": data.git_pat.strip(), "updated_at": now},
            upsert=True
        )

    record = {
        "id": "git_settings",
        "key": "git_settings",
        "type": "setting",
        "git_org": data.git_org if data.git_org is not None else existing.get("git_org", ""),
        "git_repo": data.git_repo if data.git_repo is not None else existing.get("git_repo", ""),
        "git_branch": data.git_branch or existing.get("git_branch", "main"),
        "updated_at": now,
        "token_id": token_id
    }
    settings_container.replace_one({"id": "git_settings"}, record, upsert=True)
    return record

@app.delete("/deployment/git", status_code=204)
@app.delete("/deployment/git/{id}", status_code=204)
@app.delete("/api/records/deployment/git", status_code=204)
@app.delete("/api/records/deployment/git/{id}", status_code=204)
@retry_db_operation()
def delete_git_settings(id: Optional[str] = None):
    doc = settings_container.find_one({"$or": [{"id": "git_settings"}, {"key": "git_settings"}]})
    if doc and doc.get("token_id"):
        secrets_container.delete_one({"id": doc["token_id"]})
    settings_container.delete_one({"$or": [{"id": "git_settings"}, {"key": "git_settings"}]})
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- Interactive Status & Assessment Mode ---
@app.get("/api/records/interactive-status")
@retry_db_operation()
def get_interactive_status():
    doc = interactive_statuses_container.find_one({}, sort=[("_id", -1)])
    if not doc:
        return {"status": "continuous", "is_interactive": False}
    return sanitize_document(doc)

@app.post("/api/records/interactive-status")
@app.patch("/api/records/interactive-status")
@retry_db_operation()
def set_interactive_status(request: InteractiveStatusRequest):
    now = datetime.utcnow().isoformat()
    record = {
        "id": "interactive_status",
        "status": request.status,
        "is_interactive": request.status.lower() in ["interactive", "true"],
        "updated_at": now
    }
    interactive_statuses_container.replace_one({"id": "interactive_status"}, record, upsert=True)
    return record

@app.delete("/api/records/interactive-status", status_code=204)
@retry_db_operation()
def delete_interactive_status():
    interactive_statuses_container.delete_many({})
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/api/run-assessment/")
@retry_db_operation()
def get_run_assessment_status(email_id: Optional[str] = Query(None)):
    query = {"email_id": email_id} if email_id else {}
    doc = run_assessment_status_container.find_one(query, sort=[("_id", -1)])
    if not doc:
        return {"status": "false", "result": False}
    return sanitize_document(doc)

@app.post("/api/run-assessment/")
@app.patch("/api/run-assessment/")
@retry_db_operation()
def set_run_assessment_status(data: RunAssessmentStatusRequest):
    now = datetime.utcnow().isoformat()
    record = {
        "id": data.email_id or "default_assessment_status",
        "email_id": data.email_id,
        "status": data.status or "false",
        "result": str(data.status).lower() in ["true", "1", "lite"],
        "updated_at": now
    }
    run_assessment_status_container.replace_one({"id": record["id"]}, record, upsert=True)
    return record

@app.get("/api/allow-data-agent-to-run/")
@retry_db_operation()
def get_allow_data_agent_status(email_id: Optional[str] = Query(None)):
    return {"status": "false", "result": False}


# ==============================================================================
# 4. AGENT LOGS & MONITORING & ACTIONS
# ==============================================================================
@app.get("/agent-logs")
@retry_db_operation()
def get_agent_logs(
    run_id: Optional[str] = Query(None),
    workspace_id: Optional[str] = Query(None),
    app_id: Optional[str] = Query(None),
    agent_name: Optional[str] = Query(None),
    log_level: Optional[str] = Query(None),
    function_name: Optional[str] = Query(None)
):
    query: Dict[str, Any] = {}
    if run_id: query["run_id"] = run_id
    if workspace_id: query["workspace_id"] = workspace_id
    if app_id: query["app_id"] = app_id
    if agent_name: query["agent_name"] = agent_name
    if log_level: query["log_level"] = log_level
    if function_name: query["function_name"] = function_name

    items = list(agent_log_container.find(query).sort("timestamp", 1))
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id"),
            "app_id": item.get("app_id"),
            "timestamp": item.get("timestamp"),
            "agent_name": item.get("agent_name"),
            "log_level": item.get("log_level"),
            "message": item.get("message"),
            "details": item.get("details"),
            "correlation_id": item.get("correlation_id"),
            "function_name": item.get("function_name")
        }
        for item in sanitize_document(items)
    ]

@app.get("/agent-logs/{log_id}")
@retry_db_operation()
def get_agent_log_by_id(log_id: str):
    doc = agent_log_container.find_one({"id": log_id})
    if not doc:
        raise HTTPException(status_code=404, detail=f"No agent log found with id '{log_id}'")
    return sanitize_document(doc)

@app.post("/agent-logs")
@retry_db_operation()
def create_agent_log(data: AgentLog):
    item = {
        "id": str(uuid.uuid4()),
        "run_id": data.run_id,
        "workspace_id": data.workspace_id,
        "app_id": data.app_id,
        "timestamp": data.timestamp or datetime.utcnow().isoformat(),
        "agent_name": data.agent_name,
        "log_level": data.log_level,
        "message": data.message,
        "details": data.details,
        "correlation_id": data.correlation_id,
        "function_name": data.function_name
    }
    agent_log_container.insert_one(item)
    return {"message": f"Logged action for agent '{data.agent_name}' with level '{data.log_level}'", "id": item["id"]}

@app.patch("/agent-logs/{log_id}")
@retry_db_operation()
def patch_agent_log(log_id: str, data: AgentLog):
    existing = agent_log_container.find_one({"id": log_id})
    if not existing:
        raise HTTPException(status_code=404, detail=f"No agent log found with id '{log_id}'")
    update_data = {k: v for k, v in model_to_dict(data, exclude_unset=True).items() if v is not None}
    agent_log_container.update_one({"id": log_id}, {"$set": update_data})
    return {"message": f"Updated agent log with id '{log_id}'"}

@app.delete("/agent-logs/{log_id}")
@retry_db_operation()
def delete_agent_log_by_id(log_id: str):
    agent_log_container.delete_one({"id": log_id})
    return {"message": f"Deleted agent log with id '{log_id}'"}

@app.delete("/agent-logs/bulk/delete")
@retry_db_operation()
def bulk_delete_agent_logs(run_id: str = Query(...), workspace_id: str = Query(...), app_id: str = Query(...)):
    res = agent_log_container.delete_many({"run_id": run_id, "workspace_id": workspace_id, "app_id": app_id})
    return {"message": f"Deleted {res.deleted_count} logs matching run_id '{run_id}', workspace_id '{workspace_id}', app_id '{app_id}'"}

@app.post("/agent-actions")
@app.post("/api/records/activities")
@retry_db_operation()
def log_agent_action(data: AgentAction):
    now_iso = datetime.utcnow().isoformat()
    action_text = data.activity_summary or data.action or (str(data.details) if data.details else "Agent Activity")
    run_identifier = data.run_id or data.run_no or data.correlation_id or "unknown"
    workspace_identifier = data.workspace_id or data.project_id or "personal"
    app_identifier = data.app_id or data.workbook_id or "unknown"
    proj_name = data.project_name or data.app_name or "Unknown"

    item = {
        "id": data.id or str(uuid.uuid4()),
        "project_name": proj_name,
        "run_no": data.run_no or run_identifier,
        "run_id": run_identifier,
        "status": data.status or "success",
        "email_id": data.email_id,
        "user_email": data.user_email or data.email_id,
        "created_at": data.created_at or data.timestamp or now_iso,
        "timestamp": data.timestamp or data.created_at or now_iso,
        "ts": data.ts,
        "payload": data.payload if isinstance(data.payload, dict) else {},
        "agent_name": data.agent_name or "Agent",
        "activity_summary": action_text,
        "action": data.action or action_text,
        "details": data.details or action_text,
        "project_id": workspace_identifier,
        "workspace_id": workspace_identifier,
        "workbook_id": app_identifier,
        "app_id": app_identifier,
        "correlation_id": data.correlation_id or data.run_no or run_identifier,
        "type": data.type or "agent_activity"
    }
    agent_action_container.insert_one(item)
    return {"message": f"Logged action for {data.agent_name}"}

@app.get("/agent-actions")
@app.get("/api/records/activities")
@app.get("/records/agent-actions")
@retry_db_operation()
def get_agent_actions(
    run_id: Optional[str] = Query(None),
    run_no: Optional[str] = Query(None),
    workspace_id: Optional[str] = Query(None),
    project_id: Optional[str] = Query(None),
    app_id: Optional[str] = Query(None),
    workbook_id: Optional[str] = Query(None),
    agent_name: Optional[str] = Query(None),
    limit: Optional[int] = Query(None),
    offset: Optional[int] = Query(0)
):
    query: Dict[str, Any] = {}
    
    # Flexible run filter
    r_id = run_id or run_no
    if r_id:
        query["$or"] = [{"run_id": r_id}, {"run_no": r_id}, {"correlation_id": r_id}]
    
    # Flexible workspace filter
    w_id = workspace_id or project_id
    if w_id:
        if "$and" not in query:
            query["$and"] = []
        query["$and"].append({"$or": [{"workspace_id": w_id}, {"project_id": w_id}]})
        
    # Flexible app filter
    a_id = app_id or workbook_id
    if a_id:
        if "$and" not in query:
            query["$and"] = []
        query["$and"].append({"$or": [{"app_id": a_id}, {"workbook_id": a_id}]})
        
    # Flexible agent name filter (supports "Parsing", "Parsing Agent", "Mapping", "Mapping Agent", etc.)
    if agent_name:
        clean_name = agent_name.strip()
        base_name = re.sub(r"\s+agent$", "", clean_name, flags=re.IGNORECASE).strip()
        query["agent_name"] = {"$regex": f"^{re.escape(base_name)}(\\s+agent)?$", "$options": "i"}

    cursor = agent_action_container.find(query).sort("timestamp", 1)
    if offset:
        cursor = cursor.skip(offset)
    if limit:
        cursor = cursor.limit(limit)
    items = list(cursor)
    return sanitize_document(items)

@app.post("/api-error-logs")
@retry_db_operation()
def log_api_error(data: ApiErrorLog):
    item = {
        "id": str(uuid.uuid4()),
        "timestamp": data.timestamp or datetime.utcnow().isoformat(),
        "service_name": data.service_name,
        "endpoint": data.endpoint,
        "status_code": data.status_code,
        "error_message": data.error_message,
        "correlation_id": data.correlation_id
    }
    api_error_container.insert_one(item)
    return {"message": f"Logged API error for {data.service_name}"}

@app.get("/api-error-logs")
@app.get("/api-error-logs/{service_name}")
@retry_db_operation()
def get_api_errors(service_name: Optional[str] = None):
    query = {"service_name": service_name} if service_name else {}
    items = list(api_error_container.find(query).sort("timestamp", -1))
    return sanitize_document(items)

@app.post("/app-error-logs")
@retry_db_operation()
def log_app_error(data: AppErrorLog):
    item = {
        "id": str(uuid.uuid4()),
        "timestamp": data.timestamp or datetime.utcnow().isoformat(),
        "app_name": data.app_name,
        "platform": data.platform,
        "screen_name": data.screen_name,
        "error_message": data.error_message,
        "correlation_id": data.correlation_id
    }
    app_error_container.insert_one(item)
    return {"message": f"Logged app error for {data.app_name}"}

@app.get("/app-error-logs")
@app.get("/app-error-logs/{app_name}")
@retry_db_operation()
def get_app_errors(app_name: Optional[str] = None):
    query = {"app_name": app_name} if app_name else {}
    items = list(app_error_container.find(query).sort("timestamp", -1))
    return sanitize_document(items)


# ==============================================================================
# 5. PARSING
# ==============================================================================
@app.get("/parsing")
@retry_db_operation()
def get_all_parsing():
    items = list(parsing_container.find({}))
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "parsing_result": item.get("parsing_result")
        }
        for item in sanitize_document(items)
    ]

@app.get("/parsing/by-run/{run_id}")
@retry_db_operation()
def get_parsing_by_run(run_id: str):
    items = find_by_identifier(parsing_container, run_id)
    if not items:
        return {"message": f"No record found for run_id '{run_id}'"}
    return sanitize_document(items)

@app.get("/parsing/by-app/{app_id}")
@retry_db_operation()
def get_parsing_by_app(app_id: str):
    items = find_by_identifier(parsing_container, app_id)
    if not items:
        return {"message": f"No record found for app_id '{app_id}'"}
    return sanitize_document(items)

@app.get("/parsing/{app_id}")
@retry_db_operation()
def get_parsing(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(parsing_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "parsing_result": item.get("parsing_result")
        }
        for item in sanitize_document(items)
    ]

@app.post("/parsing")
@retry_db_operation()
def upsert_parsing(data: ParsingData):
    identifier = data.app_id or data.folder_name or data.run_id
    if not identifier:
        return {"message": "Either app_id, folder_name or run_id must be provided"}

    # Clean previous record(s) for this folder/app_id
    folder_ref = data.app_id or data.folder_name
    if folder_ref:
        parsing_container.delete_many({"$or": [{"app_id": folder_ref}, {"folder_name": folder_ref}]})
    elif data.run_id:
        parsing_container.delete_many({"run_id": data.run_id})

    doc_id = str(uuid.uuid4())

    item = {
        "id": doc_id,
        "folder_name": data.folder_name or data.app_id,
        "app_id": data.app_id or data.folder_name,
        "space_id": data.space_id or data.workspace_id,
        "workspace_id": data.workspace_id or data.space_id,
        "app_name": data.app_name,
        "run_id": data.run_id,
        "parsing_result": data.parsing_result
    }
    item = sanitize_numbers(item)
    parsing_container.replace_one({"id": doc_id}, item, upsert=True)
    return {"message": f"Inserted parsing for folder '{identifier}'"}

@app.patch("/parsing/{app_id}")
@retry_db_operation()
def patch_parsing(app_id: str, data: ParsingData, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(parsing_container, app_id, workspace_id or data.workspace_id, run_id or data.run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    doc = items[0]
    if data.run_id: doc["run_id"] = data.run_id
    if data.workspace_id or data.space_id: doc["workspace_id"] = data.workspace_id or data.space_id
    if data.parsing_result is not None: doc["parsing_result"] = data.parsing_result
    parsing_container.replace_one({"id": doc["id"]}, doc, upsert=True)
    return {"message": f"Patched parsing for folder '{app_id}'"}

@app.delete("/parsing/{app_id}")
@retry_db_operation()
def delete_parsing(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(parsing_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    for item in items:
        parsing_container.delete_one({"id": item["id"]})
    return {"message": f"Deleted {len(items)} parsing record(s) for folder '{app_id}'"}


# ==============================================================================
# 6. MAPPING
# ==============================================================================
@app.get("/mapping")
@retry_db_operation()
def get_all_mapping():
    items = list(mapping_container.find({}))
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "mapping_result": item.get("mapping_result")
        }
        for item in sanitize_document(items)
    ]

@app.get("/mapping/by-run/{run_id}")
@retry_db_operation()
def get_mapping_by_run(run_id: str):
    items = find_by_identifier(mapping_container, run_id)
    if not items:
        return {"message": f"No record found for run_id '{run_id}'"}
    return sanitize_document(items)

@app.get("/mapping/by-app/{app_id}")
@retry_db_operation()
def get_mapping_by_app(app_id: str):
    items = find_by_identifier(mapping_container, app_id)
    if not items:
        return {"message": f"No record found for app_id '{app_id}'"}
    return sanitize_document(items)

@app.get("/mapping/{app_id}")
@retry_db_operation()
def get_mapping(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(mapping_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "mapping_result": item.get("mapping_result")
        }
        for item in sanitize_document(items)
    ]

@app.post("/mapping")
@retry_db_operation()
def upsert_mapping(data: MappingData):
    identifier = data.app_id or data.folder_name or data.run_id
    if not identifier:
        return {"message": "Either app_id, folder_name or run_id must be provided"}

    # Clean previous record(s) for this folder/app_id
    folder_ref = data.app_id or data.folder_name
    if folder_ref:
        mapping_container.delete_many({"$or": [{"app_id": folder_ref}, {"folder_name": folder_ref}]})
    elif data.run_id:
        mapping_container.delete_many({"run_id": data.run_id})

    doc_id = str(uuid.uuid4())

    item = {
        "id": doc_id,
        "folder_name": data.folder_name or data.app_id,
        "app_id": data.app_id or data.folder_name,
        "space_id": data.space_id or data.workspace_id,
        "workspace_id": data.workspace_id or data.space_id,
        "app_name": data.app_name,
        "run_id": data.run_id,
        "mapping_result": data.mapping_result
    }
    item = sanitize_numbers(item)
    mapping_container.replace_one({"id": doc_id}, item, upsert=True)
    return {"message": f"Inserted mapping for folder '{identifier}'"}

@app.patch("/mapping/{app_id}")
@retry_db_operation()
def patch_mapping(app_id: str, data: MappingData, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(mapping_container, app_id, workspace_id or data.workspace_id, run_id or data.run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    doc = items[0]
    if data.run_id: doc["run_id"] = data.run_id
    if data.workspace_id or data.space_id: doc["workspace_id"] = data.workspace_id or data.space_id
    if data.mapping_result is not None: doc["mapping_result"] = data.mapping_result
    mapping_container.replace_one({"id": doc["id"]}, doc, upsert=True)
    return {"message": f"Patched mapping for folder '{app_id}'"}

@app.delete("/mapping/{app_id}")
@retry_db_operation()
def delete_mapping(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(mapping_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    for item in items:
        mapping_container.delete_one({"id": item["id"]})
    return {"message": f"Deleted {len(items)} mapping record(s) for folder '{app_id}'"}


# ==============================================================================
# 7. ASSESSMENT
# ==============================================================================
@app.get("/assessment")
@retry_db_operation()
def get_all_assessment():
    items = list(assessment_container.find({}))
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "assessment_result": item.get("assessment_result")
        }
        for item in sanitize_document(items)
    ]

@app.get("/assessment/by-run/{run_id}")
@retry_db_operation()
def get_assessment_by_run(run_id: str):
    items = find_by_identifier(assessment_container, run_id)
    if not items:
        return {"message": f"No record found for run_id '{run_id}'"}
    return sanitize_document(items)

@app.get("/assessment/by-app/{app_id}")
@retry_db_operation()
def get_assessment_by_app(app_id: str):
    items = find_by_identifier(assessment_container, app_id)
    if not items:
        return {"message": f"No record found for app_id '{app_id}'"}
    return sanitize_document(items)

@app.get("/assessment/{app_id}")
@retry_db_operation()
def get_assessment(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(assessment_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "assessment_result": item.get("assessment_result")
        }
        for item in sanitize_document(items)
    ]

@app.post("/assessment")
@retry_db_operation()
def upsert_assessment(data: AssessmentData):
    identifier = data.app_id or data.folder_name or data.run_id
    if not identifier:
        return {"message": "Either app_id, folder_name or run_id must be provided"}

    # Clean previous record(s) for this folder/app_id
    folder_ref = data.app_id or data.folder_name
    if folder_ref:
        assessment_container.delete_many({"$or": [{"app_id": folder_ref}, {"folder_name": folder_ref}]})
    elif data.run_id:
        assessment_container.delete_many({"run_id": data.run_id})

    doc_id = str(uuid.uuid4())

    item = {
        "id": doc_id,
        "folder_name": data.folder_name or data.app_id,
        "app_id": data.app_id or data.folder_name,
        "space_id": data.space_id or data.workspace_id,
        "workspace_id": data.workspace_id or data.space_id,
        "app_name": data.app_name,
        "run_id": data.run_id,
        "assessment_result": data.assessment_result
    }
    item = sanitize_numbers(item)
    assessment_container.replace_one({"id": doc_id}, item, upsert=True)
    return {"message": f"Inserted assessment for folder '{identifier}'"}

@app.patch("/assessment/{app_id}")
@retry_db_operation()
def patch_assessment(app_id: str, data: AssessmentData, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(assessment_container, app_id, workspace_id or data.workspace_id, run_id or data.run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    doc = items[0]
    if data.run_id: doc["run_id"] = data.run_id
    if data.workspace_id or data.space_id: doc["workspace_id"] = data.workspace_id or data.space_id
    if data.assessment_result is not None: doc["assessment_result"] = data.assessment_result
    assessment_container.replace_one({"id": doc["id"]}, doc, upsert=True)
    return {"message": f"Patched assessment for folder '{app_id}'"}

@app.delete("/assessment/{app_id}")
@retry_db_operation()
def delete_assessment(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(assessment_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    for item in items:
        assessment_container.delete_one({"id": item["id"]})
    return {"message": f"Deleted {len(items)} assessment record(s) for folder '{app_id}'"}


# ==============================================================================
# 8. REPORT GENERATION & VALIDATION
# ==============================================================================
@app.get("/report-generation")
@app.get("/report")
@retry_db_operation()
def get_all_report_generation():
    items = list(report_generation_container.find({}))
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "report_result": item.get("report_result")
        }
        for item in sanitize_document(items)
    ]

@app.get("/report-generation/by-run/{run_id}")
@app.get("/report/by-run/{run_id}")
@retry_db_operation()
def get_report_generation_by_run(run_id: str):
    items = find_by_identifier(report_generation_container, run_id)
    if not items:
        return {"message": f"No record found for run_id '{run_id}'"}
    return sanitize_document(items)

@app.get("/report-generation/{app_id}")
@app.get("/report/{app_id}")
@retry_db_operation()
def get_report_generation(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(report_generation_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "report_result": item.get("report_result")
        }
        for item in sanitize_document(items)
    ]

@app.post("/report-generation")
@app.post("/report")
@retry_db_operation()
def upsert_report_generation(data: ReportGenerationData):
    identifier = data.app_id or data.folder_name or data.run_id
    if not identifier:
        return {"message": "Either app_id, folder_name or run_id must be provided"}

    # Clean previous record(s) for this folder/app_id
    folder_ref = data.app_id or data.folder_name
    if folder_ref:
        report_generation_container.delete_many({"$or": [{"app_id": folder_ref}, {"folder_name": folder_ref}]})
    elif data.run_id:
        report_generation_container.delete_many({"run_id": data.run_id})

    doc_id = str(uuid.uuid4())

    item = {
        "id": doc_id,
        "folder_name": data.folder_name or data.app_id,
        "app_id": data.app_id or data.folder_name,
        "space_id": data.space_id or data.workspace_id,
        "workspace_id": data.workspace_id or data.space_id,
        "app_name": data.app_name,
        "run_id": data.run_id,
        "report_result": data.report_result
    }
    item = sanitize_numbers(item)
    report_generation_container.replace_one({"id": doc_id}, item, upsert=True)
    return {"message": f"Inserted report generation for '{identifier}'"}

@app.patch("/report-generation/{app_id}")
@app.patch("/report/{app_id}")
@retry_db_operation()
def patch_report_generation(app_id: str, data: ReportGenerationData, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(report_generation_container, app_id, workspace_id or data.workspace_id, run_id or data.run_id)
    if not items:
        return {"message": f"No report generation record found for '{app_id}'"}
    doc = items[0]
    if data.run_id: doc["run_id"] = data.run_id
    if data.workspace_id or data.space_id: doc["workspace_id"] = data.workspace_id or data.space_id
    if data.report_result is not None: doc["report_result"] = data.report_result
    report_generation_container.replace_one({"id": doc["id"]}, doc, upsert=True)
    return {"message": f"Patched report generation for '{app_id}'"}

@app.delete("/report-generation/{app_id}")
@app.delete("/report/{app_id}")
@retry_db_operation()
def delete_report_generation(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(report_generation_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    for item in items:
        report_generation_container.delete_one({"id": item["id"]})
    return {"message": f"Deleted {len(items)} report generation record(s) for folder '{app_id}'"}

# --- Validation ---
@app.get("/validation/{app_id}")
@retry_db_operation()
def get_validation(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(validation_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    return [
        {
            "id": item.get("id"),
            "run_id": item.get("run_id"),
            "workspace_id": item.get("workspace_id") or item.get("space_id"),
            "app_id": item.get("app_id") or item.get("folder_name"),
            "validation_result": item.get("validation_result")
        }
        for item in sanitize_document(items)
    ]

@app.post("/validation")
@retry_db_operation()
def upsert_validation(data: ValidationData):
    identifier = data.app_id or data.folder_name or data.run_id
    if not identifier:
        return {"message": "Either app_id, folder_name or run_id must be provided"}

    items = find_by_identifier(validation_container, identifier, data.workspace_id or data.space_id, data.run_id)
    doc_id = items[0]["id"] if items else str(uuid.uuid4())

    item = {
        "id": doc_id,
        "folder_name": data.folder_name or data.app_id,
        "app_id": data.app_id or data.folder_name,
        "space_id": data.space_id or data.workspace_id,
        "workspace_id": data.workspace_id or data.space_id,
        "app_name": data.app_name,
        "run_id": data.run_id,
        "validation_result": data.validation_result
    }
    item = sanitize_numbers(item)
    validation_container.replace_one({"id": doc_id}, item, upsert=True)
    msg_type = "Updated" if items else "Inserted"
    return {"message": f"{msg_type} validation for '{identifier}'"}

@app.patch("/validation/{app_id}")
@retry_db_operation()
def patch_validation(app_id: str, data: ValidationData, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(validation_container, app_id, workspace_id or data.workspace_id, run_id or data.run_id)
    if not items:
        return {"message": f"No validation record found for '{app_id}'"}
    doc = items[0]
    if data.run_id: doc["run_id"] = data.run_id
    if data.workspace_id or data.space_id: doc["workspace_id"] = data.workspace_id or data.space_id
    if data.validation_result is not None: doc["validation_result"] = data.validation_result
    validation_container.replace_one({"id": doc["id"]}, doc, upsert=True)
    return {"message": f"Patched validation for '{app_id}'"}

@app.delete("/validation/{app_id}")
@retry_db_operation()
def delete_validation(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(validation_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No record found for folder '{app_id}'"}
    for item in items:
        validation_container.delete_one({"id": item["id"]})
    return {"message": f"Deleted {len(items)} validation record(s) for folder '{app_id}'"}


# ==============================================================================
# 9. RUN HISTORY
# ==============================================================================
def _format_run_history_item(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": item.get("id"),
        "run_id": item.get("run_id"),
        "workspace_id": item.get("workspace_id") or item.get("space_id"),
        "timestamp": item.get("timestamp"),
        "app_id": item.get("app_id") or item.get("folder_name"),
        "app_name": item.get("app_name"),
        "user_email": item.get("user_email"),
        "parsing_status": item.get("parsing_status"),
        "parsing_message": item.get("parsing_message"),
        "mapping_status": item.get("mapping_status"),
        "mapping_message": item.get("mapping_message"),
        "assessment_status": item.get("assessment_status"),
        "assessment_message": item.get("assessment_message"),
        "report_generation_status": item.get("report_generation_status"),
        "report_generation_message": item.get("report_generation_message"),
        "devops_fabric_sync_status": item.get("devops_fabric_sync_status"),
        "devops_fabric_sync_message": item.get("devops_fabric_sync_message"),
        "connection_id": item.get("connection_id"),
        "server_url": item.get("server_url"),
    }

@app.get("/run-history")
@retry_db_operation()
def get_all_run_history(
    run_id: Optional[str] = Query(None),
    workspace_id: Optional[str] = Query(None),
    app_id: Optional[str] = Query(None),
):
    query: Dict[str, Any] = {}
    if run_id: query["run_id"] = run_id
    if workspace_id: query["workspace_id"] = workspace_id
    if app_id: query["$or"] = [{"app_id": app_id}, {"folder_name": app_id}]

    items = list(run_history_container.find(query).sort("timestamp", -1))
    return [_format_run_history_item(item) for item in sanitize_document(items)]

@app.post("/run-history")
@retry_db_operation()
def create_run_history(data: RunHistory):
    now = datetime.utcnow().isoformat()
    doc_id = data.id or str(uuid.uuid4())
    item = {
        "id": doc_id,
        "run_id": data.run_id,
        "workspace_id": data.workspace_id or data.space_id,
        "timestamp": data.timestamp or now,
        "app_id": data.app_id or data.folder_name,
        "folder_name": data.folder_name or data.app_id,
        "app_name": data.app_name,
        "user_email": data.user_email,
        "parsing_status": data.parsing_status,
        "parsing_message": data.parsing_message,
        "mapping_status": data.mapping_status,
        "mapping_message": data.mapping_message,
        "assessment_status": data.assessment_status,
        "assessment_message": data.assessment_message,
        "report_generation_status": data.report_generation_status,
        "report_generation_message": data.report_generation_message,
        "devops_fabric_sync_status": data.devops_fabric_sync_status,
        "devops_fabric_sync_message": data.devops_fabric_sync_message,
        "connection_id": data.connection_id,
        "server_url": data.server_url,
    }
    run_history_container.replace_one({"id": doc_id}, item, upsert=True)
    return {"message": f"Logged run history for folder '{data.app_id or data.folder_name}' by user '{data.user_email}'"}

@app.get("/run-history/by-folder/{app_id}")
@retry_db_operation()
def get_run_history_by_folder(
    app_id: str,
    workspace_id: Optional[str] = Query(None),
    run_id: Optional[str] = Query(None),
    user_email: Optional[str] = Query(None),
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    page: Optional[int] = Query(1, ge=1),
    page_size: Optional[int] = Query(10, ge=1, le=100),
):
    query: Dict[str, Any] = {"$or": [{"app_id": app_id}, {"folder_name": app_id}]}
    if workspace_id: query["workspace_id"] = workspace_id
    if run_id: query["run_id"] = run_id
    if user_email: query["user_email"] = user_email
    if start_date: query["timestamp"] = {"$gte": start_date}
    if end_date:
        if "timestamp" in query:
            query["timestamp"]["$lte"] = end_date
        else:
            query["timestamp"] = {"$lte": end_date}

    skip = (page - 1) * page_size
    items = list(run_history_container.find(query).sort("timestamp", -1).skip(skip).limit(page_size))
    if not items:
        return {"message": f"No run history found for app_id '{app_id}' with provided filters"}
    return [_format_run_history_item(item) for item in sanitize_document(items)]

@app.get("/run-history/by-email/{user_email}")
@retry_db_operation()
def get_run_history_by_email(
    user_email: str,
    app_id: Optional[str] = Query(None),
    page: Optional[int] = Query(1, ge=1),
    page_size: Optional[int] = Query(10, ge=1, le=100)
):
    query: Dict[str, Any] = {"user_email": user_email}
    if app_id: query["$or"] = [{"app_id": app_id}, {"folder_name": app_id}]

    skip = (page - 1) * page_size
    items = list(run_history_container.find(query).sort("timestamp", -1).skip(skip).limit(page_size))
    if not items:
        return {"message": f"No run history found for user_email '{user_email}' with provided filters"}
    return [_format_run_history_item(item) for item in sanitize_document(items)]

@app.get("/run-history/{app_id}")
@retry_db_operation()
def get_single_run_history(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(run_history_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No run history found for '{app_id}'"}
    return [_format_run_history_item(item) for item in sanitize_document(items)]

@app.patch("/run-history/{app_id}")
@retry_db_operation()
def update_run_history(
    app_id: str,
    data: RunHistory,
    workspace_id: Optional[str] = Query(None),
    run_id: Optional[str] = Query(None)
):
    eff_run_id = data.run_id or run_id
    eff_workspace_id = data.workspace_id or data.space_id or workspace_id
    items = find_by_identifier(run_history_container, app_id, eff_workspace_id, eff_run_id)

    if not items:
        item = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "app_id": app_id,
            "folder_name": data.folder_name or app_id,
            "app_name": data.app_name,
            "workspace_id": eff_workspace_id,
            "run_id": eff_run_id,
            "user_email": data.user_email
        }
        for k, v in model_to_dict(data, exclude_unset=True).items():
            if v is not None:
                item[k] = v
        run_history_container.insert_one(item)
        return {"message": f"Created run history for '{app_id}'"}

    item = items[0]
    for key, val in model_to_dict(data, exclude_unset=True).items():
        if val is not None:
            item[key] = val
    if eff_run_id: item["run_id"] = eff_run_id
    if eff_workspace_id: item["workspace_id"] = eff_workspace_id

    doc_id = item["id"]
    run_history_container.replace_one({"id": doc_id}, item, upsert=True)
    return {"message": f"Updated run history for folder '{app_id}'"}

@app.delete("/run-history/{app_id}")
@retry_db_operation()
def delete_run_history(app_id: str, workspace_id: Optional[str] = Query(None), run_id: Optional[str] = Query(None)):
    items = find_by_identifier(run_history_container, app_id, workspace_id, run_id)
    if not items:
        return {"message": f"No run history found for app_id '{app_id}'"}
    for item in items:
        run_history_container.delete_one({"id": item["id"]})
    return {"message": f"Deleted {len(items)} run history record(s) for folder '{app_id}'"}


# ==============================================================================
# 10. SEMANTIC KERNEL RESULTS & SUMMARY AGGREGATOR
# ==============================================================================
def _format_semantic_kernel_item(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": item.get("id"),
        "run_id": item.get("run_id"),
        "workspace_id": item.get("workspace_id") or item.get("space_id"),
        "app_id": item.get("app_id") or item.get("folder_name"),
        "email_id": item.get("email_id") or item.get("user_email"),
        "user_email": item.get("user_email") or item.get("email_id"),
        "project_name": item.get("project_name"),
        "status": item.get("status"),
        "total_apps": item.get("total_apps", 0),
        "total_migrated": item.get("total_migrated", 0),
        "total_failed": item.get("total_failed", 0),
        "total_cancelled": item.get("total_cancelled", 0),
        "total_pending": item.get("total_pending", 0),
        "total_generation_completed": item.get("total_generation_completed", 0),
        "total_ran_till_parsing": item.get("total_ran_till_parsing", 0),
        "total_validation_skipped": item.get("total_validation_skipped", 0),
        "run_no": item.get("run_no"),
        "execution_level": item.get("execution_level"),
        "workspace_type": item.get("workspace_type"),
        "app_type": item.get("app_type"),
        "start_date_time": item.get("start_date_time"),
        "end_date_time": item.get("end_date_time"),
        "time_duration": item.get("time_duration"),
        "time_elapsed": item.get("time_elapsed"),
        "deployment_type": item.get("deployment_type"),
        "payload": item.get("payload")
    }

@app.get("/api/records/semantic-kernel")
@retry_db_operation()
def get_semantic_kernel_records(
    run_id: Optional[str] = Query(None),
    workspace_id: Optional[str] = Query(None),
    app_id: Optional[str] = Query(None),
    email_id: Optional[str] = Query(None),
    user_email: Optional[str] = Query(None),
    status: Optional[str] = Query(None)
):
    query: Dict[str, Any] = {}
    if run_id:
        query["$or"] = [{"run_id": run_id}, {"id": run_id}]
    if workspace_id:
        query["$or"] = [{"workspace_id": workspace_id}, {"payload.workspace_id": workspace_id}]
    if app_id:
        query["$or"] = [{"app_id": app_id}, {"payload.app_id": app_id}]

    effective_email = email_id or user_email
    if effective_email:
        query["$or"] = [
            {"email_id": effective_email},
            {"user_email": effective_email},
            {"payload.user_email": effective_email},
            {"payload.email_id": effective_email}
        ]
    if status:
        query["status"] = status

    items = list(semantic_kernel_container.find(query).sort("_id", -1))
    if not items:
        return {"message": "No semantic kernel results found"}
    return [_format_semantic_kernel_item(item) for item in sanitize_document(items)]

@app.get("/api/records/semantic-kernel/summary")
@retry_db_operation()
def get_semantic_kernel_summary(
    email_id: Optional[str] = Query(None),
    user_email: Optional[str] = Query(None),
    workspace_id: Optional[str] = Query(None),
    run_id: Optional[str] = Query(None)
):
    """Aggregate monitoring metrics across Semantic Kernel records"""
    query: Dict[str, Any] = {}
    effective_email = (email_id or user_email or "").strip().lower()
    if effective_email:
        query["$or"] = [
            {"email_id": {"$regex": f"^{effective_email}$", "$options": "i"}},
            {"user_email": {"$regex": f"^{effective_email}$", "$options": "i"}},
            {"payload.user_email": {"$regex": f"^{effective_email}$", "$options": "i"}},
            {"payload.email_id": {"$regex": f"^{effective_email}$", "$options": "i"}}
        ]
    if workspace_id:
        query["$or"] = [{"workspace_id": workspace_id}, {"payload.workspace_id": workspace_id}]
    if run_id:
        query["$or"] = [{"run_id": run_id}, {"id": run_id}]

    items = list(semantic_kernel_container.find(query))

    unique_run_ids = set()
    total_runs = 0
    total_apps = 0
    total_migrated = 0
    total_generation_completed = 0
    total_ran_till_parsing = 0
    total_failed = 0
    total_pending = 0
    total_cancelled = 0
    total_validation_skipped = 0

    for item in items:
        rid = item.get("run_id") or item.get("id")
        if rid:
            if rid in unique_run_ids:
                continue
            unique_run_ids.add(rid)
        total_runs += 1

        payload = item.get("payload") or {}
        processed_items = payload.get("processed_items") or []

        if processed_items:
            item_apps = len(processed_items)
            migrated_cnt = 0
            gen_comp_cnt = 0
            ran_till_parsing_cnt = 0
            failed_cnt = 0
            pending_cnt = 0
            cancelled_cnt = 0
            val_skipped_cnt = 0

            for p in processed_items:
                final_status = str(p.get("final_status") or p.get("status") or "").strip().upper()
                steps = p.get("steps") or {}
                rep_gen_status = str(steps.get("report_generation") or steps.get("generation") or "").upper()
                pars_status = str(steps.get("parsing") or "").upper()
                val_status = str(steps.get("validation") or "").upper()

                if final_status in ["FAILED", "ERROR", "VALIDATION_FAILED"]:
                    failed_cnt += 1
                elif "CANCELLED" in final_status or final_status in ["STOPPED", "HALTED"]:
                    cancelled_cnt += 1
                elif final_status in ["IN PROGRESS", "RUNNING", "PROCESSING", "PENDING"]:
                    pending_cnt += 1
                elif val_status == "COMPLETED" or final_status in ["SUCCESS", "COMPLETED", "FULL_MIGRATION_COMPLETED"]:
                    migrated_cnt += 1
                elif rep_gen_status == "COMPLETED":
                    gen_comp_cnt += 1
                    if val_status == "SKIPPED":
                        val_skipped_cnt += 1
                elif final_status == "RAN TILL PARSING" or pars_status == "COMPLETED":
                    ran_till_parsing_cnt += 1

            total_apps += item_apps
            total_migrated += migrated_cnt
            total_generation_completed += gen_comp_cnt
            total_ran_till_parsing += ran_till_parsing_cnt
            total_failed += failed_cnt
            total_pending += pending_cnt
            total_cancelled += cancelled_cnt
            total_validation_skipped += val_skipped_cnt
        else:
            total_apps += item.get("total_apps") or 0
            total_migrated += item.get("total_migrated") or 0
            total_generation_completed += item.get("total_generation_completed") or 0
            total_ran_till_parsing += item.get("total_ran_till_parsing") or 0
            total_failed += item.get("total_failed") or 0
            total_pending += item.get("total_pending") or 0
            total_cancelled += item.get("total_cancelled") or 0
            total_validation_skipped += item.get("total_validation_skipped") or 0
    return {
        "total_runs": total_runs,
        "total_apps": total_apps,
        "total_workbooks": total_apps,
        "total_generation_completed": total_generation_completed,
        "apps_with_generation_completed": total_generation_completed,
        "total_migrated": total_migrated,
        "apps_with_fully_migrated": total_migrated,
        "total_ran_till_parsing": total_ran_till_parsing,
        "apps_that_ran_till_parsing": total_ran_till_parsing,
        "total_failed": total_failed,
        "total_pending": total_pending,
        "in_progress": total_pending,
        "total_cancelled": total_cancelled,
        "total_validation_skipped": total_validation_skipped
    }

@app.get("/api/records/semantic-kernel/{run_id}")
@retry_db_operation()
def get_semantic_kernel_single_run(run_id: str):
    doc = semantic_kernel_container.find_one({"$or": [{"run_id": run_id}, {"id": run_id}]})
    if not doc:
        raise HTTPException(status_code=404, detail=f"No semantic kernel record found for run '{run_id}'")
    return _format_semantic_kernel_item(sanitize_document(doc))

@app.post("/api/records/semantic-kernel")
@retry_db_operation()
def upsert_semantic_kernel_record(data: SemanticKernelData):
    run_id = data.run_id or str(uuid.uuid4())
    existing = list(semantic_kernel_container.find({"$or": [{"run_id": run_id}, {"id": run_id}]}))

    doc_id = existing[0]["id"] if existing else run_id
    item = model_to_dict(data, exclude_unset=True)
    item["id"] = doc_id
    item["run_id"] = run_id

    item = sanitize_numbers(item)
    semantic_kernel_container.replace_one({"id": doc_id}, item, upsert=True)
    return {"message": "Semantic kernel result stored", "run_id": run_id, "id": doc_id}

@app.patch("/api/records/semantic-kernel")
@app.patch("/api/records/semantic-kernel/{run_id}")
@retry_db_operation()
def patch_semantic_kernel_record(data: SemanticKernelData, run_id: Optional[str] = None):
    eff_run_id = run_id or data.run_id
    if not eff_run_id:
        raise HTTPException(status_code=400, detail="run_id must be provided")

    existing = list(semantic_kernel_container.find({"$or": [{"run_id": eff_run_id}, {"id": eff_run_id}]}))
    doc = existing[0] if existing else {"id": eff_run_id, "run_id": eff_run_id}

    for k, v in model_to_dict(data, exclude_unset=True).items():
        if v is not None:
            doc[k] = v
    doc["run_id"] = eff_run_id
    doc = sanitize_numbers(doc)

    semantic_kernel_container.replace_one({"id": doc["id"]}, doc, upsert=True)
    return {"message": "Semantic kernel result updated", "run_id": eff_run_id, "id": doc["id"]}

@app.delete("/api/records/semantic-kernel/{run_id}")
@retry_db_operation()
def delete_semantic_kernel_record(run_id: str):
    res = semantic_kernel_container.delete_many({"$or": [{"run_id": run_id}, {"id": run_id}]})
    return {"message": f"Deleted {res.deleted_count} semantic kernel record(s) for run '{run_id}'"}


# ==============================================================================
# FILE STORAGE (GridFS) -- replaces Azure Blob Storage for binary artifacts
# (e.g. Tableau .twbx workbooks) too large for a normal document. "container"
# groups files the same way an Azure Blob container did (e.g. "t2fworkbooks").
# ==============================================================================
@app.post("/files/{container}/{key:path}")
async def upload_file(container: str, key: str, request: Request):
    """Uploads/overwrites a file. Body is the raw file bytes."""
    data = await request.body()
    if not data:
        raise HTTPException(status_code=400, detail="Empty file body")

    # Remove any previous version under the same container+key so downloads
    # always resolve the latest upload without needing separate version tracking.
    for existing in fs.find({"filename": key, "container": container}):
        fs.delete(existing._id)

    file_id = fs.put(
        data,
        filename=key,
        container=container,
        content_type=request.headers.get("content-type", "application/octet-stream"),
        uploaded_at=datetime.utcnow().isoformat(),
    )
    return {"id": str(file_id), "container": container, "key": key, "size": len(data)}


@app.get("/files/{container}/{key:path}")
def download_file(container: str, key: str):
    """Downloads a file's raw bytes."""
    grid_out = fs.find_one({"filename": key, "container": container})
    if not grid_out:
        raise HTTPException(status_code=404, detail=f"File '{key}' not found in container '{container}'")
    return Response(
        content=grid_out.read(),
        media_type=getattr(grid_out, "content_type", None) or "application/octet-stream"
    )


@app.get("/files/{container}")
def list_files(container: str, prefix: Optional[str] = None):
    """Lists files in a container, optionally filtered by a filename prefix."""
    query: Dict[str, Any] = {"container": container}
    if prefix:
        query["filename"] = {"$regex": f"^{re.escape(prefix)}"}
    items = []
    for grid_out in fs.find(query):
        items.append({
            "key": grid_out.filename,
            "size": grid_out.length,
            "uploaded_at": getattr(grid_out, "uploaded_at", None),
        })
    return items


@app.delete("/files/{container}/{key:path}")
def delete_file(container: str, key: str):
    """Deletes a file (all versions under the same container+key)."""
    deleted = 0
    for existing in fs.find({"filename": key, "container": container}):
        fs.delete(existing._id)
        deleted += 1
    if deleted == 0:
        raise HTTPException(status_code=404, detail=f"File '{key}' not found in container '{container}'")
    return {"message": f"Deleted {deleted} version(s) of '{key}' from '{container}'"}


if __name__ == '__main__':
    import uvicorn
    port = int(os.getenv("PORT", 8008))
    uvicorn.run(app, host='0.0.0.0', port=port)