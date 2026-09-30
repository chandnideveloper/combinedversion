import asyncio
import uuid
import datetime
from typing import Optional, Dict, Any
from openai import AsyncAzureOpenAI
from app.tableau.core.config import Config
from app.tableau.core.logging_utils import log_error, log_info, log_warning, run_background_task
from app.services.activity_logger import UnifiedLogger

class ActionLogger:
    def __init__(self):
        self.unified_logger = UnifiedLogger("tableau")
        
        self.llm_client = None
        if Config.AZURE_OPENAI_API_KEY and Config.AZURE_OPENAI_ENDPOINT:
            self.llm_client = AsyncAzureOpenAI(
                api_key=Config.AZURE_OPENAI_API_KEY,
                api_version=Config.AZURE_OPENAI_API_VERSION,
                azure_endpoint=Config.AZURE_OPENAI_ENDPOINT
            )
            self.deployment_name = getattr(Config, "AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")

    async def _generate_llm_content(self, system_prompt: str, user_prompt: str) -> str:
        if not self.llm_client:
            return str(user_prompt)
        try:
            response = await self.llm_client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            log_error(f"[ActionLogger] LLM failed: {e}")
            return str(user_prompt)

    async def send_activity_to_api(self, project_id, workbook_id, run_id, technical_message, token=None, project_name="Unknown"):
        """Generates a summary and sends it to the central HTTP API."""
        summary = await self._generate_llm_content(
            "Summarize this action in <100 chars:", technical_message
        )
        await self.unified_logger.log_action_async(run_id, project_id, workbook_id, summary, status="running", project_name=project_name)
        # Also log the deep technical trace on successful runs
        await self.unified_logger.log_trace_async(run_id, project_id, workbook_id, technical_message, level="INFO", details=summary, project_name=project_name)

    async def send_error_to_api(self, project_id, workbook_id, run_id, technical_message, error_detail=None, token=None):
        """Logs an error event to the central HTTP API with an LLM-generated summary."""
        summary = await self._generate_llm_content(
            "Summarize this error in <100 chars:", technical_message
        )
        # Log to the action collection
        await self.unified_logger.log_action_async(run_id, project_id, workbook_id, summary, status="error")
        # Also log the deep technical trace
        await self.unified_logger.log_trace_async(run_id, project_id, workbook_id, technical_message, level="ERROR", details=str(error_detail))