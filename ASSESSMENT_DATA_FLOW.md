# Assessment & Result Data Flow — Technical Deep Dive

## 🔄 Complete Data Journey: Assessment → Storage → Retrieval

This document traces exactly how assessment data flows through the system for both Qlik and Tableau.

---

## 📍 Phase 1: Assessment Request Initiated

### Entry Point: `/invoke-batch`

```
Client sends POST /invoke-batch
    ↓
Semantic Kernel receives request
    ↓
Extract source_type ("qlik" or "tableau")
    ↓
Generate run_id (UUID) and run_no (R-xxx)
    ↓
Create initial run_history record with status="pending"
    ↓
Queue background task for processing
    ↓
Return run_id to client (202 Accepted)
```

### What's stored at this point (QT2F or QT2F_Tableau):

**Collection: run_history**
```json
{
  "_id": ObjectId,
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "run_no": "R-101",
  "email_id": "user@company.com",
  "source_type": "qlik",
  "workspace_id": "personal",
  "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
  "app_name": "Executive Sales Analytics",
  "assessment_status": "pending",
  "assessment_message": null,
  "parsing_status": "pending",
  "mapping_status": "pending",
  "report_generation_status": "pending",
  "validation_status": "pending",
  "overall_status": "pending",
  "created_at": ISODate("2026-09-01T10:00:00Z"),
  "updated_at": ISODate("2026-09-01T10:00:00Z")
}
```

---

## 📍 Phase 2: Assessment Agent Starts

### Location: `plugins/queue_handler.py` → `run_assessment()` coroutine

```
Background task starts
    ↓
Mark assessment_status = "running" in run_history
    ↓
Log agent action: "Assessment starting"
    ↓
Call Assessment Agent API (POST /assessment or POST /start-assessment)
    │
    └─→ Assessment Agent receives:
        {
          "source_type": "qlik",
          "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
          "workspace_id": "personal",
          "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
          "app_name": "Executive Sales Analytics",
          "model_provider": "groq",
          "model_name": "llama-3.3-70b-versatile",
          ...
        }
    ↓
Wait for response
```

### Agent Actions logged (agent_actions collection):

```json
{
  "_id": ObjectId,
  "id": "action-1",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "run_no": "R-101",
  "agent_name": "Assessment Agent",
  "activity_summary": "Assessment starting for app_id",
  "status": "running",
  "timestamp": ISODate("2026-09-01T10:00:30Z"),
  "details": {
    "phase": "assessment",
    "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115"
  }
}
```

---

## 📍 Phase 3: Assessment Agent Executes

### Inside Assessment Agent (separate service)

```
Receive request for Qlik app
    ↓
Connect to Qlik Engine API
    ↓
Extract metadata:
  - Sheets (12)
  - Visualizations (45)
  - Calculations (23)
  - Data sources (3)
    ↓
Analyze each visualization:
  - Chart type
  - Dimensions & measures
  - Complex expressions
    ↓
Run compatibility checks:
  - Set Analysis usage?
  - Native Qlik functions?
  - Advanced aggregations?
    ↓
Calculate scores:
  - Complexity: 1-100
  - Readiness: 1-100
    ↓
Generate findings and recommendations
    ↓
Return JSON result
```

### Assessment Result Structure

```json
{
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
      "message": "Uses Qlik-specific features...",
      "affected_objects": ["Sheet1", "Sheet3"]
    }
  ],
  "incompatibilities": [
    "Qlik Set Analysis requires manual conversion",
    "Advanced aggregation functions need USERELATIONSHIP"
  ],
  "recommendations": [
    "Review Set Analysis manually",
    "Validate hierarchies in Fabric"
  ]
}
```

---

## 📍 Phase 4: Assessment Agent Completes

### Assessment Agent returns HTTP 200

```
Semantic Kernel receives response
    ↓
Extract assessment_result JSON
    ↓
Call mongo_service.save_assessment_record(
    run_id="8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    app_id="05796d2f-579b-4539-9b56-3ebd0b266115",
    workspace_id="personal",
    app_name="Executive Sales Analytics",
    assessment_result=<full_json>,
    source_type="qlik"
)
    ↓
Determine target database:
    source_type=="qlik" → Database: QT2F
    source_type=="tableau" → Database: QT2F_Tableau
    ↓
Save to PRIMARY database (QT2F/QT2F_Tableau)
    └─→ collection: assessment
    └─→ document: assessment record (see below)
    ↓
Mark assessment_status = "completed" in run_history
    ↓
Log agent action: "Assessment completed"
    ↓
Extract AI provider used
    └─→ Save to run_history.actual_provider = "groq"
    └─→ Save to run_history.actual_model = "llama-3.3-70b-versatile"
```

---

## 📍 Phase 5: Assessment Result Stored in MongoDB

