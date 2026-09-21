# Quick Start: Get Your Tableau Assessment Results in 5 Minutes

This guide gets you from "I want to see Tableau results" to "I have Tableau results" in 5 minutes.

---

## 🚀 3-Step Quick Start

### Step 1: Submit Your Tableau Workbook (30 seconds)

Copy-paste this command, replacing values:

```bash
curl -X POST http://localhost:8000/invoke-batch \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "email": "your.email@company.com",
    "source_type": "tableau",
    "deployment_type": "DIRECT_FABRIC",
    "department_repo": "Tableau_Migrated",
    "fabric_group_id": "your-fabric-group-id",
    "site_id": "your-tableau-site-id",
    "model": "auto",
    "run_validation": false,
    "items": [
      {
        "project_id": "YOUR_PROJECT_ID",
        "project_name": "Your Project Name",
        "workbook_id": "YOUR_WORKBOOK_ID",
        "workbook_name": "Your Workbook Name"
      }
    ]
  }'
```

**You'll get back:**
```json
{
  "success": true,
  "run_id": "8f3b23e7-7193-4df1-8e9a-bb808cf702e5",
  "run_no": "R-101"
}
```

✅ **Save the `run_id`** — you'll need it for the next steps!

---

### Step 2: Check Progress (Repeat Every 30 Seconds)

```bash
curl "http://localhost:8000/run-history?email=your.email@company.com&run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&project_id=YOUR_PROJECT_ID" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**Look for this in the response:**
```json
{
  "assessment_status": "completed",  ← This is what you're waiting for
  "assessment_message": "Assessment completed successfully"
}
```

⏱️ **Typical wait time:** 1-5 minutes

Once you see `"assessment_status": "completed"`, proceed to Step 3.

---

### Step 3: Get Your Assessment Result (30 seconds)

When assessment is done, run this:

```bash
curl "http://localhost:8000/api/results/assessment?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=YOUR_WORKBOOK_ID" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**You'll get back your assessment scores and findings:**

```json
{
  "status": "success",
  "data": {
    "workbook_name": "Your Workbook Name",
    "assessment_result": {
      "status": "success",
      "complexity_score": 72,
      "readiness_score": 85,
      "estimated_effort": "MEDIUM",
      "object_count": {
        "sheets": 8,
        "visualizations": 32,
        "calculations": 12
      },
      "assessment_findings": [
        {
          "severity": "MEDIUM",
          "message": "Tableau Set Analysis requires manual DAX conversion"
        }
      ],
      "recommendations": [
        "Review all calculated fields for DAX equivalents",
        "Plan for data refresh strategy in Fabric"
      ]
    }
  }
}
```

✅ **You're done!** You have your assessment result!

---

## 📊 What the Scores Mean

| Score | Assessment Result | What You Should Do |
|-------|------|---------|
| 0-30 | ❌ Low Readiness | May need significant redesign |
| 31-60 | ⚠️ Medium Readiness | Plan for manual work |
| 61-85 | ✅ Good Readiness | Straightforward migration |
| 86-100 | ✨ Excellent Readiness | Quick migration expected |

---

## 🔍 Get More Details: What The Agent Did

Want to see exactly what happened during assessment? Run:

