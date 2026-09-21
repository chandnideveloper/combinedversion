# Complete QT2F Result Retrieval & Storage Guide

## 🎯 Quick Reference

This guide shows you exactly how to:
1. Submit a migration pipeline for assessment/parsing/mapping
2. Track the run status in real-time
3. Retrieve assessment results and agent actions
4. Access all phase results (parsing, mapping, report generation)

All data is stored in MongoDB with proper Qlik/Tableau separation.

---

## 📊 Database Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  Semantic Kernel Orchestrator               │
│                      (:8000)                                │
└─────────────────────────────────────────────────────────────┘
                          │
                          ↓
┌─────────────────────────────────────────────────────────────┐
│              MongoDB Atlas Cluster                          │
│                                                             │
│  ┌──────────────────┐        ┌──────────────────┐          │
│  │  QT2F (Qlik)     │        │ QT2F_Tableau     │          │
│  │  ─────────────   │        │  ────────────    │          │
│  │  run_history     │        │  run_history     │          │
│  │  assessment      │        │  assessment      │          │
│  │  parsing         │        │  parsing         │          │
│  │  mapping         │        │  mapping         │          │
│  │  report_gen...   │        │  report_gen...   │          │
│  │  agent_actions   │        │  agent_actions   │          │
│  │  semantic_kernel │        │  semantic_kernel │          │
│  └──────────────────┘        └──────────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Complete Workflow — Qlik Example

### Step 1: Start Assessment Pipeline

```http
POST http://localhost:8000/invoke-batch
Content-Type: application/json
Authorization: Bearer <USER_TOKEN>

{
  "email": "user@company.com",
  "source_type": "qlik",
  "deployment_type": "DIRECT_FABRIC",
  "department_repo": "Qlik_Migrated",
  "fabric_group_id": "c5068f11-011c-4648-a151-231f32581819",
  "model": "auto",
  "run_validation": false,
  "items": [
    {
      "workspace_id": "personal",
      "workspace_name": "Personal Space",
      "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
      "app_name": "Executive Sales Analytics"
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Qlik batch processing queued successfully for 1 item(s).",
  "run_no": "R-101",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "items_queued": 1,
  "source_type": "qlik"
}
```

**Key data to save:**
- `run_id` → Use this to query all results
- `run_no` → Human-readable reference
- `source_type` → Always "qlik" or "tableau"

---

### Step 2: Get Pipeline Status

```http
GET http://localhost:8000/run-history?email=user@company.com&run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&project_id=personal
Authorization: Bearer <USER_TOKEN>
```

**Response:**
```json
{
  "status": "success",
  "email": "user@company.com",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "project_id": "personal",
  "data": [
    {
      "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
      "app_name": "Executive Sales Analytics",
      "workspace_id": "personal",
      "assessment_status": "completed",
      "assessment_message": "Assessment completed successfully",
      "parsing_status": "completed",
      "parsing_message": "Parsing completed successfully",
      "mapping_status": "in_progress",
      "report_generation_status": "pending",
      "validation_status": "pending",
      "overall_status": "running",
      "updated_at": "2026-09-01T10:05:00Z"
    }
  ]
}
```

---

### Step 3: Get Assessment Result (Phase-specific)

```http
GET http://localhost:8000/api/results/assessment?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=05796d2f-579b-4539-9b56-3ebd0b266115
Authorization: Bearer <USER_TOKEN>
```

**Response:**
```json
{
  "status": "success",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
  "data": {
    "id": "uuid",
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
    "app_name": "Executive Sales Analytics",
    "workspace_id": "personal",
    "assessment_result": {
      "status": "success",
      "complexity_score": 75,
      "readiness_score": 85,
      "estimated_effort": "MEDIUM",
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
          "severity": "MEDIUM",
          "message": "Uses Qlik-specific features not directly supported in Power BI",
          "affected_objects": ["Sheet1", "Sheet3"]
        }
      ],
      "incompatibilities": [
        "Qlik Set Analysis requires manual conversion to DAX",
        "Advanced aggregation functions need USERELATIONSHIP"
      ],
      "recommendations": [
        "Review Set Analysis expressions manually",
        "Validate hierarchical structures in Fabric"
      ]
    },
    "timestamp": "2026-09-01T10:00:30Z"
  }
}
```

**What this tells you:**
- ✅ Complexity Score: 75/100 → Moderately complex
- ✅ Readiness Score: 85/100 → Well-structured for migration
- ✅ Specific incompatibilities listed → Plan manual work
- ✅ Object counts → Validate completeness

---

### Step 4: Get Assessment Agent Actions (Audit Log)

```http
GET http://localhost:8000/api/results/assessment-agent-actions?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=05796d2f-579b-4539-9b56-3ebd0b266115
Authorization: Bearer <USER_TOKEN>
```

