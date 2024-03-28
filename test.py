from inspeq.client import Evaluator
from inspeq.client import Eval

# old way to call th metrics
API_KEY = "sdk_api-key"
inspeq_instance = Evaluator(sdk_api_key=API_KEY)

input_data =    {
    "prompt": "string",
    "context": "string",
    "response": "string"
  }
result=inspeq_instance.word_limit_test(input_data)
print(result)

# Eval new way to call the metrics

prompt = "query_text" # these are required fields depending on metrics
context = "context_text"  # these are required fields depending on metrics
response = "output_text"  # these are required fields depending on metrics
API_KEY = "sdk_api_key" # it is required field
task_name = "abc" #it is compulsory to provide whatever you want to give the task name.

metrics_list = [
    "DIVERSITY"
]
metrics_config = {
    "diversity_config": {
        "threshold": 0.5,
        "custom_labels": ["string"],
        "label_thresholds": [0],
    }
}
inspeq_instance = Eval(API_KEY)
result = inspeq_instance.evaluate_task(prompt, context, response, task_name, metrics_list, metrics_config)
print(result)