### Database: QT2F (Qlik) or QT2F_Tableau (Tableau)
### Collection: assessment

```json
{
  "_id": ObjectId,
  "id": "uuid-for-this-assessment",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
  "workbook_id": "05796d2f-579b-4539-9b56-3ebd0b266115",  // For Tableau compatibility
  "workspace_id": "personal",
  "project_id": "personal",  // For Tableau compatibility
  "space_id": "personal",
  "app_name": "Executive Sales Analytics",
  "workbook_name": "Executive Sales Analytics",  // For Tableau compatibility
  "folder_name": "Executive Sales Analytics",
  "source_type": "qlik",
  
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
        "message": "Uses Qlik-specific features...",
        "affected_objects": ["Sheet1", "Sheet3"]
      }
    ],
    "incompatibilities": [
      "Qlik Set Analysis requires manual conversion",
      "Advanced aggregation functions need USERELATIONSHIP"
    ],
    "recommendations": [
      "Review Set Analysis manually",
      "Validate hierarchies in Fabric"
    ]
  },
  
  "timestamp": ISODate("2026-09-01T10:01:30Z"),
  "created_at": ISODate("2026-09-01T10:01:30Z"),
  "updated_at": ISODate("2026-09-01T10:01:30Z")
}
```

### Parallel: run_history updated

**Database: QT2F (Qlik) or QT2F_Tableau (Tableau)**
**Collection: run_history**

```json
{
  "_id": ObjectId,
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "run_no": "R-101",
  "email_id": "user@company.com",
  "source_type": "qlik",
  "workspace_id": "personal",
  "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
  "app_name": "Executive Sales Analytics",
  
  "assessment_status": "completed",                    // ← CHANGED
  "assessment_message": "Assessment completed successfully",  // ← CHANGED
  "actual_provider": "groq",                           // ← NEW
  "actual_model": "llama-3.3-70b-versatile",          // ← NEW
  "model_mode": "auto",                               // ← NEW
  
  "parsing_status": "pending",
  "mapping_status": "pending",
  "report_generation_status": "pending",
  "validation_status": "pending",
  "overall_status": "running",                        // ← CHANGED
  
  "created_at": ISODate("2026-09-01T10:00:00Z"),
  "updated_at": ISODate("2026-09-01T10:01:30Z")       // ← CHANGED
}
```

### Parallel: semantic_kernel record updated

**Database: QT2F (Qlik) or QT2F_Tableau (Tableau)**
**Collection: semantic_kernel**

```json
{
  "_id": ObjectId,
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "run_no": "R-101",
  "email_id": "user@company.com",
  "status": "running",
  "overall_status": "running",
  
  "status_list": [
    {
      "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
      "workspace_id": "personal",
      "app_name": "Executive Sales Analytics",
      "steps": {
        "assessment": "COMPLETED",                    // ← CHANGED
        "parsing": "PENDING",
        "mapping": "PENDING",
        "report_generation": "PENDING",
        "validation": "PENDING"
      },
      "final_status": "RUNNING",
      "start_date_time": "2026-09-01T10:00:00Z",
      "end_date_time": null,
      "time_duration": null,
      "time_elapsed": 90
    }
  ],
  
  "updated_at": ISODate("2026-09-01T10:01:30Z")
}
```

### Agent Actions logged

```json
[
  {
    "id": "action-step1",
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "agent_name": "Assessment Agent",
    "activity_summary": "Assessment starting",
    "status": "running",
    "timestamp": ISODate("2026-09-01T10:00:30Z")
  },
  {
    "id": "action-step2",
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "agent_name": "Assessment Agent",
    "activity_summary": "Extracted 45 visualizations",
    "status": "success",
    "timestamp": ISODate("2026-09-01T10:00:45Z")
  },
  {
    "id": "action-step3",
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "agent_name": "Assessment Agent",
    "activity_summary": "Analyzed 23 calculations",
    "status": "success",
    "timestamp": ISODate("2026-09-01T10:01:00Z")
  },
  {
    "id": "action-step4",
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "agent_name": "Assessment Agent",
    "activity_summary": "Generated assessment report",
    "status": "success",
    "timestamp": ISODate("2026-09-01T10:01:15Z")
  },
  {
    "id": "action-step5",
    "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    "agent_name": "Assessment Agent",
    "activity_summary": "Assessment completed",
    "status": "success",
    "timestamp": ISODate("2026-09-01T10:01:30Z")
  }
]
```

---

## 📍 Phase 6: Client Retrieves Assessment Result

### API Call: GET /api/results/assessment

