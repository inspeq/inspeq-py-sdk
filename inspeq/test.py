from sdk import Evaluator
from dataobjects import data_objects


API_KEY="0be2911254c67aa338a82c9ca0d22c77"
inspeq_instance = Evaluator(API_KEY)


# for i, data_object in enumerate(data_objects, start=1):
#     input_data = {
#         "llm_input_query": data_object["llm_input_query"],
#         "llm_input_context": data_object["llm_input_context"],
#         "llm_output": data_object["llm_output"],
#     }

input_data =  {
        "llm_input_query": "What weather factor produces a great variance in local climates in the Seattle area?",
        "llm_input_context": "From 1981 to 2010, the average annual precipitation measured at Seattle...",
        "llm_output": "The presence of the Olympic Mountains is the weather factor that produces...",
    }


print("\n c. response_tone is:")
print(inspeq_instance.response_tone(input_data))

print("\n g. word_limit_test is:")
print(inspeq_instance.word_limit_test(input_data))
