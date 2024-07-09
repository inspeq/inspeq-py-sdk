import logging
import requests
import os
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
logger = logging.getLogger(__name__)
class InspeqError(Exception):
    """Base exception class for Inspeq SDK errors."""

class APIError(InspeqError):
    """Exception raised for API-related errors."""

class ConfigError(InspeqError):
    """Exception raised for configuration-related errors."""

class InputError(InspeqError):
    """Exception raised for invalid input errors."""

class InspeqEval:
    
    DEFAULT_API_URL = "https://prod-api.inspeq.ai"
    
    def __init__(
        self, 
        inspeq_api_key: str, 
        inspeq_project_id: str, 
        inspeq_api_url: Optional[str] = None,
        log_level: int = logging.INFO
    ):
        if not inspeq_api_key:
            raise ConfigError("No SDK API key provided.")
        if not inspeq_project_id:
            raise ConfigError("No project ID provided.")

        self.inspeq_api_key = inspeq_api_key
        self.inspeq_project_id = inspeq_project_id
        self.inspeq_api_url = inspeq_api_url or os.getenv("INSPEQ_API_URL") or self.DEFAULT_API_URL
        
        self._setup_logging(log_level)
        self._setup_logging(log_level)

    def _setup_logging(self, log_level: int) -> None:
        logging.basicConfig(level=log_level)
        logger.setLevel(log_level)

    def _handle_http_error(self, response: requests.Response) -> None:
        if response.status_code == 400:
            raise APIError("Bad Request: " + response.text)
        elif response.status_code == 401:
            raise APIError("Unauthorized: SDK API key is not valid.")
        elif response.status_code == 409:
            raise APIError("Conflict: " + response.text)
        elif response.status_code == 422:
            error_detail = response.json().get("detail", "Invalid input.")
            raise InputError(error_detail)
        else:
            raise APIError(f"HTTP Error: {response.status_code} - {response.text}")

    def evaluate_llm_task(
        self, 
        metrics_list: List[str], 
        input_data: List[Dict[str, str]], 
        task_name: Optional[str] = None, 
        metrics_config: Optional[Dict] = None
    ) -> Dict:
        url = f"{self.inspeq_api_url}/api/v2/sdk/evaluate_llm"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        request_body = {
            "project_id": self.inspeq_project_id,
            "secret_key": self.inspeq_api_key,
            "metrics": metrics_list,
            "input_data": input_data,
            "task_name": task_name
        }
        payload = {
            "request_body": request_body,
            "metrics_config": metrics_config or {}
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(f"API call failed with status code {response.status_code}: {response.text}")
