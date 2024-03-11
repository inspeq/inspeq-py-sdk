from inspeq.client import Evaluator


API_KEY = "sdk_key"
inspeq_instance = Evaluator(sdk_api_key=API_KEY)

input_data={
    "prompt":"string",
     "response":" string "
  }

print("Word limit test :", inspeq_instance.word_limit_test(input_data))




