📊 Tableau to Fabric Autonomous Migration Agent:-

An enterprise-grade, AI-powered orchestration system built to autonomously migrate Tableau workbooks and data layers directly into Microsoft Fabric and Power BI. This system reduces manual rebuild efforts by utilizing a multi-agent architecture to parse Tableau files, map schemas, convert calculations, and generate Fabric-ready Tabular Model Definition Language (TMDL) and Power BI Report (PBIR) artifacts.

 
This application is designed as a production-ready backend that can be deployed as an Azure Managed Application within a customer's tenant.

 

🏗️ Tech Stack
Deployment Model: Azure Managed Application (One-click deploy via ARM/Bicep) 

Backend API: Python 3.11 + FastAPI (Async & optimized for LLM calls) 

Agent Orchestration: Microsoft AutoGen / Semantic Kernel 

LLM Provider: AI Foundry using OpenAI GPT-4o (2025-03-31 model) 

Storage & Config: Azure Cosmos DB (configs/logs) and Azure Key Vault (credentials) 

Data/Telemetry: Azure Monitor, Application Insights, Log Analytics Workspace 



📂 Project Structure

 
report gen/
├── .env                        # Environment variables (Azure DB, OpenAI credentials)
├── .gitignore                  # Git ignore rules
├── Dockerfile                  # Production-ready Docker container instructions
├── requirements.txt            # Python dependencies (FastAPI, autogen, openai, etc.)
├── main.py                     # FastAPI application entry point (/migrate endpoint)
└── app/                        
    ├── config.py               # Config loader for Azure DevOps, AI, and Cosmos DB
    ├── schemas.py              # Pydantic models for API request validation
    ├── logging_utils.py        # Centralized logging sending telemetry to Azure Monitor
    ├── agents/                 # Migration AI Agents
    │   ├── coordinator_agent.py  # Orchestrates the migration workflow
    │   ├── file_agent.py         # File manipulation and CI/CD Azure DevOps pushing
    │   ├── folder_agent.py       # Manages repository folder destinations
    │   └── tableau_parser.py     # Parses legacy Tableau .twbx/.twb XML files
    ├── core_logic/             # Translation Business Logic
    │   ├── report_generator.py   # Assembles PBIR JSON layout and coordinates
    │   ├── template_manager.py   # Loads base Power BI visual templates
    │   └── tmdl_generator.py     # Translates schemas to TMDL, DAX, and M Scripts
    └── templates/              
        ├── static/               # Core PBIP structural JSON templates
        └── visuals/              # Component templates (barChart, card, pieChart)


⚙️ Configuration (.env)
Create a .env file in the root directory. Security compliance requires that passwords or sensitive data must not be exposed in standard logs, and should be securely referenced via Azure Key Vault in production.


# ==========================================
# Deployment Settings + Key Vault
# ==========================================
# Base API used to resolve deployment targets and token IDs:
#   /deployment/azure-devops -> org/project/repo + token_id
#   /deployment/git          -> org/repo + token_id
DEPLOYMENT_SETTINGS_API_URL="https://<your-deployment-settings-api>"

# Key Vault URL where token_id is resolved to the actual PAT secret.
# This service is expected to use managed identity / container access policy.
KEYVAULT_API_URL="https://<your-keyvault-name>.vault.azure.net/"

# Branch/environment selector used by pushes (e.g., dev, qa, main)
ENVIRONMENT="production"
 
# ==========================================
# AI / LLM Settings (GPT-4o via AI Foundry)
# ==========================================
AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
AZURE_OPENAI_ENDPOINT="https://your-resource-name.openai.azure.com/"
AZURE_OPENAI_API_VERSION="2024-02-15-preview"
 
# ==========================================
# Application Settings
# ==========================================
COSMOS_DB_API_URL="https://<your-cosmos-api>"
PORT=7000


💻 Installation & Execution

