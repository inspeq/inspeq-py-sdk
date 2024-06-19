API_KEY = "in-5e5fad8426f3ae232f981191dbfbc50c"
PROJECT_ID = "d0b9e1f8-4ef4-4306-b6ce-f61986dc6eef"

from inspeq.client import InspeqEval

inspeq_eval = InspeqEval(inspeq_api_key=API_KEY, project_id=PROJECT_ID)

input_data = [{
    "llm_input_query": "string", 
    "llm_input_context": "string",  
    "llm_output": "string" 
}]
metrics_config = {
    "response_tone_config": {
        "threshold": 0.5,
        "custom_labels": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "label_thresholds": [
            0,
            0.5,
            0.7,
            1
        ]
    }
}

try:
    results = inspeq_eval.evaluate_llm_task(
        input_data=input_data,
        task_name="your_task_name",
        metrics_config=metrics_config,
        metrics_list=["response_tone"]
    )
    print(results)
except ValueError as e:
    print(e)