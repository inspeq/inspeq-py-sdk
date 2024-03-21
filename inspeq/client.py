import logging
import requests
import json

API_URL = "https://api.inspeq.ai"

# Configure logging
logger = logging.getLogger(__name__)


class Evaluator:
    def __init__(self, sdk_api_key, api_url=None):
        if not sdk_api_key:
            raise ValueError("No SDK API key provided.")
        self.sdk_api_key = sdk_api_key
        self.API_URL = api_url if api_url else API_URL

    def make_api_request(self, endpoint, input_data):
        url = f"{self.API_URL}/api/v1/sdk/{endpoint}"
        prompt = input_data.get("prompt", "")
        context = input_data.get("context", "")
        response = input_data.get("response", "")

        try:
            response = requests.post(
                url,
                params={"secret_key": self.sdk_api_key},
                json={
                    "llm_input_query": prompt,
                    "llm_input_context": context,
                    "llm_output": response,
                },
            )
            response.raise_for_status()

            return json.dumps(response.json()["data"])
        except requests.exceptions.HTTPError as err:
            if response.status_code == 401:
                logger.error("SDK API key is not valid.")
            else:
                logger.error(f"HTTP Error: {err}")
            return None

    def word_limit_test(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("prompt", "").strip()
        if not response_data:
            raise ValueError("'prompt' is not provided")

        return self.make_api_request("word_limit_test", input_data)

    def grammatical_correctness(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("grammatical_correctness", input_data)

    def do_not_use_keywords(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("do_not_use_keywords", input_data)

    def fluency(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("answer_fluency", input_data)

    def answer_relevance(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("prompt", "").strip()
        if not response_data:
            raise ValueError("'prompt' is not provided")

        return self.make_api_request("answer_relevance", input_data)

    def response_tone(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("response_tone", input_data)

    def factual_consistency(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("factual_consistency", input_data)

    def conceptual_similarity(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("conceptual_similarity", input_data)

    def clarity(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("clarity", input_data)

    def readability(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("readability", input_data)

    def coherence(self, input_data):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("coherence", input_data)

    def get_all_metrics(self, input_data):
        metrics_results = {}

        metrics_results["factual_consistency"] = self.factual_consistency(input_data)
        metrics_results["answer_relevance"] = self.answer_relevance(input_data)
        metrics_results["response_tone"] = self.response_tone(input_data)
        metrics_results["grammatical_correctness"] = self.grammatical_correctness(
            input_data
        )
        metrics_results["fluency"] = self.fluency(input_data)
        metrics_results["do_not_use_keywords"] = self.do_not_use_keywords(input_data)
        metrics_results["word_limit_test"] = self.word_limit_test(input_data)
        metrics_results["conceptual_similarity"] = self.conceptual_similarity(
            input_data
        )
        metrics_results["coherence"] = self.coherence(input_data)
        metrics_results["readability"] = self.readability(input_data)
        metrics_results["clarity"] = self.clarity(input_data)

        return metrics_results