**Response:**
```json
{
  "status": "success",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
  "count": 5,
  "phase": "assessment",
  "data": [
    {
      "id": "action-id-1",
      "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
      "run_no": "R-101",
      "agent_name": "Assessment Agent",
      "activity_summary": "Assessment started for app_id",
      "status": "running",
      "action": "INFO",
      "message": "Initiating assessment for Executive Sales Analytics",
      "details": {
        "phase": "assessment",
        "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
        "start_time": "2026-09-01T10:00:30Z"
      },
      "timestamp": "2026-09-01T10:00:30Z"
    },
    {
      "id": "action-id-2",
      "agent_name": "Assessment Agent",
      "activity_summary": "Extracted 45 visualizations",
      "status": "success",
      "action": "INFO",
      "timestamp": "2026-09-01T10:00:45Z"
    },
    {
      "id": "action-id-3",
      "agent_name": "Assessment Agent",
      "activity_summary": "Analyzed 23 calculations",
      "status": "success",
      "action": "INFO",
      "timestamp": "2026-09-01T10:01:00Z"
    },
    {
      "id": "action-id-4",
      "agent_name": "Assessment Agent",
      "activity_summary": "Generated assessment report",
      "status": "success",
      "action": "INFO",
      "timestamp": "2026-09-01T10:01:15Z"
    },
    {
      "id": "action-id-5",
      "agent_name": "Assessment Agent",
      "activity_summary": "Assessment completed for app_id",
      "status": "success",
      "action": "INFO",
      "timestamp": "2026-09-01T10:01:30Z"
    }
  ]
}
```

**What this tells you:**
- ✅ Complete execution timeline
- ✅ Each step and its status (success/error)
- ✅ Performance: took ~60 seconds total
- ✅ What was analyzed (visualizations, calculations)

---

### Step 5: Get Parsing Result (Once Available)

```http
GET http://localhost:8000/api/results/parsing?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=05796d2f-579b-4539-9b56-3ebd0b266115
Authorization: Bearer <USER_TOKEN>
```

**Response:**
```json
{
  "status": "success",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
  "data": {
    "id": "uuid",
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
    "app_name": "Executive Sales Analytics",
    "workspace_id": "personal",
    "parsing_result": {
      "status": "success",
      "source_type": "qlik",
      "metadata": {
        "data_sources": [
          {
            "name": "Sales Data Connection",
            "type": "SQL",
            "connection_string": "***REDACTED***",
            "tables": ["FactSales", "DimDate", "DimProduct"]
          }
        ],
        "sheets": [
          {
            "id": "sheet-1",
            "name": "Overview",
            "visualizations": [
              {
                "id": "viz-1",
                "title": "Sales by Region",
                "type": "bar",
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
            "type": "measure",
            "data_type": "numeric"
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
    "timestamp": "2026-09-01T10:02:00Z"
  }
}
```

---

### Step 6: Get ALL Phase Results at Once

```http
GET http://localhost:8000/api/results/all-phases?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=05796d2f-579b-4539-9b56-3ebd0b266115
Authorization: Bearer <USER_TOKEN>
```

**Response:**
```json
{
  "status": "success",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
  "data": {
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
    "assessment": {
      "assessment_result": { ... }
    },
    "parsing": {
      "parsing_result": { ... }
    },
    "mapping": {
      "mapping_result": { ... }
    },
    "report_generation": {
      "generation_result": { ... }
    },
    "validation": null  // Not yet available
  }
}
```

---

### Step 7: Get Run Summary (Complete Status)

```http
GET http://localhost:8000/api/results/run-summary?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5
Authorization: Bearer <USER_TOKEN>
```

**Response:**
```json
{
  "status": "success",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "data": {
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "run_no": "R-101",
    "email_id": "user@company.com",
    "status": "running",
    "overall_status": "running",
    "items_count": 1,
    "items_completed": 0,
    "items_failed": 0,
    "status_list": [
      {
        "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
        "workspace_id": "personal",
        "app_name": "Executive Sales Analytics",
        "workspace_name": "Personal Space",
        "steps": {
          "assessment": "COMPLETED",
          "parsing": "COMPLETED",
          "mapping": "RUNNING",
          "report_generation": "PENDING",
          "validation": "PENDING"
        },
        "final_status": "RUNNING",
        "start_date_time": "2026-09-01T10:00:00Z",
        "end_date_time": null,
        "time_duration": null,
        "time_elapsed": 300
      }
    ],
    "metadata": {
      "workspace_type": "single space",
      "app_type": "single app",
      "source_type": "qlik",
      "deployment_type": "DIRECT_FABRIC",
      "execution_level": "app",
      "model_mode": "auto",
      "requested_model": "groq",
      "actual_model": "groq",
      "fabric_group_id": "c5068f11-011c-4648-a151-231f32581819"
    },
    "start_date_time": "2026-09-01T10:00:00Z",
    "end_date_time": null,
    "created_at": "2026-09-01T10:00:00Z",
    "updated_at": "2026-09-01T10:05:00Z"
  }
}
```

---

## 📊 Complete Workflow — Tableau Example

### Step 1: Discover Tableau Workbooks