```bash
curl "http://localhost:8000/api/results/assessment-agent-actions?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=YOUR_WORKBOOK_ID" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**You'll see the step-by-step log:**

```json
{
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

---

## 💾 Where Is The Data?

Your assessment data is stored in MongoDB here:

| What | Where | Database |
|------|-------|----------|
| Assessment scores & findings | `assessment` collection | `QT2F_Tableau` |
| What agent did | `agent_actions` collection | `QT2F_Tableau` |
| Phase status | `run_history` collection | `QT2F_Tableau` |
| Run metadata | `semantic_kernel` collection | `QT2F_Tableau` |

💡 **All Tableau data** is in `QT2F_Tableau` database

---

## 📋 Complete Checklist

- [ ] **Step 1:** Submit workbook via `/invoke-batch` → Got `run_id`
- [ ] **Step 2:** Check status via `/run-history` → Status is `"completed"`
- [ ] **Step 3:** Get results via `/api/results/assessment` → Got scores & findings
- [ ] **Optional:** Get details via `/api/results/assessment-agent-actions` → Saw steps

---

## ⏱️ Timeline Expectations

```
0:00    Submit workbook
          ↓
0:30    Assessment agent starts
          ↓
1:00    Agent extracts visualizations
          ↓
1:30    Agent analyzes calculations
          ↓
2:00    Agent generates findings
          ↓
2:30    Assessment complete ✅ (ready to retrieve)
          ↓
2:35    You get results via API
```

**Total time:** 2-5 minutes

---

## 🔧 Troubleshooting Quick Fixes

### Problem: `/run-history` returns empty
**Solution:** Check that your `run_id` is spelled exactly right (copy from Step 1 response)

### Problem: `/api/results/assessment` returns `not_found`
**Solution:** Assessment still running. Go back to Step 2 and check status again.

### Problem: Results show `complexity_score: 0`
**Solution:** Assessment didn't complete. Check `/run-history` for errors in `assessment_message`.

### Problem: "Authorization Bearer token invalid"
**Solution:** Replace `YOUR_TOKEN_HERE` with your actual auth token.

---

## 📝 Real Example: End-to-End

Here's a real example you can copy-paste and modify:

### 1. Submit
```bash
curl -X POST http://localhost:8000/invoke-batch \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer abc123def456" \
  -d '{
    "email": "alice@company.com",
    "source_type": "tableau",
    "deployment_type": "DIRECT_FABRIC",
    "department_repo": "Tableau_Migrated",
    "fabric_group_id": "c5068f11-011c-4648-a151-231f32581819",
    "site_id": "techcoreteam2026-50af0fff68",
    "model": "auto",
    "items": [
      {
        "project_id": "c5134699-2aa2-4ab2-b201-7fcd06cf453a",
        "project_name": "Finance Analytics",
        "workbook_id": "0d148ef0-7433-46f0-b4bc-dd52180b9ab2",
        "workbook_name": "Sales Dashboard"
      }
    ]
  }'
```

**Response:**
```
run_id: 8f3b23e7-7193-4df1-8e9a-bb808cf702e5
```

### 2. Check Status (wait 2 minutes, then run)
```bash
curl "http://localhost:8000/run-history?email=alice@company.com&run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&project_id=c5134699-2aa2-4ab2-b201-7fcd06cf453a" \
  -H "Authorization: Bearer abc123def456"
```

**When you see `"assessment_status": "completed"`, continue to step 3**

### 3. Get Results
```bash
curl "http://localhost:8000/api/results/assessment?run_id=8f3b23e7-7193-4df1-8e9a-bb808cf702e5&app_id=0d148ef0-7433-46f0-b4bc-dd52180b9ab2" \
  -H "Authorization: Bearer abc123def456"
```

**You get back:**
```json
{
  "data": {
    "assessment_result": {
      "complexity_score": 72,
      "readiness_score": 85,
      "assessment_findings": [...]
    }
  }
}
```

✅ Done!

---

## 🎓 Next Steps After Getting Results

### If complexity_score > 70 (Complex)
→ Review the findings in detail
→ Plan manual work for incompatibilities
→ Allocate more time for migration

### If complexity_score 40-70 (Moderate)
→ Follow recommendations
→ Plan standard migration timeline
→ Prepare team for manual adjustments

### If complexity_score < 40 (Simple)
→ Quick migration expected
→ Minimal manual work needed
→ Fast path to Fabric

---

## 📞 Need More Help?

| Topic | Read This |
|-------|-----------|
| Complete API examples | COMPLETE_RESULT_RETRIEVAL_GUIDE.md |
| What data is stored where | TABLEAU_STORAGE_AND_RETRIEVAL.md |
| How it all works | ASSESSMENT_DATA_FLOW.md |
| Schema details | TABLEAU_QLIK_DATABASE_SCHEMA.md |
| Navigation map | DOCUMENTATION_INDEX.md |

---

## ✨ That's It!

You now know:
✅ How to submit a Tableau workbook
✅ How to check progress
✅ How to get assessment results
✅ What the scores mean
✅ Where the data is stored

**Go run your first assessment now!** 🚀

---
