import requests


class Inspeq:
    def __init__(self, sdk_api_key):
        self.sdk_api_key = sdk_api_key


    def evaluate_word_limit_test(self,  input_data):
        url = "https://stage.inspeq.ai/api/v1/sdk/sdk_evaluate_word_limit_test"

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
        url = "https://stage.inspeq.ai/api/v1/sdk/sdk_evalaute_grammatical_correctness"

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
        url = "https://stage.inspeq.ai/api/v1/sdk/sdk_evaluate_do_not_use_keywords"

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
        url = "https://stage.inspeq.ai/api/v1/sdk/sdk_evalaute_response_tone"

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
        url = "https://stage.inspeq.ai/api/v1/sdk/sdk_evalaute_answer_relevance"

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
        url = "https://stage.inspeq.ai/api/v1/sdk/sdk_evalaute_response_tone"

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
        url = "https://stage.inspeq.ai/api/v1/sdk/sdk_evaluate_factual_consistency"

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
        url = "https://stage.inspeq.ai/api/v1/sdk/sdk_evalaute_conceptual_similarity"

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





inspeq_instance = Inspeq("12")


# Example input data
input_data = {
    "llm_input_query": "your_llm_input_context",
    "llm_input_context": "your_llm_input_query",
    "llm_output": "your_llm_output",
}

# Use the process_request method with the instance
print("1. evaluate_factual_consistency is:")
inspeq_instance.evaluate_factual_consistency(input_data)

print("\n 2. evalaute_answer_relevance is:")
inspeq_instance.evalaute_answer_relevance(input_data)

print("\n 3. evalaute_do_not_use_keywords is:")
inspeq_instance.evalaute_do_not_use_keywords(input_data)

print("\n 4. evalaute_grammatical_correctness is:")
inspeq_instance.evalaute_grammatical_correctness(input_data)

print("\n 5. evalaute_fluency is:")
inspeq_instance.evalaute_fluency(input_data)

print("\n 6. evaluate_conceptual_similarity is:")
inspeq_instance.evaluate_conceptual_similarity(input_data)

print("\n 7. evaluate_word_limit_test is:")
inspeq_instance.evaluate_word_limit_test(input_data)

print("\n 8. evaluate_response_tone is:")
inspeq_instance.evaluate_response_tone(input_data)











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