Option 1: Running via Docker (Production / Azure Container Apps)
The application is containerized for seamless deployment via Azure Container Apps using GitHub Actions.
 
 # Build the production image
docker build -t vectorlab-migration-agent .
 
# Run the container locally for testing
docker run -d -p 7000:7000 --env-file .env --name fabric_agent vectorlab-migration-agent

Option 2: Local Development Environment

# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
 
# 2. Install backend dependencies
pip install -r requirements.txt
 
# 3. Start the FastAPI server locally
uvicorn main:app --host 0.0.0.0 --port 7000 --reload
 

 📡 API Usage
Start Migration Endpoint
Triggers the autonomous workflow to read mapped inputs from Cosmos DB, generate Fabric TMDL/PBIR code, and push the artifacts directly to the configured Azure DevOps deployment pipeline.

 
Endpoint: POST /migrate
Headers:

Authorization: Bearer <token> (Requires Microsoft Entra ID authentication)
Content-Type: application/json
Request Body:
 
 {
  "folder_name": "Finance_Dashboards",
  "project_id": "proj_abc123",
  "workbook_id": "wb_456def",
  "run_id": "run_001",
  "department_repo": "finance-fabric-repo"
}


🔒 Security & Compliance
- **Authentication & Authorization**: Secured via Microsoft Entra ID (M365) with robust JWT signature verification against Entra ID JWKS endpoints (`RS256`), issuer matching, and audience validation via the shared `app.core.auth` package.
- **Least-Privilege Access**: All Azure service interactions (Key Vault, Cosmos DB, Azure Monitor) utilize `DefaultAzureCredential` from `azure-identity` for managed identity least-privilege authentication.
- **Compliance**: Architecture complies with GDPR and ISO 27001 standards. PII data masking is enforced during data layer transitions.
- **Networking**: Uses HTTPS with TLS 1.2+ exclusively; backend components are privately networked.

---

## 🛡️ Resilience & Observability

### Resilient HTTP Client & Circuit Breaker
To prevent cascading failures across downstream services (Azure DevOps, Key Vault, Cosmos DB, AI Foundry), all outbound HTTP calls use `ResilientHttpClient` (`app/core/http_client.py`), featuring:
- **Timeouts**: Enforced default and connection timeouts on all requests.
- **Exponential Backoff**: Automated retries with capped exponential backoff for idempotent requests (`GET`) and transient `5xx` / network errors.
- **Per-Host Circuit Breaker**: Tracks consecutive failures per domain. Transitions from `CLOSED` to `OPEN` after threshold failures, fast-failing subsequent requests with `CircuitBreakerOpenException` until the recovery period elapses (`HALF_OPEN`).

### Centralized Structured Logging & Dead-Letter Store
- **Correlation Tracking**: Uses `contextvars` to propagate `run_id`, `project_id`, and `workbook_id` across all async tasks and logs.
- **Contract Validation**: All Cosmos DB telemetry payloads are validated against Pydantic schemas (`CosmosLogRecord`, `CosmosActivityRecord`, `CosmosGenerationRecord`).
- **Dead-Letter Storage**: If Cosmos DB logging fails or times out, logs are automatically persisted locally to `deadletter_store/failed_cosmos_writes.jsonl` to ensure zero telemetry loss.

---

## 🧪 Testing & CI/CD Pipeline

### Running Unit Tests
The repository includes a comprehensive unit test suite covering authentication, resilience, contracts, and smoke tests:
```bash
# Run all unit tests locally
python -m unittest discover -s tests -v
```

### CI/CD Pipeline (`azure-pipelines.yml`)
The automated CI/CD pipeline enforces code quality and reliability:
1. **Validate Stage**: Automatically runs syntax checks (`flake8`) and the full unit test suite (`pytest` / `unittest`) across all branch pushes before Docker images are built.
2. **Build & Push Stages**: Containerizes and deploys environment-specific builds (`Dev`, `Test`, `Prod`) to Azure Container Registry (ACR) upon validation success.