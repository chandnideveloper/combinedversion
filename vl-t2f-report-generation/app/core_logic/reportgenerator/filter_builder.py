import json
import uuid
import re
from typing import Dict, Optional, List, Tuple
from app.core.logging_utils import log_info, log_error, log_warning
from app.core.config import Config
from app.core_logic.template_manager.template_manager import TemplateManager
from app.services.action_logger import ActionLogger


class FilterBuilderMixin:
    pass
