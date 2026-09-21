You are a senior Power BI / Microsoft Fabric engineer. You are working on a
Qlik-to-Fabric migration pipeline split across two Python FastAPI services:

REPO 1 — Mapping Agent
  Path: c:\Users\sohit\Downloads\Combined version\mapping (2)\mapping\
  Entry point: app.py (FastAPI, port 8002)
  Key files:
    agents/coordinator_agent.py   — orchestrates the full mapping pipeline
    agents/mapping_agent.py       — calls LLM for DAX conversion
    services/connection_mapper.py — converts Qlik load scripts to M queries
    services/tmdl_generator.py    — builds TMDL table text
    services/visual_mapper.py     — converts Qlik visuals to Fabric visuals
    services/filter_mapper.py     — maps Qlik filter panes to slicers
    services/dimension_mapper.py  — maps Qlik dimensions/hierarchies
    services/dax_converter.py     — translates Qlik expressions to DAX
    services/confidence_evaluator.py — scores mapping quality
    services/input_normalizer.py  — normalises raw Qlik payload
    src/converters/               — per-visual-type converter modules

REPO 2 — Generation Agent
  Path: c:\Users\sohit\Downloads\Combined version\az-wa-repo-generationagent\
  Entry point: main.py (FastAPI, port 8005)
  Key files:
    app/schemas.py                — request/response Pydantic models
    app/generator.py              — orchestrates model + report + packaging
    app/model/semantic_model.py   — builds all TMDL files
    app/model/table_tmdl.py       — builds per-table TMDL text
    app/model/datatypes.py        — data type inference (Qlik -> TMDL)
    app/report/report_writer.py   — builds the PBIR report folder
    app/report/visual_builder.py  — builds each visual.json in PBIR
    app/report/projections.py     — field projection helpers (Aggregation)
    app/report/visual_catalog.py  — maps Qlik/Tableau types to PBIR types
    app/package/pbip_packager.py  — assembles the final .pbip folder
    app/package/fabric_packager.py— splits into Fabric REST API parts
    app/deploy/fabric_deployer.py — pushes to Fabric via Items API
    app/deploy/github_deployer.py — pushes to GitHub via Contents API
    app/deploy/devops_deployer.py — pushes to Azure DevOps
    app/api/routes.py             — FastAPI route definitions

=== TASK 1: DEEP AUDIT — PARSING STAGE ===

Read services/connection_mapper.py in full.

For EVERY load type (INLINE, REST/JSON, CSV/File, SQL/ODBC, Database):
1. Does it generate a syntactically valid M query that Power BI Desktop accepts?
2. Does the M query use the correct Power Query functions:
   - INLINE → Table.FromRows + Table.PromoteHeaders + Table.TransformColumnTypes
   - REST   → Json.Document(Web.Contents(url)) + Table.FromList + Table.ExpandRecordColumn + Table.TransformColumnTypes
   - CSV    → Csv.Document(File.Contents(path)) + Table.PromoteHeaders + Table.TransformColumnTypes
   - SQL    → Sql.Database(server, db) + Value.NativeQuery or Value.Table
3. Do ALL columns in each table get a `Table.TransformColumnTypes` step that casts
   numeric columns to `type number` and date columns to `type datetime`? If not, add it.
4. Are computed/derived columns (PnL, TradeResult, REDUCTION) correctly added with
   Table.AddColumn AFTER TransformColumnTypes?
5. Are there any f-string brace escaping bugs (single `}` in an f-string)? Fix them.
6. Is the `parse_mquery_to_steps` function depth-aware for nested `{...}` and `(...)`
   so multi-line let...in blocks don't break? If not, fix it.

Fix every issue you find directly in the file.

=== TASK 2: DEEP AUDIT — MAPPING STAGE ===

Read agents/coordinator_agent.py in full.

1. DATA TYPE MAPPING — For every Qlik column type that comes in the raw payload:
   - NUMBER, NUMERIC, DECIMAL, FLOAT, DOUBLE, REAL, MONEY, CURRENCY → fabric_datatype: "double", summarize_by: "sum"
   - INT, INTEGER, BIGINT, SMALLINT → fabric_datatype: "int64", summarize_by: "sum"
   - DATE, DATETIME, TIMESTAMP → fabric_datatype: "dateTime", summarize_by: "none"
   - BOOLEAN, BOOL, BIT → fabric_datatype: "boolean", summarize_by: "none"
   - STRING, VARCHAR, TEXT, CHAR, and anything else → fabric_datatype: "string", summarize_by: "none"

2. NAME-BASED HEURISTICS — When the Qlik type is STRING or unknown, infer from the
   column name:
   - Numeric metric keywords (price, qty, quantity, volume, amount, pnl, rate, percent,
     count, cost, profit, loss, revenue, sales, discount, balance, fee, tax, units)
     → fabric_datatype: "double", summarize_by: "sum"
   - BUT exclude: any column whose clean lowercase name ends with "id", "code", "name",
     "type", "status", "result", "category", "desc", "description", "side", "symbol",
     "trader", "flag", "comment", "note", "title" — these stay as "string".
   - Date keywords (date, tradedate, orderdate, dob, created_at, updated_at, shipdate)
     → fabric_datatype: "dateTime", summarize_by: "none"
   - Integer keywords (year, month, day, rank, opentime, closetime, firstid, lastid)
     → fabric_datatype: "int64", summarize_by: "none" (not sum, these are IDs/periods)

3. VISUAL MAPPING — Read services/visual_mapper.py.
   - Does it map ALL of: KPI/gauge, filterpane, listbox, bargraph, linechart, piechart,
     scatterplot, table, pivot, textobject, container, button, bookmarkobject?
   - For every Qlik type it cannot map 1:1, does it produce a meaningful fallback?
   - Add mappings for any missing types.

