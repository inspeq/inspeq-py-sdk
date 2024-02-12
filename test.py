from inspeq.client import Evaluator


API_KEY=""
inspeq_instance = Evaluator(sdk_api_key=API_KEY,API_URL="")


# for i, data_object in enumerate(data_objects, start=1):
#     input_data = {
#         "llm_input_query": data_object["llm_input_query"],
#         "llm_input_context": data_object["llm_input_context"],
#         "llm_output": data_object["llm_output"],
#     }

input_data =  {
        "llm_input_query": "What weather factor produces a great variance in local climates in the Seattle area?",
        "llm_input_context": "From 1981 to 2010, the average annual precipitation measured at Seattle was approximately 37.49 inches. However, despite this relatively consistent average, the distribution of rainfall across the region varies significantly due to several influential weather factors. These factors include the presence of the Olympic Mountains, which play a crucial role in shaping Seattle's microclimates. The Olympic Mountains act as a barrier to weather systems originating from the Pacific Ocean, leading to the formation of distinct precipitation patterns known as the 'rain shadow effect.' On the windward side of the mountains, particularly closer to the coast, there tends to be higher precipitation rates due to the moist air masses coming from the ocean. However, as these air masses encounter the Olympic Mountains, they are forced to rise, cool, and release moisture, resulting in heavier precipitation on the windward side. Conversely, the leeward side experiences much drier conditions as the air descends and warms, creating a rain shadow effect. This stark difference in precipitation patterns contributes significantly to the variability in local climates across the Seattle area. Additionally, the proximity to Puget Sound and the Pacific Ocean also influences weather patterns, including temperature regulation and the formation of fog and coastal breezes, further adding to the complexity and variability of Seattle's microclimates.",
        "llm_output": "The presence of the Olympic Mountains is one of the primary weather factors that produces a significant variance in local climates within the Seattle area. These mountains act as a barrier to weather systems coming from the Pacific Ocean, leading to what is known as the 'rain shadow effect.' On the western side of the mountains, particularly closer to the coast, there tends to be higher precipitation rates due to the moist air masses originating from the ocean. However, as these air masses encounter the Olympic Mountains, they are forced to rise, cool, and release moisture, resulting in heavier precipitation on the windward side of the mountains. Conversely, the leeward side experiences much drier conditions as the air descends and warms, creating a rain shadow effect. This stark difference in precipitation patterns contributes significantly to the variability in local climates across the Seattle area. Additionally, the proximity to Puget Sound and the Pacific Ocean also influences weather patterns, including temperature regulation and the formation of fog and coastal breezes, further adding to the complexity and variability of Seattle's microclimates.",
    }


# print("\n c. response_tone is:")
# print(inspeq_instance.get_all_metrices(input_data))

result=inspeq_instance.get_all_metrics(input_data)

print(result)
