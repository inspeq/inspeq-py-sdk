API_KEY = "in-5e5fad8426f3ae232f981191dbfbc50c"
PROJECT_ID = "d0b9e1f8-4ef4-4306-b6ce-f61986dc6eef"

from inspeq.client import InspeqEval




inspeq_eval = InspeqEval(inspeq_api_key= API_KEY, project_id =PROJECT_ID )


input_data={
   "context": "Paris is the capital of France and its largest city.",
   "response":"Paris is the capital of France."
 }


config_input= {
       "threshold": 0.5,
       "custom_labels": ["custom_label_1","custom_label_2"],
       "label_thresholds": [0,0.5, 1],
   }




results = inspeq_eval.factual_consistency(input_data= input_data ,config_input= config_input ,task_name="your_task_name")


print(results)




