from inspeq.client import Evaluator


API_KEY=""
inspeq_instance = Evaluator(sdk_api_key=API_KEY)


# for i, data_object in enumerate(data_objects, start=1):
#     input_data = {
#         "llm_input_query": data_object["llm_input_query"],
#         "llm_input_context": data_object["llm_input_context"],
#         "llm_output": data_object["llm_output"],
#     }

input_data = {
            "llm_input_context": "Seattle is known for its wet  to its location in the Pacific Northwest region of the United States. From 1981 to 2010, the average annual precipitation measured at Seattle-Tacoma International Airport was 37.49 inches (952 mm). This significant amount of rainfall contributes to lush vegetation and a generally green landscape throughout the year. The city's proximity to the Pacific Ocean also influences its weather patterns, with maritime air masses bringing moisture-laden air inland. However, despite the overall wetness of the climate, there is a great variance in local climates within the Seattle area.",
            "llm_input_query": "What factors contribute to the variance in local climates in the Seattle area?",
            "llm_output": "Several factors contribute to the variance in local climates in the Seattle area. One significant factor is the presence of the Olympic Mountains to the west of the city. These mountains act as a barrier, causing the 'rain shadow effect' where the western slopes receive abundant rainfall while the eastern slopes experience much drier conditions. Additionally, Seattle's proximity to Puget Sound and other bodies of water can create microclimates, with areas closer to the water experiencing milder temperatures due to the moderating influence of the water. Furthermore, elevation plays a role, with higher elevations generally being cooler and receiving more precipitation compared to lower-lying areas. Urban heat island effects can also impact local climates, with downtown areas typically being warmer than surrounding suburbs and rural areas.",
        }


print("\n c. response_tone is:")
print(inspeq_instance.factual_consistency(input_data))

inspeq_instance.get_all_metrices(input_data)
