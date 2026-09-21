# QT2F Database Schema — Tableau & Qlik Result Storage

## 📋 Overview

Two separate MongoDB databases store Qlik and Tableau migration results:
- **QT2F** → Qlik Cloud migration results
- **QT2F_Tableau** → Tableau Cloud migration results

Both follow the same collection structure, with platform-specific field mappings where needed.

---

## 🏗️ Database Collections

### 1. **run_history** (Status tracking across all phases)

**Purpose**: Track pipeline phase status for each workbook/app per run.

**Collection Name**: `run_history`

**Document Schema**:
```json
{
  "_id": ObjectId,
  "run_id": "uuid",                          // Unique run identifier
  "run_no": "R-101",                         // Human-readable run number
  "email_id": "user@company.com",            // User who initiated the run
  "user_email": "user@company.com",          // Same as email_id
  
  // Platform-specific identifiers
  "source_type": "qlik" | "tableau",         // Source platform
  "workspace_id": "uuid",                    // Qlik space_id OR Tableau project_id
  "project_id": "uuid",                      // (Tableau) project_id
  "space_id": "uuid",                        // (Qlik) space_id
  "workspace_name": "Personal Space",        // Display name
  "project_name": "Finance Analytics",       // (Tableau only)
  
  "app_id": "uuid",                          // Qlik app_id
  "workbook_id": "uuid",                     // (Tableau) workbook_id
  "app_name": "Executive Dashboard",         // Qlik app name
  "workbook_name": "Amazon Prime Titles",    // (Tableau) workbook name
  
  // Phase Status
  "assessment_status": "pending|running|completed|failed|skipped",
  "assessment_message": "Assessment completed successfully",
  "assessment_error": "null",
  
  "parsing_status": "pending|running|completed|failed|skipped",
  "parsing_message": "Parsing completed successfully",
  "parsing_error": "null",
  
  "mapping_status": "pending|running|completed|failed|skipped",
  "mapping_message": "Mapping completed successfully",
  "mapping_error": "null",
  
  "report_generation_status": "pending|running|completed|failed|skipped",
  "report_generation_message": "Report generation completed",
  "report_generation_error": "null",
  
  "validation_status": "pending|running|completed|failed|skipped",
  "validation_message": "Validation passed",
  "validation_error": "null",
  
  // Overall Status
  "overall_status": "pending|running|completed|failed",
  "error_message": "null",
  "status_message": "Pipeline execution in progress",
  
  // Model tracking (never persist API keys)
  "actual_provider": "groq",                 // Which AI provider was used
  "actual_model": "llama-3.3-70b-versatile", // Which model was used
  "model_mode": "auto|manual",               // How model was selected
  
  // Timestamps
  "created_at": ISODate("2026-09-01T10:00:00Z"),
  "updated_at": ISODate("2026-09-01T10:05:00Z"),
  "started_at": ISODate("2026-09-01T10:00:30Z"),
  "completed_at": ISODate("2026-09-01T10:05:00Z"),
  
  // Fabric/deployment info
  "fabric_group_id": "workspace-guid",
  "lakehouse_id": "lakehouse-guid",
  "department_repo": "Qlik_Migrated"
}
```

**Indexes**:
```javascript
db.run_history.createIndex({ run_id: 1, workspace_id: 1, app_id: 1 })
db.run_history.createIndex({ run_id: 1 })
db.run_history.createIndex({ email_id: 1, run_id: 1 })
db.run_history.createIndex({ source_type: 1, workbook_id: 1 })
db.run_history.createIndex({ updated_at: -1 })
```

---

### 2. **assessment** (Assessment phase results)

**Purpose**: Store detailed assessment findings for each workbook/app.

**Collection Name**: `assessment`

