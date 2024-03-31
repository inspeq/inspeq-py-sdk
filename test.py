# from inspeq.client import Evaluator
from inspeq.client import Evaluator

API_KEY = "in-f579f248eb74d2bbf5c4fa40bac03298"

prompt = "query_text"
context = "context_text"  
response = "output_text"  
task_name = "abc" 

metrics_list = [
    "model_refusal",
    "Answer_relevance",
    "conceptual_similarity"
]
metrics_config = {
    "model_refusal_config": {
        "threshold": 0.5,
        "custom_labels": ["string","ss"],
        "label_thresholds": [0,1],
    },
    "conceptual_similarity_config": {
        "threshold": 0.5,
        "custom_labels": ["string"],
        "label_thresholds": [0],
    }
}
inspeq_instance = Evaluator(API_KEY, api_url="https://stage.inspeq.ai")
result = inspeq_instance.eval(prompt, context, response, task_metric_list=metrics_list, task_metric_config=metrics_config)
print(result)