```
Client sends:
  GET /api/results/assessment?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=05796d2f-579b-4539-9b56-3ebd0b266115
    ↓
Semantic Kernel receives request
    ↓
Call mongo_service.get_assessment_result(
    run_id="8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    app_id="05796d2f-579b-4539-9b56-3ebd0b266115"
)
    ↓
Query PRIMARY database (QT2F or QT2F_Tableau)
    Collection: assessment
    Filter: {
      run_id: "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
      $or: [
        { app_id: "05796d2f-579b-4539-9b56-3ebd0b266115" },
        { workbook_id: "05796d2f-579b-4539-9b56-3ebd0b266115" }
      ]
    }
    ↓
Return matching document
    ↓
Respond to client with JSON
```

### Response to Client

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
    "assessment_result": {
      "status": "success",
      "complexity_score": 75,
      "readiness_score": 85,
      "estimated_effort": "MEDIUM",
      ...
    }
  }
}
```

---

## 📍 Phase 7: Client Retrieves Agent Actions

### API Call: GET /api/results/assessment-agent-actions

```
Client sends:
  GET /api/results/assessment-agent-actions?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=05796d2f-579b-4539-9b56-3ebd0b266115
    ↓
Semantic Kernel receives request
    ↓
Call mongo_service.get_assessment_agent_actions(
    run_id="8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
    app_id="05796d2f-579b-4539-9b56-3ebd0b266115"
)
    ↓
Query PRIMARY database
    Collection: agent_actions
    Filter: {
      run_id: "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
      agent_name: { $regex: "^Assessment Agent" },
      $or: [
        { app_id: "05796d2f-579b-4539-9b56-3ebd0b266115" },
        { workbook_id: "05796d2f-579b-4539-9b56-3ebd0b266115" }
      ]
    }
    Sort: timestamp ascending (chronological)
    ↓
Return list of matching documents
    ↓
Respond to client with JSON array
```

### Response to Client

```json
{
  "status": "success",
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "app_id": "05796d2f-579b-4539-9b56-3ebd0b266115",
  "count": 5,
  "phase": "assessment",
  "data": [
    { "activity_summary": "Assessment starting", "timestamp": "...", ... },
    { "activity_summary": "Extracted 45 visualizations", "timestamp": "...", ... },
    { "activity_summary": "Analyzed 23 calculations", "timestamp": "...", ... },
    { "activity_summary": "Generated assessment report", "timestamp": "...", ... },
    { "activity_summary": "Assessment completed", "timestamp": "...", ... }
  ]
}
```

---

## 🎯 Key Database Locations

### For Qlik Apps:
- **Primary Database**: `QT2F`
- **Collections**:
  - `run_history` → Phase status for Qlik runs
  - `assessment` → Qlik assessment results
  - `parsing` → Qlik parsing results
  - `mapping` → Qlik mapping results
  - `report_generation` → Qlik generated artifacts
  - `agent_actions` → All agent activity logs
  - `semantic_kernel` → Aggregate run records

### For Tableau Workbooks:
- **Primary Database**: `QT2F_Tableau`
- **Collections**: (Same structure as Qlik)

---

## 💾 Data Consistency Guarantee

When assessment completes, exactly these documents are created/updated:

1. ✅ `run_history` — status = "completed"
2. ✅ `assessment` — full result document
3. ✅ `agent_actions` — 5 activity log entries (start, steps, end)
4. ✅ `semantic_kernel` — aggregate run record with phase status

**All four are atomically consistent** because they're saved in order before moving to the next phase.

---

## 🔍 Debugging: Verify Complete Storage

```javascript
// Check if assessment completed successfully
db.run_history.findOne({
  run_id: "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  app_id: "05796d2f-579b-4539-9b56-3ebd0b266115"
})
// Expected: assessment_status = "completed"

// Check if assessment result exists
db.assessment.findOne({
  run_id: "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  app_id: "05796d2f-579b-4539-9b56-3ebd0b266115"
})
// Expected: document with assessment_result field

// Check if agent actions logged
db.agent_actions.find({
  run_id: "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  agent_name: /Assessment/
}).count()
// Expected: >= 2 (at least start and end)

// Check if semantic kernel updated
db.semantic_kernel.findOne({
  run_id: "8f3b23e7-7193-4df1-8e9a-bb808cf702e5"
})
// Expected: status_list[0].steps.assessment = "COMPLETED"
```

---

## 🚀 Performance Timeline (Example)

```
10:00:00 — run_history created (status=pending)
10:00:00 — semantic_kernel created (status=pending)
10:00:05 — Assessment API called
10:00:30 — First agent action logged (Assessment starting)
10:00:45 — Agent action logged (Extracted visualizations)
10:01:00 — Agent action logged (Analyzed calculations)
10:01:15 — Agent action logged (Generated report)
10:01:30 — Assessment result saved to MongoDB
10:01:30 — run_history updated (status=completed)
10:01:30 — semantic_kernel updated (status=completed)
10:01:30 — Agent action logged (Assessment completed)

Total: 90 seconds for entire assessment phase
```

---
