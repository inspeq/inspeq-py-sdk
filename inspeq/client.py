import logging
import requests

API_URL ="https://api.inspeq.ai"

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
        self.API_URL = API_URL

    @handle_request_exceptions
    def make_api_request(self, endpoint, input_data):
        url = f"{self.API_URL}/api/v1/sdk/{endpoint}"
        print(url)
        return requests.post(
            url, params={"secret_key": self.sdk_api_key}, json=input_data,verify=False
        )
    
    def word_limit_test(self, input_data):
        url = f"{self.API_URL}/api/v1/sdk/word_limit_test"

        response = requests.post(
            url, params={"secret_key": self.sdk_api_key}, json=input_data,verify=False
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
        url = f"{self.API_URL}/api/v1/sdk/response_tone"

        response = requests.post(
            url, params={"secret_key": self.sdk_api_key}, json=input_data,verify=False
        )
        response.raise_for_status()

        return response.json()["data"]["tone"]

    def factual_consistency(self, input_data):
        return self.make_api_request("factual_consistency", input_data)

    def conceptual_similarity(self, input_data):
        return self.make_api_request("conceptual_similarity", input_data)
    
    def get_all_metrices(self, input_data):
        print("\n  a. factual_consistency is:")
        print(self.factual_consistency(input_data))

        print("\n b. answer_relevance is:")
        print(self.answer_relevance(input_data))

        print("\n c. response_tone is:")
        print(self.response_tone(input_data))

        print("\n  d. grammatical_correctness is:")
        print(self.grammatical_correctness(input_data))

        print("\n e. fluency is:")
        print(self.fluency(input_data))

        print("\n f. do_not_use_keywords is:")

        print(self.do_not_use_keywords(input_data))

        print("\n g. word_limit_test is:")
        print(self.word_limit_test(input_data))

        print("\n h.  conceptual_similarity is:")
        print(self.conceptual_similarity(input_data))
