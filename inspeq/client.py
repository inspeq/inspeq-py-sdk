import requests
import os
from dataobjects import data_objects
from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL")

class Inspeq:
    def __init__(self, sdk_api_key):
        self.sdk_api_key = sdk_api_key

    def evaluate_word_limit_test(self, input_data):
        url = f"{API_URL}/sdk_evaluate_word_limit_test"

        try:
            response = requests.post(
                url, params={"secret_key": self.sdk_api_key}, json=input_data
            )
            response.raise_for_status()

            print(response.json())
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 401:
                print("API key is not valid")
            else:
                print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def evalaute_grammatical_correctness(self, input_data):
        url = f"{API_URL}/sdk_evalaute_grammatical_correctness"

        try:
            response = requests.post(
                url, params={"secret_key": self.sdk_api_key}, json=input_data
            )
            response.raise_for_status()

            print(response.json())
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 401:
                print("API key is not valid")
            else:
                print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def evalaute_do_not_use_keywords(self, input_data):
        url = f"{API_URL}/sdk_evaluate_do_not_use_keywords"

        try:
            response = requests.post(
                url, params={"secret_key": self.sdk_api_key}, json=input_data
            )
            response.raise_for_status()

            print(response.json())
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 401:
                print("API key is not valid")
            else:
                print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def evalaute_fluency(self, input_data):
        url = f"{API_URL}/sdk_evalaute_response_tone"

        try:
            response = requests.post(
                url, params={"secret_key": self.sdk_api_key}, json=input_data
            )
            response.raise_for_status()

            print(response.json())
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 401:
                print("API key is not valid")
            else:
                print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def evalaute_answer_relevance(self, input_data):
        url = f"{API_URL}/sdk_evalaute_answer_relevance"

        try:
            response = requests.post(
                url, params={"secret_key": self.sdk_api_key}, json=input_data
            )
            response.raise_for_status()

            print(response.json())
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 401:
                print("API key is not valid")
            else:
                print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def evaluate_response_tone(self, input_data):
        url = f"{API_URL}/sdk_evalaute_response_tone"

        try:
            response = requests.post(
                url, params={"secret_key": self.sdk_api_key}, json=input_data
            )
            response.raise_for_status()

            print(response.json())
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 401:
                print("API key is not valid")
            else:
                print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def evaluate_factual_consistency(self, input_data):
        url = f"{API_URL}/sdk_evaluate_factual_consistency"

        try:
            response = requests.post(
                url, params={"secret_key": self.sdk_api_key}, json=input_data
            )
            response.raise_for_status()

            print(response.json())
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 401:
                print("API key is not valid")
            else:
                print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def evaluate_conceptual_similarity(self, input_data):
        url = f"{API_URL}/sdk_evalaute_conceptual_similarity"

        try:
            response = requests.post(
                url, params={"secret_key": self.sdk_api_key}, json=input_data
            )
            response.raise_for_status()

            print(response.json())
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 401:
                print("API key is not valid")
            else:
                print(f"Request failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")




# Metrics implemented:
# 1. Word Limit Test - evaluate_word_limit_test
# 2. Grammatical Correctness - evalaute_grammatical_correctness
# 3. Do Not Use Keywords - evalaute_do_not_use_keywords
# 4. Fluency - evalaute_fluency
# 5. Answer Relevance - evalaute_answer_relevance
# 6. Response Tone - evaluate_response_tone
# 7. Factual consistency -evaluate_factual_consistency
# 8. Conceptual similarity- evaluate_conceptual_similarity

# Metrics to-do:
# (Add metrics that are planned but not yet implemented, if any)
