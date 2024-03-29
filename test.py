from inspeq.client import Evaluator
from inspeq.client import Eval

# old way to call th metrics
API_KEY = "in-f579f248eb74d2bbf5c4fa40bac03298"
inspeq_instance = Evaluator(sdk_api_key=API_KEY)

inspeq_instance = Evaluator(sdk_api_key=API_KEY)


input_data = {
            "response": "Paris is the capital of France."
        }

config_input= {
        "threshold": 0.5,
        "custom_labels": ["custom_label_1","custom_label_2"],
        "label_thresholds": [0,1],
    }


print("Model Refusal:", inspeq_instance.response_tone(input_data = input_data,config_input=config_input, task_name="your_task_name"))



# New  Eval Testing

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
inspeq_instance = Eval(API_KEY)
result = inspeq_instance.evaluate_task(prompt, context, response, task_name, metrics_list, metrics_config)
print(result)


