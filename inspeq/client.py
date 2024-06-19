import logging
import requests
import json
import os


API_URL = "https://api.inspeq.ai"

# Configure logging
logger = logging.getLogger(__name__)


class InspeqEval:
    def __init__(self, inspeq_api_key, project_id, config_file=None, api_url=None):
        self.inspeq_api_key = inspeq_api_key
        self.project_id = project_id  # Ensure project_id is set
        self.API_URL = api_url if api_url else "https://api.inspeq.ai"
        self.task_name = None

        if not inspeq_api_key:
            raise ValueError("No SDK API key provided.")
        if not project_id:
            raise ValueError("No project ID provided.")

        if config_file is None:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            # Construct the full path to the JSON file
            config_file_path = os.path.join(script_dir, "config_file.json")
        else:
            config_file_path = config_file

        try:
            with open(config_file_path, "r") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file '{config_file_path}' not found.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error loading JSON from config file: {e}")

    def make_api_request(self, endpoint, input_data, config_input=None, task_name=None):
        url = f"{self.API_URL}/api/v2/sdk/{endpoint}"

        prompt = input_data.get("prompt", "")
        context = input_data.get("context", "")
        response = input_data.get("response", "")

        try:
            response = requests.post(
                url,
                params={
                    "project_id": self.project_id,
                    "secret_key": self.inspeq_api_key,
                    "task_name": task_name,
                },
                json={
                    "input_data": {
                        "llm_input_query": prompt,
                        "llm_input_context": context,
                        "llm_output": response,
                    },
                    "config_input": config_input,
                },
            )
            response.raise_for_status()
            return json.dumps(response.json()["data"])
        except requests.exceptions.HTTPError as err:
            if response.status_code == 400:
                print("Error: response status is 400")
                raise ValueError(response.text)
            elif response.status_code == 401:
                print("SDK API key is not valid.")
            elif response.status_code == 422:
                error_detail = response.json().get(
                    "detail", "Please check the details provided to the fucntion."
                )
                raise ValueError(error_detail)

            else:
                raise ValueError(f"{err}")
            return None

    def response_tone(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input if config_input else self.get_default_config("response_tone")
        )

        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request(
            "response_tone", input_data, config_input, task_name
        )

    def factual_consistency(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input
            if config_input
            else self.get_default_config("factual_consistency")
        )

        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request(
            "factual_consistency", input_data, config_input, task_name
        )

    def word_limit_test(self, input_data, config_input=None, task_name=None):

        # Validate input_data
        response_data = input_data.get("response", "").strip()
        config_input = (
            config_input if config_input else self.get_default_config("word_limit_test")
        )

        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("prompt", "").strip()
        if not response_data:
            raise ValueError("'prompt' is not provided")

        return self.make_api_request(
            "word_limit_test", input_data, config_input, task_name
        )

    def do_not_use_keywords(self, input_data, config_input=None, task_name=None):

        # Validate input_data
        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input
            if config_input
            else self.get_default_config("do_not_use_keywords")
        )

        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request(
            "do_not_use_keywords", input_data, config_input, task_name
        )

    def answer_relevance(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input
            if config_input
            else self.get_default_config("answer_relevance")
        )

        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("prompt", "").strip()
        if not response_data:
            raise ValueError("'prompt' is not provided")

        return self.make_api_request(
            "answer_relevance", input_data, config_input, task_name
        )

    def conceptual_similarity(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input
            if config_input
            else self.get_default_config("conceptual_similarity")
        )

        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request(
            "conceptual_similarity", input_data, config_input, task_name
        )

    def clarity(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input if config_input else self.get_default_config("clarity")
        )

        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("clarity", input_data, config_input, task_name)

    def creativity(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input if config_input else self.get_default_config("creativity")
        )

        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("creativity", input_data, config_input, task_name)

    def readability(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        config_input = (
            config_input if config_input else self.get_default_config("readability")
        )

        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request(
            "readability",
            input_data=input_data,
            config_input=config_input,
            task_name=task_name,
        )

    def coherence(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input if config_input else self.get_default_config("coherence")
        )

        if not response_data:
            raise ValueError("'response' is not provided")
        response_data = input_data.get("context", "").strip()
        if not response_data:
            raise ValueError("'context' is not provided")

        return self.make_api_request("coherence", input_data, config_input, task_name)

    def diversity(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        config_input = (
            config_input if config_input else self.get_default_config("diversity")
        )

        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request("diversity", input_data, config_input, task_name)

    def model_refusal(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        response_data = input_data.get("response", "").strip()
        config_input = (
            config_input if config_input else self.get_default_config("model_refusal")
        )

        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request(
            "model_refusal", input_data, config_input, task_name
        )

    def data_leakage(self, input_data, config_input=None, task_name=None):

        response_data = input_data.get("response", "").strip()

        config_input = (
            config_input if config_input else self.get_default_config("data_leakage")
        )

        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request(
            "data_leakage", input_data, config_input, task_name
        )

    def narrative_continuity(self, input_data, config_input=None, task_name=None):

        response_data = input_data.get("response", "").strip()
        config_input = (
            config_input
            if config_input
            else self.get_default_config("narrative_continuity")
        )

        if not response_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request(
            "narrative_continuity", input_data, config_input, task_name
        )

    def prompt_injection(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        prompt_data = input_data.get("prompt", "").strip()
        config_input = (
            config_input
            if config_input
            else self.get_default_config("prompt_injection")
        )

        if not prompt_data:
            raise ValueError("'input_prompt' is not provided")

        return self.make_api_request(
            "prompt_injection", input_data, config_input, task_name
        )

    def insecure_output(self, input_data, config_input=None, task_name=None):
        # Validate input_data
        prompt_data = input_data.get("response", "").strip()
        config_input = (
            config_input if config_input else self.get_default_config("insecure_output")
        )

        if not prompt_data:
            raise ValueError("'response' is not provided")

        return self.make_api_request(
            "insecure_output", input_data, config_input, task_name
        )

    def evaluate_llm_task(
        self, metrics_list, input_data, task_name=None, metrics_config=None
    ):
        url = 'https://api.inspeq.ai/api/v2/sdk/evaluate_llm'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        request_body = {
            "project_id": self.project_id,
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
            raise ValueError(f"API call failed with status code {response.status_code}: {response.text}")
        
    def get_metric_config(self, metric_name, metrics_config):
        if metrics_config and metric_name + "_config" in metrics_config:
            return metrics_config[metric_name + "_config"]
        else:
            default_config = (
                self.config.get("evaluations", {})
                .get("LLM", {})
                .get("configurations", {})
            )
            metric_config_name = f"{metric_name}_config"
            return default_config.get(metric_config_name, None)

    def get_default_config(self, metric_name):
        default_config = (
            self.config.get("evaluations", {}).get("LLM", {}).get("configurations", {})
        )
        metric_config_name = f"{metric_name}_config"
        return default_config.get(metric_config_name, None)
