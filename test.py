from inspeq.client import Evaluator
import time


API_KEY=""
inspeq_instance = Evaluator(sdk_api_key=API_KEY)


# for i, data_object in enumerate(data_objects, start=1):
#     input_data = {
#         "llm_input_query": data_object["llm_input_query"],
#         "llm_input_context": data_object["llm_input_context"],
#         "llm_output": data_object["llm_output"],
#     }
a=time.time()
input_data = {
           "llm_input_query": " ",
    "llm_input_context": "Cybersecurity is the practice of protecting computer systems, networks, and data from unauthorized access, attacks, and damage...",
    "llm_output": "Cybersecurity encompasses several fundamental concepts, including confidentiality, integrity, availability, authentication, and non-repudiation. Confidentiality refers to the protection of sensitive information from unauthorized access or disclosure, ensuring that only authorized individuals can access the data. Integrity involves maintaining the accuracy and consistency of data throughout its lifecycle, preventing unauthorized modifications or alterations. Availability ensures that systems and data are accessible and usable when needed, minimizing downtime and disruptions to operations. Authentication verifies the identity of users or entities attempting to access a system or resource, typically through credentials such as passwords, biometrics, or cryptographic keys. Non-repudiation provides proof of the origin or delivery of data and prevents parties from denying their involvement in a transaction or communication."
        }


print("Factual Consistency:", inspeq_instance.factual_consistency(input_data))
print("Answer Relevance:", inspeq_instance.answer_relevance(input_data))
print("Response Tone:", inspeq_instance.response_tone(input_data))
print("Grammatical Correctness:", inspeq_instance.grammatical_correctness(input_data))
print("Fluency:", inspeq_instance.fluency(input_data))
print("Do Not Use Keywords:", inspeq_instance.do_not_use_keywords(input_data))
print("Word Limit Test:", inspeq_instance.word_limit_test(input_data))
print("Conceptual Similarity:", inspeq_instance.conceptual_similarity(input_data))
print("Coherence:", inspeq_instance.coherence(input_data))
print("Readability:", inspeq_instance.readability(input_data))
b=time.time()
print(b-a)
