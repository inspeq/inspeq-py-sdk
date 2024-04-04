API_KEY = ""

    
from inspeq.client import InspeqEval


from inspeq.client import InspeqEval



inspeq_eval = InspeqEval(inspeq_api_key= API_KEY)


input_data = {
           "response": "Paris is the capital of France."
       }


config_input= {
       "threshold": 0.5,
       "custom_labels": ["custom_label_1","custom_label_2"],
       "label_thresholds": [0,0.5, 1],
   }


results = inspeq_eval.readability(input_data= input_data ,config_input= config_input ,task_name="your_task_name")


print(results)