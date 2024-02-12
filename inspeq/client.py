import logging
import requests
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Configure logging
logger = logging.getLogger(__name__)


class Evaluator:
    def __init__(self, sdk_api_key, API_URL=None):
        self.sdk_api_key = sdk_api_key
        self.API_URL = API_URL or "prod_url"
    def make_api_request(self, endpoint, input_data):
        url = f"{self.API_URL}{endpoint}"
        try: 
            response = requests.post(
                url,
                params={"secret_key": self.sdk_api_key},
                json=input_data,
                verify=False,
            )
            if response.status_code == 401:
                logger.error("API key is not valid.")
                return None
            response.raise_for_status()
            return response.json()["data"]
        except requests.exceptions.InvalidURL:
            logger.error("Invalid URL provided. Please provide a valid URL.")
            return None
        except requests.exceptions.ConnectionError:
            logger.error("Failed to establish a connection to the server.")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            return None

    def word_limit_test(self, input_data):
        url = f"{self.API_URL}/api/v1/sdk/word_limit_test"
     
        try:
            response = requests.post(
                url,
                params={"secret_key": self.sdk_api_key},
                json=input_data,
                verify=False,
            )
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

            return response.json()["data"]["word_limit_test"]

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise

    def grammatical_correctness(self, input_data):
        return self.make_api_request("/api/v1/sdk/grammatical_correctness", input_data)

    def do_not_use_keywords(self, input_data):
        return self.make_api_request("/api/v1/sdk/do_not_use_keywords", input_data)

    def fluency(self, input_data):
        return self.make_api_request("/api/v1/sdk/answer_fluency", input_data)

    def answer_relevance(self, input_data):
        return self.make_api_request("/api/v1/sdk/answer_relevance", input_data)

    def response_tone(self, input_data):
        url = f"{self.API_URL}/api/v1/sdk/response_tone"

        try:
            response = requests.post(
                url,
                params={"secret_key": self.sdk_api_key},
                json=input_data,
                verify=False,
            )
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

            return response.json()["data"]["tone"]
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise

    def factual_consistency(self, input_data):
        return self.make_api_request("/api/v1/sdk/factual_consistency", input_data)

    def conceptual_similarity(self, input_data):
        return self.make_api_request("/api/v1/sdk/conceptual_similarity", input_data)

    def get_all_metrics(self, input_data):
        start=time.time()
    
        metrics = []

        metrics.append(("factual_consistency", self.factual_consistency(input_data)))
        metrics.append(("answer_relevance", self.answer_relevance(input_data)))
        metrics.append((" response_tone", self.response_tone(input_data)))
        metrics.append(("grammatical_correctness", self.grammatical_correctness(input_data)))
        metrics.append(("fluency", self.fluency(input_data)))
        metrics.append(("do_not_use_keywords", self.do_not_use_keywords(input_data)))
        metrics.append(("word_limit_test", self.word_limit_test(input_data)))
        metrics.append(("conceptual_similarity", self.conceptual_similarity(input_data)))
        end=time.time()
        print("time",end-start)

        return metrics
    
