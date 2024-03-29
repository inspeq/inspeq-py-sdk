from inspeq.client import Evaluator
from inspeq.client import Eval

# old way to call th metrics
API_KEY = "in-f579f248eb74d2bbf5c4fa40bac03298"
inspeq_instance = Evaluator(sdk_api_key=API_KEY)

input_data =    {
    "prompt": "string",
    "context": "string",
    "response": "string"
  }

config_input= {
        "threshold": 0.5,
        "custom_labels": ["string","dsfd"],
        "label_thresholds": [0,0.5],
    }

result=inspeq_instance.data_leakage(input_data,config_input, task_name="test_task")
print(result)

#
prompt = "query_text" # these are required fields depending on metrics
context = "context_text"  # these are required fields depending on metrics
response = "output_text"  # these are required fields depending on metrics
task_name = "abc" #it is compulsory to provide whatever you want to give the task name.

metrics_list = [
    "DIVERSITY",
    "Answer_relevance",
    "conceptual_similarity"
]
metrics_config = {
    "diversity_config": {
        "threshold": 0.5,
        "custom_labels": ["string"],
        "label_thresholds": [0],
    },
    "conceptual_similarity_config": {
        "threshold": 0.5,
        "custom_labels": ["string"],
        "label_thresholds": [0],
    }
}
# inspeq_instance = Eval(API_KEY)
# result = inspeq_instance.evaluate_task(prompt, context, response, task_name, metrics_list, metrics_config)
# print(result)


payload = {
            "metrics_list": metrics_list,
            "input_data": {
                "llm_input_query": prompt,
                "llm_input_context": context,
                "llm_output": response,
            },
            "metrics_config": metrics_config or {},
        }