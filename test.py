from inspeq.client import Evaluator


API_KEY=""
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


# print("\n c. response_tone is:")
# print(inspeq_instance.get_all_metrices(input_data))

inspeq_instance.get_all_metrices(input_data)
