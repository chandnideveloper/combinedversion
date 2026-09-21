# Direct Answer: How Tableau Results are Stored & Retrieved (QT2F_Tableau)

This document answers your specific question: *"Where will they be storing the data of the tableaus and how can i get the tableau result accurately like the get apis and the post apis that will works accurately"*

---

## 🎯 Where Tableau Results Are Stored

### Primary Storage Location

```
MongoDB Atlas Cluster
└─ Database: QT2F_Tableau (separate from QT2F for Qlik)
   ├─ Collection: run_history
   ├─ Collection: assessment
   ├─ Collection: parsing
   ├─ Collection: mapping
   ├─ Collection: report_generation
   ├─ Collection: validation
   ├─ Collection: agent_actions
   └─ Collection: semantic_kernel
```

**Key Point:** Each Tableau workbook assessment stores results in `QT2F_Tableau` database, separate from Qlik results in `QT2F`.

---

## 📝 What Gets Stored for Each Tableau Workbook

When you submit a Tableau workbook for assessment, these 4 documents are created:

### 1️⃣ run_history Entry
```json
{
  "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  "run_no": "R-105",
  "source_type": "tableau",                          // ← Tableau flag
  "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
  "workbook_name": "Amazon Prime Titles",
  "project_id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
  "project_name": "Finance Analytics",
  "site_id": "techcoreteam2026-50af0fff68",
  
  "assessment_status": "completed",                  // ← Phase status
  "assessment_message": "Assessment completed successfully",
  
  "parsing_status": "pending",
  "mapping_status": "pending",
  "report_generation_status": "pending",
  "validation_status": "pending",
  
  "overall_status": "running",
  
  "actual_provider": "groq",                         // ← What AI ran assessment
  "actual_model": "llama-3.3-70b-versatile",
  "model_mode": "auto",
  
  "created_at": "2026-09-01T10:00:00Z",
  "updated_at": "2026-09-01T10:01:30Z"
}
```

**Location:** `QT2F_Tableau.run_history`
**Use Case:** Track phase status and high-level progress

---

### 2️⃣ assessment Entry
```json
{
  "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
  "workbook_name": "Amazon Prime Titles",
  "project_id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
  "project_name": "Finance Analytics",
  "source_type": "tableau",                          // ← Tableau flag
  
  "assessment_result": {
    "status": "success",
    
    "complexity_score": 68,                          // ← Key scores
    "readiness_score": 78,
    "estimated_effort": "MEDIUM",
    
    "object_count": {
      "sheets": 8,
      "visualizations": 32,
      "dashboards": 4,
      "data_sources": 3,
      "calculated_fields": 12,
      "parameters": 5
    },
    
    "assessment_findings": [                         // ← What was found
      {
        "category": "visualization_compatibility",
        "severity": "MEDIUM",
        "message": "Tableau-specific visualization types need conversion",
        "affected_objects": ["Sheet: Dashboard1", "Sheet: Analytics2"],
        "recommendation": "Review custom visualization conversions"
      },
      {
        "category": "data_source_dependency",
        "severity": "LOW",
        "message": "Uses live connection - recommend extracting to Fabric",
        "affected_objects": ["Tableau Server Data Source"],
        "recommendation": "Plan for data refresh strategy in Fabric"
      }
    ],
    
    "incompatibilities": [                           // ← What won't convert directly
      "Tableau Sets require manual Power Query logic",
      "Advanced LOD (Level of Detail) expressions need DAX equivalents",
      "Tableau-specific aggregations (ATTR, RAWSQL) need rewriting"
    ],
    
    "recommendations": [                             // ← Next steps
      "Review and validate all calculated fields",
      "Plan for data refresh strategy in Fabric",
      "Test Power BI equivalents for complex vizzes"
    ]
  },
  
  "timestamp": "2026-09-01T10:01:30Z",
  "created_at": "2026-09-01T10:01:30Z"
}
```

**Location:** `QT2F_Tableau.assessment`
**Use Case:** Get assessment findings, scores, and recommendations