**Document Schema**:
```json
{
  "_id": ObjectId,
  "id": "uuid",
  "run_id": "uuid",
  
  // Platform mapping
  "source_type": "qlik|tableau",
  "app_id": "uuid",                          // Qlik app_id
  "workbook_id": "uuid",                     // (Tableau) workbook_id
  "workspace_id": "uuid",                    // Qlik space_id OR Tableau project_id
  "project_id": "uuid",                      // (Tableau) project_id
  "space_id": "uuid",                        // (Qlik) space_id
  "app_name": "app name",
  "workbook_name": "workbook name",
  "folder_name": "folder name",
  
  // Assessment result
  "assessment_result": {
    "status": "success",
    "complexity_score": 75,                   // 0-100
    "readiness_score": 85,                    // 0-100
    "estimated_effort": "HIGH|MEDIUM|LOW",
    "object_count": {
      "sheets": 12,
      "visualizations": 45,
      "tables": 8,
      "calculations": 23,
      "measures": 45,
      "dimensions": 12
    },
    "assessment_findings": [
      {
        "category": "visualization_type",
        "severity": "HIGH|MEDIUM|LOW",
        "message": "Contains advanced Tableau viz type not directly supported",
        "affected_objects": ["Sheet1", "Sheet2"]
      }
    ],
    "incompatibilities": [
      "Feature X not available in Power BI",
      "Formula pattern Y requires manual conversion"
    ],
    "recommendations": [
      "Consider splitting this workbook into 2 semantic models",
      "Validate hierarchical dimensions in Fabric"
    ],
    "metadata": {
      "total_sheets": 12,
      "total_visualizations": 45,
      "formula_count": 23,
      "data_sources": 3
    }
  },
  
  "timestamp": ISODate("2026-09-01T10:00:00Z"),
  "created_at": ISODate("2026-09-01T10:00:00Z"),
  "updated_at": ISODate("2026-09-01T10:00:00Z")
}
```

**Indexes**:
```javascript
db.assessment.createIndex({ run_id: 1, app_id: 1 })
db.assessment.createIndex({ run_id: 1, workbook_id: 1 })
db.assessment.createIndex({ source_type: 1 })
```

---

### 3. **parsing** (Parsing phase results)

**Purpose**: Store extracted metadata from Qlik or unpacked Tableau workbooks.

**Collection Name**: `parsing`

**Document Schema**:
```json
{
  "_id": ObjectId,
  "id": "uuid",
  "run_id": "uuid",
  
  // Platform mapping
  "source_type": "qlik|tableau",
  "app_id": "uuid",
  "workbook_id": "uuid",
  "workspace_id": "uuid",
  "project_id": "uuid",
  "app_name": "app name",
  "workbook_name": "workbook name",
  "folder_name": "folder name",
  
  // Parsing result (Qlik or Tableau metadata)
  "parsing_result": {
    "status": "success",
    "source_type": "qlik|tableau",
    "metadata": {
      "data_sources": [
        {
          "name": "Data Connection 1",
          "type": "SQL|REST|Excel",
          "connection_string": "***",           // Sanitized
          "tables": ["table1", "table2"]
        }
      ],
      "sheets": [
        {
          "id": "sheet-1",
          "name": "Dashboard",
          "visualizations": [
            {
              "id": "viz-1",
              "title": "Sales by Region",
              "type": "bar|line|scatter",
              "expressions": ["Sum(Sales)", "Avg(Quantity)"],
              "dimensions": ["Region", "Product"]
            }
          ]
        }
      ],
      "calculations": [
        {
          "id": "calc-1",
          "name": "Total Sales",
          "expression": "[Sales] + [Other Charges]",
          "type": "measure|dimension",
          "data_type": "numeric|string|date"
        }
      ],
      "model": {
        "tables": [...],
        "relationships": [...]
      }
    },
    "parsing_errors": [],
    "parsing_warnings": []
  },
  
  "timestamp": ISODate("2026-09-01T10:00:00Z"),
  "created_at": ISODate("2026-09-01T10:00:00Z"),
  "updated_at": ISODate("2026-09-01T10:00:00Z")
}
```

**Indexes**:
```javascript
db.parsing.createIndex({ run_id: 1, app_id: 1 })
db.parsing.createIndex({ run_id: 1, workbook_id: 1 })
```

---

### 4. **mapping** (Mapping phase results)

**Purpose**: Store Contract 2.0 mapped results (tables, measures, visuals).

**Collection Name**: `mapping`

**Document Schema**:
```json
{
  "_id": ObjectId,
  "id": "uuid",
  "run_id": "uuid",
  
  "source_type": "qlik|tableau",
  "app_id": "uuid",
  "workbook_id": "uuid",
  "workspace_id": "uuid",
  "app_name": "app name",
  "workbook_name": "workbook name",
  
  "mapping_result": {
    "status": "success",
    "contract_version": "2.0",
    "tables": [
      {
        "id": "table-1",
        "name": "DimDate",
        "source_table": "Date Dimension",
        "column_count": 10,
        "columns": [...]
      }
    ],
    "measures": [
      {
        "id": "measure-1",
        "name": "Total Sales",
        "dax_expression": "SUM(FactSales[Amount])",
        "source_expression": "Sum(Sales)",
        "conversion_status": "success|partial|failed"
      }
    ],
    "visualizations": [
      {
        "id": "visual-1",
        "name": "Sales Chart",
        "type": "column_chart|line_chart",
        "mapped_fields": ["DimDate[Date]", "Measures[Total Sales]"]
      }
    ],
    "mapping_errors": [],
    "unmapped_objects": []
  },
  
  "timestamp": ISODate("2026-09-01T10:00:00Z"),
  "created_at": ISODate("2026-09-01T10:00:00Z"),
  "updated_at": ISODate("2026-09-01T10:00:00Z")
}
```

