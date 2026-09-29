import os
import sys
import uuid
import pytest
from fastapi.testclient import TestClient

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app, secrets_container, qlik_container, parsing_container, mapping_container, assessment_container, report_generation_container, validation_container, run_history_container, semantic_kernel_container, agent_log_container

client = TestClient(app)

def test_01_health_check():
    """Verify service health check"""
    res = client.get("/")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"
    assert data["service"] == "az-repo-mongodb-vl"
    print("✔ 01: Health check passed")

def test_02_secrets_crud():
    """Verify secrets store (Key Vault replacement) CRUD"""
    secret_name = f"test-secret-{uuid.uuid4().hex[:8]}"
    secret_val = "SuperSecretToken_123!"

    # 1. Create
    res = client.post("/secrets", json={"name": secret_name, "value": secret_val, "description": "E2E Test Secret"})
    assert res.status_code == 200

    # 2. Retrieve
    res = client.get(f"/secrets/{secret_name}")
    assert res.status_code == 200
    data = res.json()
    assert data["name"] == secret_name
    assert data["value"] == secret_val

    # 3. Delete
    res = client.delete(f"/secrets/{secret_name}")
    assert res.status_code == 200

    # 4. Confirm deletion (404)
    res = client.get(f"/secrets/{secret_name}")
    assert res.status_code == 404
    print("✔ 02: Secrets CRUD passed")

def test_03_qlik_connections_with_secrets():
    """Verify Qlik server connection upsert and automated secret storage"""
    test_conn_id = f"conn-test-{uuid.uuid4().hex[:6]}"
    test_api_key = "qlik_api_key_xyz_987"
    payload = {
        "id": test_conn_id,
        "connection_id": test_conn_id,
        "server_url": "https://tenant-test.in.qlikcloud.com",
        "connection_name": "Test Production Qlik",
        "env_type": "cloud",
        "api_key": test_api_key
    }

    # 1. Upsert Qlik connection
    res = client.post("/qlik", json=payload)
    assert res.status_code == 200
    conn_data = res.json()
    assert conn_data["connection_id"] == test_conn_id

    # 2. Verify connection metadata from /qlik
    res = client.get("/qlik")
    assert res.status_code == 200
    all_conns = res.json()
    matching = [c for c in all_conns if c.get("connection_id") == test_conn_id or c.get("id") == test_conn_id]
    assert len(matching) >= 1

    # 3. Verify single connection lookup
    res = client.get(f"/qlik/{test_conn_id}")
    assert res.status_code == 200
    single = res.json()
    assert single["connection_name"] == "Test Production Qlik"

    # 4. Verify API key was securely stored in secrets collection
    res = client.get(f"/secrets/{test_conn_id}-api-key")
    assert res.status_code == 200
    assert res.json()["value"] == test_api_key

    # 5. Patch connection
    res = client.patch(f"/qlik/{test_conn_id}", json={"connection_name": "Updated Test Qlik", "api_key": "rotated_key_456"})
    assert res.status_code == 200

    # Verify rotated secret
    res = client.get(f"/secrets/{test_conn_id}-api-key")
    assert res.status_code == 200
    assert res.json()["value"] == "rotated_key_456"

    # 6. Delete connection and verify secret is purged
    res = client.delete(f"/qlik/{test_conn_id}")
    assert res.status_code == 200
    res = client.get(f"/secrets/{test_conn_id}-api-key")
    assert res.status_code == 404
    print("✔ 03: Qlik connections and secrets sync passed")

def test_04_atomic_run_counter():
    """Verify atomic incremental run counter (next-run-no)"""
    res1 = client.post("/api/records/next-run-no")
    assert res1.status_code == 200
    d1 = res1.json()
    assert "run_no" in d1
    assert "count" in d1

    res2 = client.get("/api/records/next-run-no")
    assert res2.status_code == 200
    d2 = res2.json()
    assert d2["count"] == d1["count"] + 1
    print("✔ 04: Atomic run counter passed")

