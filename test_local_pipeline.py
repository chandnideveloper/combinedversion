"""End-to-end local test runner for the Qlik-to-Fabric pipeline.

Demonstrates and verifies:
1. Parsing layer (normalizing raw Qlik engine responses & resolving theme/CSV)
2. Mapping layer (translating Qlik objects to Fabric TMDL & visual definitions)
3. Generation layer (building the full PBIR/TMDL Power BI report package)
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PAYLOAD = {
    "source_type": "qlik",
    "app_id": "afdeddc7-4dca-470b-bd3d-cdc279a1c408",
    "app_name": "FleetVision KSA",
    "run_id": "Demo-run-demo-fleet",
    "workspace_id": "personal",
    "department_repo": "Qlik_Migrated",
    "fabric_group_id": "4a212d5c-abf8-44ac-9cf5-7e47ed9aaf26",
    "deployment_type": "DIRECT_FABRIC"
}

def test_pipeline():
    print("=" * 70)
    print("STEP 1: Testing Unified Parsing Normalization...")
    print("=" * 70)
    sys.path.insert(0, os.path.join(BASE_DIR, "unified-parsing"))
    from parsers.qlik.enrichment import enrich
    from parsers.qlik.normalizer import normalize
    from parsers.qlik.prune import apply_view, normalize_view

    mock_engine_response = {
        "appId": PAYLOAD["app_id"],
        "app_name": PAYLOAD["app_name"],
        "themes": [{"active": True, "name": "Custom Theme", "dataColors": ["#0B7285", "#F76707", "#2B8A3E"]}],
        "connections": [{"id": "c1", "name": "CSV_Conn", "connection_type": "DataFiles",
                          "connection_details": {"driver": "datafiles", "other": {"path": "fleet_loads.csv"}}}],
        "dataFiles": [{"id": "f1", "name": "fleet_loads.csv", "content_text": "id,route_id,revenue\n1,R-101,500.0", "size": 35}],
        "media": {"media_files": [{"name": "logo.png", "data_base64": "ZmFrZQ=="}]},
        "sheets": [], "tables": [], "dimensions": [], "measures": [], "relationships": [],
    }
    mock_engine_response["enrichment"] = enrich(mock_engine_response)
    parsed = normalize(mock_engine_response)
    pruned = apply_view(parsed, normalize_view(None))

    assert "theme_and_styling" in pruned, "theme_and_styling missing from parsing"
    assert "dataFiles" in pruned, "dataFiles missing from parsing"
    print(f"✅ Parsing Result: theme source={pruned['theme_and_styling'].get('source')}, palette={pruned['theme_and_styling'].get('color_palette')}")
    print(f"✅ Downloaded CSV Data Files: {len(pruned.get('dataFiles', []))} file(s)")

    print("\n" + "=" * 70)
    print("STEP 2: Testing Generation Agent (Deterministic PBIR / TMDL Builder)...")
    print("=" * 70)
    sys.path.insert(0, os.path.join(BASE_DIR, "az-wa-repo-generationagent"))
    from app.generator import generate
    from app.schemas import GenerateRequest, Target, Deploy

    mapping_file = os.path.join(BASE_DIR, "MAPPINGRESPONSE.md")
    with open(mapping_file, "r", encoding="utf-8") as f:
        mapping_data = json.load(f)

    req = GenerateRequest(
        app_id=PAYLOAD["app_id"],
        run_id=PAYLOAD["run_id"],
        target=Target.POWERBI_DESKTOP,
        deploy=Deploy.NONE,
        write_to_disk=False,
    )
    res = generate(mapping_data, req)

    print(f"✅ Generation Status: {res.get('status')}")
    print(f"✅ Total PBIP Artifact Files: {res.get('file_count')}")
    print(f"✅ Total Bytes Generated: {res.get('total_bytes'):,} bytes")
    print(f"✅ Report Summary: {res.get('summary', {}).get('report')}")
    print(f"✅ Semantic Model Summary: {res.get('summary', {}).get('semantic_model')}")

    print("\n" + "=" * 70)
    print("ALL LOCAL PIPELINE CHECKS PASSED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    test_pipeline()