---

### 5. **report_generation** (Report generation phase results)

**Purpose**: Store generated PBIP, TMDL, and PBIR artifacts.

**Collection Name**: `report_generation`

**Document Schema**:
```json
{
  "_id": ObjectId,
  "id": "uuid",
  "run_id": "uuid",
  
  "source_type": "qlik|tableau",
  "app_id": "uuid",
  "workbook_id": "uuid",
  "app_name": "app name",
  "workbook_name": "workbook name",
  
  "generation_result": {
    "status": "success",
    "pbip_file_path": "s3://bucket/runs/run-id/Report.pbip",
    "pbip_size_bytes": 2560000,
    "tmdl_model": { ... },
    "pbir_visual_tree": { ... },
    "dataset_size_mb": 250,
    "deployment_target": "Fabric Workspace GUID",
    "deployment_status": "ready|deployed|failed"
  },
  
  "timestamp": ISODate("2026-09-01T10:00:00Z"),
  "created_at": ISODate("2026-09-01T10:00:00Z"),
  "updated_at": ISODate("2026-09-01T10:00:00Z")
}
```

---

### 6. **semantic_kernel** (Aggregate run record)

**Purpose**: High-level run orchestration record with overall status.

**Collection Name**: `semantic_kernel`

**Document Schema**:
```json
{
  "_id": ObjectId,
  "run_id": "uuid",
  "run_no": "R-101",
  "email_id": "user@company.com",
  
  "status": "pending|running|completed|failed",
  "overall_status": "pending|running|completed|failed",
  
  "items_count": 1,
  "items_completed": 0,
  "items_failed": 0,
  
  "status_list": [
    {
      "app_id": "uuid",
      "workspace_id": "uuid",
      "app_name": "Executive Dashboard",
      "workspace_name": "Personal Space",
      "steps": {
        "assessment": "PENDING|RUNNING|COMPLETED|FAILED",
        "parsing": "PENDING|RUNNING|COMPLETED|FAILED",
        "mapping": "PENDING|RUNNING|COMPLETED|FAILED",
        "report_generation": "PENDING|RUNNING|COMPLETED|FAILED",
        "validation": "PENDING|RUNNING|COMPLETED|FAILED"
      },
      "final_status": "PENDING|RUNNING|COMPLETED|FAILED",
      "error": "error message if failed",
      "start_date_time": ISODate("2026-09-01T10:00:00Z"),
      "end_date_time": ISODate("2026-09-01T10:05:00Z"),
      "time_duration": "5 minutes",
      "time_elapsed": 300
    }
  ],
  
  "log_lines": ["log entry 1", "log entry 2"],
  
  "metadata": {
    "workspace_type": "single space|multiple spaces",
    "app_type": "single app|multiple apps",
    "source_type": "qlik|tableau",
    "deployment_type": "DIRECT_FABRIC|GIT",
    "execution_level": "app|space|project",
    "model_mode": "auto|manual",
    "requested_model": "groq",
    "actual_model": "groq",
    "fabric_group_id": "guid"
  },
  
  "start_date_time": ISODate("2026-09-01T10:00:00Z"),
  "end_date_time": ISODate("2026-09-01T10:05:00Z"),
  
  "created_at": ISODate("2026-09-01T10:00:00Z"),
  "updated_at": ISODate("2026-09-01T10:05:00Z")
}
```

---

### 7. **agent_actions** (Agent activity log)

**Purpose**: Detailed activity trace from each agent (Assessment, Parsing, Mapping, etc.)

**Collection Name**: `agent_actions`