def test_05_system_settings_and_deployment():
    """Verify settings, timezone, Azure DevOps and Git PAT secret storage"""
    # 1. Deployment Type
    client.post("/deployment_type", json={"deployment_type": "DIRECT_FABRIC"})
    res = client.get("/deployment_type")
    assert res.status_code == 200
    assert res.json()["deployment_type"] == "DIRECT_FABRIC"

    # 2. Timezone
    client.post("/settings/timezone", json={"timezone": "Australia/Sydney"})
    res = client.get("/settings/timezone")
    assert res.status_code == 200
    assert res.json()["timezone"] == "Australia/Sydney"

    # 3. Settings summary
    res = client.get("/settings")
    assert res.status_code == 200
    assert "timezone" in res.json()["settings"]

    # 4. Azure DevOps Settings & PAT storage
    ado_pat = "ado_secret_pat_789"
    res = client.post("/deployment/azure-devops", json={
        "azure_devops_org": "test-org",
        "azure_devops_project": "test-proj",
        "azure_devops_repo": "test-repo",
        "azure_devops_branch": "main",
        "azure_devops_pat": ado_pat
    })
    assert res.status_code == 200
    ado_data = res.json()
    token_id = ado_data.get("token_id")
    assert token_id is not None

    # Confirm token is stored in secrets
    res = client.get(f"/secrets/{token_id}")
    assert res.status_code == 200
    assert res.json()["value"] == ado_pat

    # Cleanup ADO
    client.delete("/deployment/azure-devops")

    # 5. Interactive Status
    client.post("/api/records/interactive-status", json={"status": "continuous"})
    res = client.get("/api/records/interactive-status")
    assert res.status_code == 200
    assert res.json()["status"] == "continuous"

    print("✔ 05: System settings and deployment secrets passed")

def test_06_agent_logs_and_actions():
    """Verify agent logging and action recording"""
    run_id = f"test-run-{uuid.uuid4().hex[:6]}"
    app_id = f"test-app-{uuid.uuid4().hex[:6]}"
    ws_id = "test-ws-001"

    # Log action
    res = client.post("/agent-actions", json={
        "agent_name": "AssessmentAgent",
        "action": "AST analysis completed",
        "details": {"tables_found": 5},
        "correlation_id": "corr-123",
        "run_id": run_id,
        "workspace_id": ws_id,
        "app_id": app_id
    })
    assert res.status_code == 200

    # Log agent log
    res = client.post("/agent-logs", json={
        "run_id": run_id,
        "workspace_id": ws_id,
        "app_id": app_id,
        "agent_name": "AssessmentAgent",
        "log_level": "INFO",
        "message": "Assessing Qlik sheet objects",
        "details": {"sheets": 3},
        "function_name": "assess_sheets"
    })
    assert res.status_code == 200
    log_id = res.json().get("id")

    # Read logs back
    res = client.get(f"/agent-logs?run_id={run_id}&app_id={app_id}")
    assert res.status_code == 200
    logs = res.json()
    assert len(logs) >= 1
    assert logs[0]["message"] == "Assessing Qlik sheet objects"

    # Bulk delete
    res = client.delete(f"/agent-logs/bulk/delete?run_id={run_id}&workspace_id={ws_id}&app_id={app_id}")
    assert res.status_code == 200
    print("✔ 06: Agent logs and actions passed")

