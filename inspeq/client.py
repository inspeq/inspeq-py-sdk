import logging
import requests
import json

API_URL = "https://stage.inspeq.ai"

# Configure logging
logger = logging.getLogger(__name__)


class Evaluator:
    def __init__(self, sdk_api_key, api_url=None):
        if not sdk_api_key:
            raise ValueError("No SDK API key provided.")
        self.sdk_api_key = sdk_api_key
        self.API_URL = api_url if api_url else API_URL

    def make_api_request(self, endpoint, input_data, config_input:None, task_name:None):
        url = f"{self.API_URL}/api/v1/sdk/{endpoint}"
        

        prompt = input_data.get("prompt", "")
        context = input_data.get("context", "")
        response = input_data.get("response", "")

        try:
            response = requests.post(
                url,
                params={"secret_key": self.sdk_api_key, "task_name": task_name},
                json={
                    "input_data": {
                        "llm_input_query": prompt,
                        "llm_input_context": context,
                        "llm_output": response,
                    },
                    "config_input":config_input
                },
            )
            response.raise_for_status()

            return json.dumps(response.json()["data"])
        except requests.exceptions.HTTPError as err:
            if response.status_code == 400:
                print("Error: response status is 400")
                print("Response body:")
                print(response.text)
            elif response.status_code == 401:
                print("SDK API key is not valid.")
            elif response.status_code == 422:
                print("Error: Invalid input data. Please check the input")
                
            else:
                print(f"HTTP Error: {err}")
            return None

    def word_limit_test(self, input_data,  config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("prompt", "").strip()
        if not response_data:
            raise ValueError("'prompt' is not provided")

        return self.make_api_request("word_limit_test", input_data,config_input, task_name)

    # def grammatical_correctness(self, input_data):
    #     # Validate input_data
    #     response_data = input_data.get("response", "").strip()
    #     if not response_data:
    #         raise ValueError("'response' is not provided")

    #     return self.make_api_request("grammatical_correctness", input_data)


    def do_not_use_keywords(self, input_data,config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("do_not_use_keywords", input_data, config_input, task_name)

    # def fluency(self, input_data):
    #     # Validate input_data
    #     response_data = input_data.get("response", "").strip()
    #     if not response_data:
    #         raise ValueError("'response' is not provided")

    #     return self.make_api_request("answer_fluency", input_data)

    def answer_relevance(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("prompt", "").strip()
        if not response_data:
            raise ValueError("'prompt' is not provided")

        return self.make_api_request("answer_relevance", input_data, config_input, task_name)

    def response_tone(self, input_data, config_input, task_name= None):

        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("response_tone", input_data, config_input, task_name)

    def factual_consistency(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("factual_consistency", input_data, config_input, task_name)

    def conceptual_similarity(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("conceptual_similarity", input_data, config_input, task_name)

    def clarity(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("clarity", input_data, config_input, task_name)

    def readability(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("readability", input_data, config_input, task_name)

    def coherence(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("coherence", input_data, config_input, task_name)

    def model_refusal(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("model_refusal", input_data, config_input, task_name)

    def data_leakage(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("data_leakage", input_data, config_input, task_name)

    def diversity(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("diversity", input_data, config_input, task_name)

    def creativity(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("creativity", input_data, config_input, task_name)

    def narrative_continuity(self, input_data, config_input, task_name= None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        if not response_data:
            raise ValueError("'response' is not provided")
        

        return self.make_api_request("narrative_continuity", input_data, config_input, task_name)

    def get_all_metrics(self, input_data,config_input, task_name = None):
        metrics_results = {}

        metrics_results["factual_consistency"] = self.factual_consistency(input_data,config_input, task_name= None)
        metrics_results["answer_relevance"] = self.answer_relevance(input_data ,config_input, task_name= None)
        metrics_results["response_tone"] = self.response_tone(input_data ,config_input, task_name= None)
        # metrics_results["grammatical_correctness"] = self.grammatical_correctness(
        #     input_data
        # )
        # metrics_results["fluency"] = self.fluency(input_data)
        metrics_results["do_not_use_keywords"] = self.do_not_use_keywords(input_data ,config_input, task_name= None)
        metrics_results["word_limit_test"] = self.word_limit_test(input_data ,config_input, task_name= None)
        metrics_results["conceptual_similarity"] = self.conceptual_similarity(
            input_data ,config_input, task_name= None
        )
        metrics_results["coherence"] = self.coherence(input_data ,config_input, task_name= None)
        metrics_results["readability"] = self.readability(input_data ,config_input, task_name= None)
        metrics_results["clarity"] = self.clarity(input_data ,config_input, task_name= None)
        metrics_results["model_refusal"] = self.model_refusal(input_data ,config_input, task_name= None)
        metrics_results["data_leakage"] = self.data_leakage(input_data ,config_input, task_name= None)
        metrics_results["diversity"] = self.diversity(input_data ,config_input, task_name= None)
        metrics_results["creativity"] = self.creativity(input_data ,config_input, task_name= None)
        metrics_results["narrative_continuity"] = self.narrative_continuity(input_data ,config_input, task_name= None)

        return metrics_results


class Eval:
    def __init__(self, sdk_api_key, api_url=None):
        if not sdk_api_key:
            raise ValueError("No SDK API key provided.")
        self.sdk_api_key = sdk_api_key
        self.API_URL = api_url if api_url else API_URL
        self.task_name = None  # Initialize task_name

    def evaluate_task(
        self, prompt, context, response, task_name, metrics_list, metrics_config
    ):
        url = f"{self.API_URL}/api/v1/sdk/eval/?secret_key={self.sdk_api_key}&task_name={task_name}"
        headers = {"accept": "application/json", "Content-Type": "application/json"}

        payload = {
            "metrics_list": metrics_list,
            "input_data": {
                "llm_input_query": prompt,
                "llm_input_context": context,
                "llm_output": response,
            },
            "metrics_config": metrics_config or {},
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            api_response_data = response.json()

            # Extract and process data from each response:
            processed_data = []
            for response_dict in api_response_data:
                for (
                    metric_name,
                    metric_dict,
                ) in response_dict.items():  # Iterate through metric names
                    data_dict = metric_dict.get("data")  # Extract the 'data' dictionary
                    if data_dict:
                        processed_data.append(data_dict)

            return processed_data

        else:
            return f"{response.text}"

    # def eval(self, input_data, config_input=None, metrics_list=None):
    #     url = f"{self.API_URL}/api/v1/sdk/eval"
    #     prompt = input_data.get("prompt", "")
    #     context = input_data.get("context", "")
    #     response = input_data.get("response", "")

    #     # if config_input is None:
    #     #     config_input = {
    #     #         "threshold": 0.5,
    #     #         "custom_labels": ["string"],
    #     #         "label_thresholds": [0]
    #     #     }

    #     if metrics_list is None:
    #         return "Metrics list is not provided.It is required to evaluate the response."

    #     try:
    #         response = requests.post(
    #             url,
    #             params={"secret_key": self.sdk_api_key, "task_name": self.task_name},
    #             json={
    #                 "metrics_list": metrics_list,
    #                 "input_data": {
    #                     "llm_input_query": prompt,
    #                     "llm_input_context": context,
    #                     "llm_output": response,
    #                 },
    #                 "config_input": config_input
    #             },
    #         )
    #         response.raise_for_status()

    #         return json.dumps(response.json()["data"])
    #     except requests.exceptions.HTTPError as err:
    #         if response.status_code == 401:
    #             logging.error("SDK API key is not valid.")
    #         else:
    #             logging.error(f"HTTP Error: {err}")
    #         return None