---

### 3️⃣ agent_actions Entries (Audit Log)
```json
[
  {
    "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
    "run_no": "R-105",
    "agent_name": "Assessment Agent",                // ← Always "Assessment Agent" for this phase
    "activity_summary": "Assessment starting for workbook",
    "status": "running",
    "action": "INFO",
    "timestamp": "2026-09-01T10:00:30Z"
  },
  {
    "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
    "run_no": "R-105",
    "agent_name": "Assessment Agent",
    "activity_summary": "Extracted 32 visualizations from Tableau",
    "status": "success",
    "action": "INFO",
    "timestamp": "2026-09-01T10:00:45Z"
  },
  {
    "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
    "run_no": "R-105",
    "agent_name": "Assessment Agent",
    "activity_summary": "Analyzed 12 calculated fields",
    "status": "success",
    "action": "INFO",
    "timestamp": "2026-09-01T10:01:00Z"
  },
  {
    "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
    "run_no": "R-105",
    "agent_name": "Assessment Agent",
    "activity_summary": "Generated assessment report",
    "status": "success",
    "action": "INFO",
    "timestamp": "2026-09-01T10:01:15Z"
  },
  {
    "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
    "run_no": "R-105",
    "agent_name": "Assessment Agent",
    "activity_summary": "Assessment completed successfully",
    "status": "success",
    "action": "INFO",
    "timestamp": "2026-09-01T10:01:30Z"
  }
]
```

**Location:** `QT2F_Tableau.agent_actions`
**Use Case:** Get step-by-step activity log and execution timeline

---

### 4️⃣ semantic_kernel Entry
```json
{
  "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  "run_no": "R-105",
  "email_id": "user@company.com",
  "status": "running",
  "overall_status": "running",
  
  "status_list": [
    {
      "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
      "project_id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
      "workbook_name": "Amazon Prime Titles",
      "project_name": "Finance Analytics",
      
      "steps": {
        "assessment": "COMPLETED",                    // ← All phase statuses
        "parsing": "PENDING",
        "mapping": "PENDING",
        "report_generation": "PENDING",
        "validation": "PENDING"
      },
      
      "final_status": "RUNNING",
      "start_date_time": "2026-09-01T10:00:00Z",
      "end_date_time": null,
      "time_elapsed": 90
    }
  ],
  
  "metadata": {
    "source_type": "tableau",                        // ← Tableau flag
    "site_id": "techcoreteam2026-50af0fff68",
    "deployment_type": "DIRECT_FABRIC",
    "fabric_group_id": "c5068f11-011c-4648-a151-231f32581819",
    "requested_model": "auto",
    "actual_model": "groq"
  },
  
  "created_at": "2026-09-01T10:00:00Z",
  "updated_at": "2026-09-01T10:01:30Z"
}
```

**Location:** `QT2F_Tableau.semantic_kernel`
**Use Case:** Get complete run metadata and current phase status

---

## 🔍 How to GET Tableau Results Accurately

### Method 1: Get Assessment Result (Main API)

**Endpoint:** `GET /api/results/assessment`

**Request:**
```bash
curl "http://localhost:8000/api/results/assessment?run_id=7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b&app_id=0d148ef0-7433-46f0-b4bc-dd52180b9ab2" \
  -H "Authorization: Bearer <TOKEN>"
```

**Response:**
```json
{
  "status": "success",
  "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  "app_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
  "data": {
    "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
    "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
    "workbook_name": "Amazon Prime Titles",
    "assessment_result": {
      "status": "success",
      "complexity_score": 68,
      "readiness_score": 78,
      "object_count": {...},
      "assessment_findings": [...],
      "incompatibilities": [...],
      "recommendations": [...]
    }
  }
}
```

✅ This is the recommended way to get assessment results.

---

### Method 2: Get Assessment Agent Actions (Audit Log)

**Endpoint:** `GET /api/results/assessment-agent-actions`