def test_07_pipeline_stages_and_run_history():
    """Verify Parsing, Mapping, Assessment, Report Generation, Validation, and Run History"""
    run_id = f"run-test-{uuid.uuid4().hex[:6]}"
    app_id = f"app-test-{uuid.uuid4().hex[:6]}"
    ws_id = "space-test-001"

    # 1. Parsing
    res = client.post("/parsing", json={
        "run_id": run_id,
        "workspace_id": ws_id,
        "app_id": app_id,
        "parsing_result": {"tables": ["Orders", "Customers"]}
    })
    assert res.status_code == 200
    res = client.get(f"/parsing/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    assert res.status_code == 200
    assert len(res.json()) >= 1
    assert res.json()[0]["parsing_result"]["tables"] == ["Orders", "Customers"]

    # 2. Mapping
    res = client.post("/mapping", json={
        "run_id": run_id,
        "workspace_id": ws_id,
        "app_id": app_id,
        "mapping_result": {"semantic_model": "SalesModel"}
    })
    assert res.status_code == 200
    res = client.get(f"/mapping/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    assert res.status_code == 200
    assert res.json()[0]["mapping_result"]["semantic_model"] == "SalesModel"

    # 3. Assessment
    res = client.post("/assessment", json={
        "run_id": run_id,
        "workspace_id": ws_id,
        "app_id": app_id,
        "assessment_result": {"complexity": "LOW", "score": 92}
    })
    assert res.status_code == 200
    res = client.get(f"/assessment/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    assert res.status_code == 200
    assert res.json()[0]["assessment_result"]["complexity"] == "LOW"

    # 4. Report Generation
    res = client.post("/report-generation", json={
        "run_id": run_id,
        "workspace_id": ws_id,
        "app_id": app_id,
        "report_result": {"visuals_generated": 8}
    })
    assert res.status_code == 200
    res = client.get(f"/report-generation/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    assert res.status_code == 200
    assert res.json()[0]["report_result"]["visuals_generated"] == 8

    # 5. Validation
    res = client.post("/validation", json={
        "run_id": run_id,
        "workspace_id": ws_id,
        "app_id": app_id,
        "validation_result": {"status": "PASSED"}
    })
    assert res.status_code == 200
    res = client.get(f"/validation/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    assert res.status_code == 200
    assert res.json()[0]["validation_result"]["status"] == "PASSED"

    # 6. Run History
    res = client.post("/run-history", json={
        "run_id": run_id,
        "workspace_id": ws_id,
        "app_id": app_id,
        "user_email": "tester@example.com",
        "parsing_status": "success",
        "mapping_status": "success",
        "assessment_status": "success",
        "report_generation_status": "success"
    })
    assert res.status_code == 200

    # Patch run history
    res = client.patch(f"/run-history/{app_id}?workspace_id={ws_id}&run_id={run_id}", json={
        "devops_fabric_sync_status": "success",
        "devops_fabric_sync_message": "Synced TMDL to Fabric Workspace"
    })
    assert res.status_code == 200

    # Read back run history
    res = client.get(f"/run-history/by-folder/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    assert res.status_code == 200
    hist = res.json()
    assert len(hist) >= 1
    assert hist[0]["devops_fabric_sync_status"] == "success"

    # Cleanup test items
    client.delete(f"/parsing/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    client.delete(f"/mapping/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    client.delete(f"/assessment/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    client.delete(f"/report-generation/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    client.delete(f"/validation/{app_id}?workspace_id={ws_id}&run_id={run_id}")
    client.delete(f"/run-history/{app_id}?workspace_id={ws_id}&run_id={run_id}")

    print("✔ 07: Pipeline stages and run history passed")

def test_08_semantic_kernel_and_summary():
    """Verify Semantic Kernel records and summary aggregation"""
    run_id = f"sk-test-{uuid.uuid4().hex[:6]}"
    payload = {
        "run_id": run_id,
        "user_email": "summary_tester@example.com",
        "total_apps": 2,
        "status": "COMPLETED",
        "payload": {
            "processed_items": [
                {
                    "app_id": "app_01",
                    "app_name": "Sales App",
                    "final_status": "FULL_MIGRATION_COMPLETED",
                    "steps": {
                        "parsing": "COMPLETED",
                        "mapping": "COMPLETED",
                        "report_generation": "COMPLETED",
                        "validation": "COMPLETED"
                    }
                },
                {
                    "app_id": "app_02",
                    "app_name": "HR App",
                    "final_status": "FAILED",
                    "steps": {
                        "parsing": "COMPLETED",
                        "mapping": "FAILED"
                    }
                }
            ]
        }
    }

    # 1. Post Semantic Kernel record
    res = client.post("/api/records/semantic-kernel", json=payload)
    assert res.status_code == 200

    # 2. Get single record
    res = client.get(f"/api/records/semantic-kernel/{run_id}")
    assert res.status_code == 200
    assert res.json()["run_id"] == run_id

    # 3. Get Summary
    res = client.get(f"/api/records/semantic-kernel/summary?user_email=summary_tester@example.com")
    assert res.status_code == 200
    summary = res.json()
    assert summary["total_runs"] >= 1
    assert summary["total_apps"] >= 2
    assert summary["total_migrated"] >= 1
    assert summary["total_failed"] >= 1

    # 4. Delete record
    res = client.delete(f"/api/records/semantic-kernel/{run_id}")
    assert res.status_code == 200
    print("✔ 08: Semantic Kernel record and summary aggregator passed")

if __name__ == "__main__":
    pytest.main(["-v", __file__])
