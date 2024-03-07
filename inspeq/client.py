import logging
import requests

API_URL = "https://api.inspeq.ai"

# Configure logging
logger = logging.getLogger(__name__)


def handle_request_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            if response is None:
                logger.error("API request returned NoneType.")
                return None
            if isinstance(response, (str, float)):
                logger.error(f"Unexpected response received: {response}")
                return None
            if response.status_code == 401:
                logger.error("API key is not valid.")
                return None
            response.raise_for_status()
            return response.json()["data"]
        except requests.exceptions.RequestException as e:
            error_msg = str(e)
            if "for url:" in error_msg:
                error_msg = error_msg.split("for url:")[
                    0
                ].strip()  # Extracts the error message
            logger.error(f"Request failed: {error_msg}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise

    return wrapper


class Evaluator:
    def __init__(self, sdk_api_key, api_url=None):
        if not sdk_api_key:
            raise ValueError("No SDK API key provided.")
        self.sdk_api_key = sdk_api_key
        self.API_URL = api_url if api_url else API_URL

    @handle_request_exceptions
    def make_api_request(self, endpoint, input_data):
        # Validate input_data
        stripped_input_data = {key: value.strip() if isinstance(value, str) else value for key, value in input_data.items()}
        if not stripped_input_data.get("llm_input_query"):
            logger.error("The 'llm_input_query' field is empty.")
            return None
        if not stripped_input_data.get("llm_input_context"):
            logger.error("The 'llm_input_context' field is empty.")
            return None
        if not stripped_input_data.get("llm_output"):
            logger.error("The 'llm_output' field is empty.")
            return None

        url = f"{self.API_URL}/api/v1/sdk/{endpoint}"
        return requests.post(
            url,
            params={"secret_key": self.sdk_api_key},
            json=stripped_input_data,
        )

    def word_limit_test(self, input_data):
        # Validate input_data
        stripped_input_data = {key: value.strip() if isinstance(value, str) else value for key, value in input_data.items()}
        if not stripped_input_data.get("llm_input_query"):
            logger.error("The 'llm_input_query' field is empty.")
            return None
        if not stripped_input_data.get("llm_input_context"):
            logger.error("The 'llm_input_context' field is empty.")
            return None
        if not stripped_input_data.get("llm_output"):
            logger.error("The 'llm_output' field is empty.")
            return None

        url = f"{self.API_URL}/api/v1/sdk/word_limit_test"
        response = requests.post(
            url,
            params={"secret_key": self.sdk_api_key},
            json=stripped_input_data,
        )
        response.raise_for_status()

        return response.json()["data"]

    def grammatical_correctness(self, input_data):
        return self.make_api_request("grammatical_correctness", input_data)

    def do_not_use_keywords(self, input_data):
        return self.make_api_request("do_not_use_keywords", input_data)

    def fluency(self, input_data):
        return self.make_api_request("answer_fluency", input_data)

    def answer_relevance(self, input_data):
        return self.make_api_request("answer_relevance", input_data)

    def response_tone(self, input_data):
        # Validate input_data
        stripped_input_data = {key: value.strip() if isinstance(value, str) else value for key, value in input_data.items()}
        if not stripped_input_data.get("llm_input_query"):
            logger.error("The 'llm_input_query' field is empty.")
            return None
        if not stripped_input_data.get("llm_input_context"):
            logger.error("The 'llm_input_context' field is empty.")
            return None
        if not stripped_input_data.get("llm_output"):
            logger.error("The 'llm_output' field is empty.")
            return None

        url = f"{self.API_URL}/api/v1/sdk/response_tone"
        response = requests.post(
            url,
            params={"secret_key": self.sdk_api_key},
            json=stripped_input_data,
        )
        response.raise_for_status()

        return response.json()["data"]

    def factual_consistency(self, input_data):
        return self.make_api_request("factual_consistency", input_data)

    def conceptual_similarity(self, input_data):
        return self.make_api_request("conceptual_similarity", input_data)

    def readability(self, input_data):
        # Validate input_data
        stripped_input_data = {key: value.strip() if isinstance(value, str) else value for key, value in input_data.items()}
        if not stripped_input_data.get("llm_input_query"):
            logger.error("The 'llm_input_query' field is empty.")
            return None
        if not stripped_input_data.get("llm_input_context"):
            logger.error("The 'llm_input_context' field is empty.")
            return None
        if not stripped_input_data.get("llm_output"):
            logger.error("The 'llm_output' field is empty.")
            return None

        url = f"{self.API_URL}/api/v1/sdk/readability"
        response = requests.post(
            url,
            params={"secret_key": self.sdk_api_key},
            json=stripped_input_data,
        )
        response.raise_for_status()

        return response.json()["data"]

    def coherence(self, input_data):
        return self.make_api_request("coherence", input_data)

    def get_all_metrics(self, input_data):
        metrics_results = {}

        metrics_results["factual_consistency"] = self.factual_consistency(input_data)
        metrics_results["answer_relevance"] = self.answer_relevance(input_data)
        metrics_results["response_tone"] = self.response_tone(input_data)
        metrics_results["grammatical_correctness"] = self.grammatical_correctness(input_data)
        metrics_results["fluency"] = self.fluency(input_data)
        metrics_results["do_not_use_keywords"] = self.do_not_use_keywords(input_data)
        metrics_results["word_limit_test"] = self.word_limit_test(input_data)
        metrics_results["conceptual_similarity"] = self.conceptual_similarity(input_data)
        metrics_results["coherence"] = self.coherence(input_data)
        metrics_results["readability"] = self.readability(input_data)

        return metrics_results
