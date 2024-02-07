import logging
import requests

API_URL ="https://stage.inspeq.ai/api/v1/sdk"
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
    def __init__(self, sdk_api_key):
        self.sdk_api_key = sdk_api_key

    @handle_request_exceptions
    def make_api_request(self, endpoint, input_data):
        url = f"{API_URL}/{endpoint}"
        return requests.post(
            url, params={"secret_key": self.sdk_api_key}, json=input_data
        )
    
    def word_limit_test(self, input_data):
        url = f"{API_URL}/word_limit_test"

        response = requests.post(
            url, params={"secret_key": self.sdk_api_key}, json=input_data
        )
        response.raise_for_status()

        return response.json()["data"]['word_limit_test']
    

    def grammatical_correctness(self, input_data):
        return self.make_api_request("grammatical_correctness", input_data)

    def do_not_use_keywords(self, input_data):
        return self.make_api_request("do_not_use_keywords", input_data)

    def fluency(self, input_data):
        return self.make_api_request("answer_fluency", input_data)

    def answer_relevance(self, input_data):
        return self.make_api_request("answer_relevance", input_data)
    
    def response_tone(self, input_data):
        url = f"{API_URL}/response_tone"

        response = requests.post(
            url, params={"secret_key": self.sdk_api_key}, json=input_data
        )
        response.raise_for_status()

        return response.json()["data"]["tone"]

    def factual_consistency(self, input_data):
        return self.make_api_request("factual_consistency", input_data)

    def conceptual_similarity(self, input_data):
        return self.make_api_request("conceptual_similarity", input_data)