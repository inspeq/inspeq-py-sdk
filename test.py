API_KEY = "in-f579f248eb74d2bbf5c4fa40bac03298"
# API_KEY = "in-b2981ee6612559e880a72b49bebfe897"



data = [{
        "response": "response1",
        "context" : "this",
        "prompt":"this is prompt yeah"
    }
    
]


from inspeq.client import InspeqEval
metrics_list = [ "response_tone"]
inspeq_eval = InspeqEval(inspeq_api_key= API_KEY)

metrics_config = {
    "response_tone_config": {
        "threshold": 0.5,
        "custom_labels": ["string", "ss"],
        "label_thresholds": [0,0.5,1]
    }
}

results = inspeq_eval.evaluate_llm_task(data= data , metrics_list= metrics_list)

print(results)