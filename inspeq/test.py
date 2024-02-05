from client import Inspeq
from dataobjects import data_objects
import os
from dotenv import load_dotenv
load_dotenv()


API_KEY=os.getenv("YOUR_INSPEQ_SDK_API_KEY")
inspeq_instance = Inspeq(API_KEY)


for i, data_object in enumerate(data_objects, start=1):
    input_data = {
        "llm_input_query": data_object["llm_input_query"],
        "llm_input_context": data_object["llm_input_context"],
        "llm_output": data_object["llm_output"],
    }
    print("evaluation no: ", i)
    print("\n  a. factual_consistency is:")
    inspeq_instance.evaluate_factual_consistency(input_data)

    print("\n b. answer_relevance is:")
    inspeq_instance.evalaute_answer_relevance(input_data)

    print("\n c. response_tone is:")
    inspeq_instance.evaluate_response_tone(input_data)

    print("\n  d. grammatical_correctness is:")
    inspeq_instance.evalaute_grammatical_correctness(input_data)

    print("\n e. fluency is:")
    inspeq_instance.evalaute_fluency(input_data)

    print("\n f. do_not_use_keywords is:")

    inspeq_instance.evalaute_do_not_use_keywords(input_data)

    print("\n g. word_limit_test is:")
    inspeq_instance.evaluate_word_limit_test(input_data)

    print("\n h.  conceptual_similarity is:")
    inspeq_instance.evaluate_conceptual_similarity(input_data)

    print("\n")