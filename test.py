# API_KEY = "in-f579f248eb74d2bbf5c4fa40bac03298"
API_KEY = "in-db252abf651a3c7fe70a3b093f17e970"



# data = [{
#         "response": "response1",
#         "context" : "this",
#         "prompt":"this is prompt yeah"
#     }
    
# ]

data = {
        "response": "response1",
        "context" : "this",
        "prompt":"this is prompt yeah"
    }
    
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

config_input=  {
    "threshold": 0.5,
    "custom_labels": [
      "strisssssssssssssssssssng"
    ],
    "label_thresholds": [
      0,1
    ]
  }


results = inspeq_eval.clarity(input_data= data ,config_input= config_input)

print(results)