**Request:**
```bash
curl "http://localhost:8000/api/results/assessment-agent-actions?run_id=7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b&app_id=0d148ef0-7433-46f0-b4bc-dd52180b9ab2" \
  -H "Authorization: Bearer <TOKEN>"
```

**Response:**
```json
{
  "status": "success",
  "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  "app_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
  "phase": "assessment",
  "count": 5,
  "data": [
    {
      "activity_summary": "Assessment starting for workbook",
      "status": "running",
      "timestamp": "2026-09-01T10:00:30Z"
    },
    {
      "activity_summary": "Extracted 32 visualizations from Tableau",
      "status": "success",
      "timestamp": "2026-09-01T10:00:45Z"
    },
    {
      "activity_summary": "Analyzed 12 calculated fields",
      "status": "success",
      "timestamp": "2026-09-01T10:01:00Z"
    },
    {
      "activity_summary": "Generated assessment report",
      "status": "success",
      "timestamp": "2026-09-01T10:01:15Z"
    },
    {
      "activity_summary": "Assessment completed successfully",
      "status": "success",
      "timestamp": "2026-09-01T10:01:30Z"
    }
  ]
}
```

✅ Use this to see what happened at each step.

---

### Method 3: Check Phase Status

**Endpoint:** `GET /run-history`

**Request:**
```bash
curl "http://localhost:8000/run-history?email=user@company.com&run_id=7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b&project_id=c5134699-2aa2-4ab2-b201-7fcd06cf453a" \
  -H "Authorization: Bearer <TOKEN>"
```

**Response:**
```json
{
  "status": "success",
  "email": "user@company.com",
  "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  "project_id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
  "data": [
    {
      "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
      "workbook_name": "Amazon Prime Titles",
      "project_id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
      "project_name": "Finance Analytics",
      
      "assessment_status": "completed",               // ← What we care about
      "assessment_message": "Assessment completed successfully",
      
      "parsing_status": "pending",
      "mapping_status": "pending",
      "report_generation_status": "pending",
      "validation_status": "pending",
      
      "overall_status": "running",
      "updated_at": "2026-09-01T10:01:30Z"
    }
  ]
}
```

✅ Use this to know when to call the result endpoints.

---

### Method 4: Get Run Summary (All Info at Once)

**Endpoint:** `GET /api/results/run-summary`

**Request:**
```bash
curl "http://localhost:8000/api/results/run-summary?run_id=7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b" \
  -H "Authorization: Bearer <TOKEN>"
```

**Response:**
```json
{
  "status": "success",
  "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  "data": {
    "run_id": "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
    "run_no": "R-105",
    "email_id": "user@company.com",
    "overall_status": "running",
    
    "status_list": [
      {
        "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
        "workbook_name": "Amazon Prime Titles",
        "steps": {
          "assessment": "COMPLETED",
          "parsing": "PENDING",
          "mapping": "PENDING",
          "report_generation": "PENDING",
          "validation": "PENDING"
        }
      }
    ],
    
    "metadata": {
      "source_type": "tableau",
      "site_id": "techcoreteam2026-50af0fff68",
      "deployment_type": "DIRECT_FABRIC",
      "actual_model": "groq"
    },
    
    "created_at": "2026-09-01T10:00:00Z",
    "updated_at": "2026-09-01T10:01:30Z"
  }
}
```

✅ Use this for a complete overview.

---

## 📍 Database Queries (Direct MongoDB Access)

If you need to query the database directly:

### Get Assessment Result
```javascript
use QT2F_Tableau  // ← Tableau database

db.assessment.findOne({
  run_id: "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  workbook_id: "0d148ef0-7433-46f0-b4bc-dd52180b9ab2"
})
```

### Get Assessment Agent Actions
```javascript
use QT2F_Tableau

db.agent_actions.find({
  run_id: "7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b",
  agent_name: /Assessment/
}).sort({ timestamp: 1 })
```

### Get All Assessment Results for a Project
```javascript
use QT2F_Tableau

db.assessment.find({
  project_id: "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
  source_type: "tableau"
}).sort({ created_at: -1 })
```