4. FILTER MAPPING — Read services/filter_mapper.py.
   - Does it produce a PBIR-compatible slicer filter JSON for every filterpane?
   - Does it correctly reference the table and column in the Fabric semantic model?

5. DIMENSION/HIERARCHY MAPPING — Read services/dimension_mapper.py.
   - Does it emit a hierarchy block in the TMDL for every Qlik drill-down dimension?

6. DAX CONVERSION — Read services/dax_converter.py.
   - Does it handle the most common Qlik aggregation functions?
     Sum(), Count(), Avg(), Min(), Max(), If(), Aggr(), RangeSum(), Above(), Below()
   - Does it correctly output valid DAX for each?

Fix every gap you find directly in each file.

=== TASK 3: DEEP AUDIT — GENERATION STAGE ===

Read app/report/visual_builder.py and app/report/visual_catalog.py in full.

1. VISUAL TYPES — For every visual type that the mapping sends, does visual_builder.py
   produce a valid PBIR visual.json? Required types:
   - barChart, columnChart, lineChart, pieChart, scatterChart → check that Y/Values
     projections are wrapped in Aggregation { Function: 0 }  ✅ verify this is working
   - gauge → Y field is Aggregation-wrapped ✅ verify
   - card / KPI → uses a Measure field, not a raw column
   - tableEx / pivotTable → all measure columns aggregation-wrapped
   - slicerVisual → has correct slicerSettings.orientation and field binding
   - bookmarkNavigator → emitted as actionButton with bookmark reference
   - groupContainer → wraps child visuals by position

2. BOOKMARKS — Does report_writer.py emit a `bookmarks` array in report.json?
   Each bookmark must reference the set of visuals visible on that page state.

3. BUTTONS — Does the mapping produce button visuals? Does visual_builder.py emit
   `actionButton` with:
   {
     "visual": {
       "visualType": "actionButton",
       "objects": {
         "action": [{"properties": {"type": {"expr": {"Literal": {"Value": "'Bookmark'"}}}},
                     "bookmarkName": "<bookmark-id>"}]
       }
     }
   }

4. FILTERS — Does report_writer.py emit page-level `filters` in the PBIR page.json?
   Each filter must use:
   {
     "type": "TopN" or "Basic",
     "expression": {"Column": {"Expression": {"SourceRef": {"Entity": "<Table>"}},
                               "Property": "<Column>"}},
     "filterType": 1
   }

5. TMDL TYPES — Read app/model/datatypes.py.
   - Verify to_tmdl_type() emits one of: string, double, int64, dateTime, boolean, binary
   - Verify summarize_by() returns "sum" for double/int64 metric columns
   - Verify infer_type_from_name() correctly excludes text-suffix columns (result, status,
     type, name, category, side, symbol, trader, reduction) from numeric coercion

Fix every gap you find directly in each file.

=== TASK 4: NEW ENDPOINT — PUSH-FIRST GENERATE ===

Modify app/generator.py:
- Add parameter `push_only: bool` to the `generate()` function signature.
- When `push_only=True` or `deploy != Deploy.NONE`:
  - Do NOT call `pbip_packager.write_to_disk()`.
  - Call `_deploy()` immediately after building the package.
- After building the package, save it to `app/package/package_store.py`:
  - `package_store.save(run_id, package_dict)` where `package_dict` is the flat
    `{relative_path: file_content_str}` dict.

Create app/package/package_store.py:
```python
# In-process cache. Swap body for CosmosDB calls when needed.
_store: dict[str, dict[str, str]] = {}

def save(run_id: str, package: dict[str, str]) -> None:
    _store[run_id] = package

def load(run_id: str) -> dict[str, str] | None:
    return _store.get(run_id)
```

Modify app/schemas.py:
- Add to GenerateRequest: `push_only: bool = False`
- Add new model:
```python
class DownloadRequest(BaseModel):
    run_id: str
    app_id: Optional[str] = None
    app_name: Optional[str] = None
```

Create app/package/zip_builder.py:
```python
import io, zipfile
def build_zip(package: dict[str, str]) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel_path, content in package.items():
            zf.writestr(rel_path, content if isinstance(content, (str, bytes)) else str(content))
    return buf.getvalue()
```

Modify app/api/routes.py:
- Modify generate_endpoint to:
  - Pass `push_only=request.push_only` to `generate()`.
  - Always call deployment if `request.deploy != Deploy.NONE`.
  - Return response WITHOUT `output_path` when `push_only=True`.
- Add new route:
```python
from fastapi.responses import StreamingResponse
import io

@router.post("/download")
def download_pbip(request: DownloadRequest):
    package = package_store.load(request.run_id)
    if not package:
        # Re-generate from Cosmos mapping
        document = fetch_mapping(request.app_id, request.run_id)
        from app.schemas import GenerateRequest, Target, Deploy
        req = GenerateRequest(
            app_id=request.app_id,
            run_id=request.run_id,
            app_name=request.app_name,
            target=Target.POWERBI_DESKTOP,
            deploy=Deploy.NONE,
            write_to_disk=False,
            include_artifacts=False,
            offline_sample_data=False,
        )
        result = generate(document, req)
        package = package_store.load(request.run_id)
    if not package:
        raise HTTPException(status_code=404, detail="No package found for this run_id. Run /generate first.")

    zip_bytes = zip_builder.build_zip(package)
    app_name = request.app_name or request.run_id
    return StreamingResponse(
        io.BytesIO(zip_bytes),
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{app_name}.zip"'}
    )
```

=== END OF PROMPT ===