```http
POST http://127.0.0.1:5000/propagate-tableau-details
Content-Type: application/json

{
  "TABLEAU_SERVER_URL": "https://prod-useast-a.online.tableau.com",
  "TABLEAU_SITE_NAME": "techcoreteam2026-50af0fff68",
  "TABLEAU_TOKEN_NAME": "MigrationToken",
  "TABLEAU_TOKEN_VALUE": "YOUR_PAT_TOKEN_SECRET"
}
```

**Response:**
```json
{
  "projects": [
    {
      "id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
      "name": "Finance Analytics"
    }
  ]
}
```

### Step 2: Get Workbooks for Project

```http
POST http://127.0.0.1:5000/get-workbooks
Content-Type: application/json

{
  "TABLEAU_SERVER_URL": "https://prod-useast-a.online.tableau.com",
  "TABLEAU_SITE_NAME": "techcoreteam2026-50af0fff68",
  "TABLEAU_TOKEN_NAME": "MigrationToken",
  "TABLEAU_TOKEN_VALUE": "YOUR_PAT_TOKEN_SECRET",
  "PROJECT_ID": ["c5134699-2aa2-4ab2-b201-7fcd06cf453a"]
}
```

**Response:**
```json
{
  "workbooks": [
    {
      "id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
      "name": "Amazon Prime Titles"
    }
  ]
}
```

### Step 3: Start Assessment Pipeline

```http
POST http://localhost:8000/invoke-batch
Content-Type: application/json
Authorization: Bearer <USER_TOKEN>

{
  "email": "user@company.com",
  "source_type": "tableau",
  "deployment_type": "DIRECT_FABRIC",
  "department_repo": "Tableau_Migrated",
  "fabric_group_id": "c5068f11-011c-4648-a151-231f32581819",
  "site_id": "techcoreteam2026-50af0fff68",
  "model": "auto",
  "run_validation": false,
  "items": [
    {
      "project_id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
      "project_name": "Finance Analytics",
      "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
      "workbook_name": "Amazon Prime Titles"
    }
  ]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Tableau batch processing queued successfully for 1 item(s).",
  "run_no": "R-102",
  "run_id": "a7b5c2d1-8f2e-4a6c-9b3d-7e1f5c2a4d9f",
  "items_queued": 1,
  "source_type": "tableau"
}
```

### Step 4-7: Same as Qlik (Use Same Endpoints)

All the retrieval endpoints work identically for Tableau. Just use the returned `run_id` and `workbook_id` instead of `app_id`.

---

## 🔍 Query Patterns for Common Tasks

### Find Assessment Results by App

```javascript
// MongoDB Query
db.assessment.find({
  run_id: "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  app_id: "05796d2f-579b-4539-9b56-3ebd0b266115"
})
```

### Get All Agent Actions for Assessment Phase

```javascript
// MongoDB Query
db.agent_actions.find({
  run_id: "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  agent_name: /Assessment/i
}).sort({ timestamp: 1 })
```

### Find Failed Runs

```javascript
// MongoDB Query
db.semantic_kernel.find({
  overall_status: "failed"
}).sort({ created_at: -1 })
```

### Get High Complexity Apps

```javascript
// MongoDB Query
db.assessment.find({
  "assessment_result.complexity_score": { $gte: 80 }
}).sort({ "assessment_result.complexity_score": -1 })
```

---

## 📝 Platform Field Mappings

| Concept | Qlik | Tableau |
|---------|------|---------|
| Container | `workspace_id` (space_id) | `workspace_id` (project_id) |
| Item | `app_id` | `workbook_id` |
| Item Name | `app_name` | `workbook_name` |
| Container Name | `workspace_name` | `project_name` |
| Database | QT2F | QT2F_Tableau |
| Source Type | "qlik" | "tableau" |

---

## ✅ Checklist for Using the API

- [ ] Get `run_id` from `/invoke-batch` response
- [ ] Poll `/run-history` to check phase status
- [ ] When assessment completes, call `/api/results/assessment`
- [ ] Review assessment findings and recommendations
- [ ] Call `/api/results/assessment-agent-actions` for detailed logs
- [ ] Once parsing completes, get `/api/results/parsing`
- [ ] Once all phases complete, call `/api/results/all-phases` for full results
- [ ] Call `/api/results/run-summary` for final metrics

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Assessment result returns `not_found` | Check the `run_id` and `app_id` match exactly. Assessment may still be running. |
| Agent actions show ERROR status | Review the `activity_summary` and `details` fields for the specific error message |
| Mapping or generation missing | These phases run after parsing. They may not have started yet. Check run status first. |
| Database query returns empty | Verify you're querying the correct database (QT2F for Qlik, QT2F_Tableau for Tableau) |

---

## 🚀 Performance Notes

- Assessment typically takes 1-5 minutes per app
- Parsing typically takes 2-10 minutes per app
- Mapping typically takes 3-15 minutes per app
- Full run can take 30+ minutes for complex apps

Poll status with 30-second intervals for live updates.

---