**Document Schema**:
```json
{
  "_id": ObjectId,
  "id": "uuid",
  
  // Trace back to run
  "run_id": "uuid",
  "run_no": "R-101",
  "correlation_id": "correlation-id or run-id",
  
  // Platform
  "source_type": "qlik|tableau",
  "workspace_id": "uuid",
  "project_id": "uuid",
  "project_name": "Finance Analytics",
  "app_id": "uuid",
  "workbook_id": "uuid",
  "folder_name": "folder name",
  
  // User
  "email_id": "user@company.com",
  "user_email": "user@company.com",
  
  // Agent that performed the action
  "agent_name": "Assessment Agent|Parsing Agent|Mapping Agent|Report Generation Agent|Validation Agent",
  
  // Activity details
  "activity_summary": "Assessment started for app_id",
  "status": "running|success|failed",
  "action": "INFO|WARNING|ERROR",
  "log_level": "INFO|WARNING|ERROR",
  "message": "Assessment completed with 45 visualizations found",
  "details": {
    // agent-specific details
    "phase": "assessment|parsing|mapping|report_generation|validation",
    "duration_ms": 5000,
    "objects_processed": 45,
    "errors_encountered": []
  },
  
  // Payload (optional agent response)
  "payload": {
    // agent-specific response data
  },
  
  "type": "agent_activity",
  "timestamp": ISODate("2026-09-01T10:00:30Z"),
  "created_at": ISODate("2026-09-01T10:00:30Z")
}
```

**Indexes**:
```javascript
db.agent_actions.createIndex({ run_id: 1 })
db.agent_actions.createIndex({ run_id: 1, timestamp: -1 })
db.agent_actions.createIndex({ agent_name: 1, timestamp: -1 })
db.agent_actions.createIndex({ app_id: 1, source_type: 1 })
```

---

## 🗺️ Platform Field Mapping

| Concept | Qlik (QT2F) | Tableau (QT2F_Tableau) |
|---------|-----------|----------------------|
| Container | `workspace_id` + `space_id` | `workspace_id` + `project_id` |
| Item | `app_id` | `workbook_id` |
| Item Name | `app_name` | `workbook_name` |
| Container Name | `workspace_name` | `project_name` |
| Source Type | `"qlik"` | `"tableau"` |

---

## 🔄 Query Patterns

### Get Assessment Result
```javascript
db.assessment.findOne({
  run_id: "uuid",
  app_id: "uuid"  // or workbook_id for Tableau
})
```

### Get All Agent Actions for a Run
```javascript
db.agent_actions.find({
  run_id: "uuid"
}).sort({ timestamp: 1 })
```

### Get Assessment Agent Actions Only
```javascript
db.agent_actions.find({
  run_id: "uuid",
  agent_name: /assessment/i
}).sort({ timestamp: 1 })
```

### Get Phase Status
```javascript
db.run_history.findOne({
  run_id: "uuid",
  app_id: "uuid"
})
// Returns: assessment_status, parsing_status, mapping_status, etc.
```

---

## 📝 Save Pattern

When saving results from Assessment/Parsing/Mapping agents:

1. **Source Database**: Determine if Qlik or Tableau from request
2. **Save to QT2F** (default): Always save to the main orchestration DB
3. **Save to source-specific DB**:
   - If Qlik: Also save to `QT2F`
   - If Tableau: Also save to `QT2F_Tableau`

Example:
```python
async def save_assessment_record(
    run_id: str,
    app_id: str,
    workspace_id: str,
    app_name: str,
    assessment_result: Dict[str, Any],
    source_type: str = "qlik"  # NEW: add this parameter
):
    doc = {
        "run_id": run_id,
        "app_id": app_id or workbook_id,
        "workspace_id": workspace_id or project_id,
        "source_type": source_type,
        "assessment_result": assessment_result,
        "timestamp": _utcnow(),
    }
    
    # Save to default DB
    await db["assessment"].update_one(
        {"run_id": run_id, "app_id": app_id},
        {"$set": doc},
        upsert=True
    )
    
    # Also save to source-specific DB
    if source_type == "tableau":
        client = AsyncIOMotorClient(settings.MONGO_URI)
        target_db = client["QT2F_Tableau"]
        await target_db["assessment"].update_one(
            {"run_id": run_id, "workbook_id": app_id},
            {"$set": doc},
            upsert=True
        )
```

---

## 🎯 Key Points

✅ **One run_id** identifies a complete pipeline execution
✅ **One document per app/workbook** in each result collection
✅ **Platform-agnostic API** returns both Qlik and Tableau results
✅ **Dual-database storage** for isolation and querying by platform
✅ **Timestamp tracking** for audit and recovery
✅ **Never store API keys** in run_history or agent_actions
✅ **Comprehensive error tracking** in each phase

---