### Get High Complexity Tableau Workbooks
```javascript
use QT2F_Tableau

db.assessment.find({
  "assessment_result.complexity_score": { $gte: 70 },
  source_type: "tableau"
}).sort({ "assessment_result.complexity_score": -1 })
```

---

## ✅ The Complete Tableau Assessment Workflow

### Step 1: Discover Tableau Workbooks
```bash
# Call Tableau Base API to get projects & workbooks
POST http://127.0.0.1:5000/get-workbooks
→ Returns: workbook_id, project_id, site_id
```

### Step 2: Submit for Assessment
```bash
# Submit to QT2F pipeline
POST http://localhost:8000/invoke-batch
{
  "source_type": "tableau",
  "items": [{
    "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
    "project_id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a"
  }]
}
→ Returns: run_id
```

### Step 3: Monitor Progress
```bash
# Check what phase we're in
GET http://localhost:8000/run-history?run_id=7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b
→ Returns: assessment_status = pending/running/completed
```

### Step 4: Get Assessment Results
```bash
# When assessment_status = "completed", get results
GET http://localhost:8000/api/results/assessment?run_id=7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b&app_id=0d148ef0-7433-46f0-b4bc-dd52180b9ab2
→ Returns: complexity_score, findings, recommendations
```

### Step 5: Get Agent Actions (What Happened)
```bash
# See what the agent did at each step
GET http://localhost:8000/api/results/assessment-agent-actions?run_id=7a2f8e9c-1b3d-5e4f-9a2b-8c1d7f3e5a6b&app_id=0d148ef0-7433-46f0-b4bc-dd52180b9ab2
→ Returns: Step-by-step activity log with timestamps
```

---

## 🔄 Field Mappings: Qlik ↔ Tableau

| Concept | Qlik Field | Tableau Field | Stored As |
|---------|-----------|---------------|-----------|
| Workspace | workspace_id | workspace_id | workspace_id |
| Container | space_id | project_id | Both stored |
| Item ID | app_id | workbook_id | Both stored |
| Item Name | app_name | workbook_name | Both stored |
| Site | (N/A) | site_id | site_id |
| Database | QT2F | QT2F_Tableau | Separate DBs |

**Important:** Every document in `QT2F_Tableau` has BOTH `workbook_id` AND `app_id` fields for compatibility.

---

## 🎯 Summary: How to Get Tableau Results

| What You Want | API Endpoint | Query Parameter | Returns |
|---------------|-------------|-----------------|---------|
| Assessment scores & findings | GET /api/results/assessment | run_id, app_id | complexity_score, readiness_score, findings |
| What agent did | GET /api/results/assessment-agent-actions | run_id, app_id | Step-by-step activity log |
| Current phase status | GET /run-history | run_id, email, project_id | assessment_status: pending/running/completed |
| Everything at once | GET /api/results/run-summary | run_id | Complete run metadata |
| Raw data (MongoDB) | Direct query | - | QT2F_Tableau database |

---

## 📊 Data Storage Locations Reference

```
Tableau Assessment Data Storage Map
═══════════════════════════════════

MongoDB Atlas
└─ Database: QT2F_Tableau
   │
   ├─ Collection: run_history
   │  └─ workbook_id, workbook_name, project_id
   │     assessment_status (pending/running/completed)
   │     actual_model (what AI was used)
   │
   ├─ Collection: assessment
   │  └─ workbook_id, workbook_name
   │     assessment_result:
   │       - complexity_score
   │       - readiness_score
   │       - assessment_findings
   │       - incompatibilities
   │       - recommendations
   │
   ├─ Collection: agent_actions
   │  └─ run_id, agent_name (Assessment Agent)
   │     activity_summary (what happened at each step)
   │     timestamp (when it happened)
   │
   └─ Collection: semantic_kernel
      └─ run_id, workbook_id
         steps.assessment (COMPLETED/PENDING/FAILED)
         metadata (source_type: tableau, site_id, etc.)
```

---

✅ **Everything is ready.** Use the APIs above to get your Tableau assessment results accurately.

