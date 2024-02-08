## Project Description

### Inspeq

### Installation

```sh
pip install inspeqai
```

### Get API keys

Get your API keys from <a href="https://app.inspeq.ai/" target="_blank">Here</a>


### Usage

```py

from inspeq.client import Evaluator


#initialization 
inspeq_eval = Evaluator(sdk_api_key="YOUR_INSPEQ_API_KEY")


# Example input data
input_data = {
    "llm_input_query": "your_llm_input_query",
    "llm_input_context": "your_llm_input_context",
    "llm_output": "your_llm_output",
}

'''Note : Do not change the structure of input data keep the structure as it
is. Put your data at places of your_llm_input_context, your_llm_input_query
and your_llm_output to  with the help of our evaluation metrices.

'''
print("\n   grammatical_correctness is:")
print(inspeq_eval.grammatical_correctness(input_data))


```

### All Metrics provided by Inspeq sdk

```py

print("\n  a. factual_consistency is:")
print(inspeq_eval.factual_consistency(input_data))

print("\n b. answer_relevance is:")
print(inspeq_eval.answer_relevance(input_data))

print("\n c. response_tone is:")
print(inspeq_eval.response_tone(input_data))

print("\n  d. grammatical_correctness is:")
print(inspeq_eval.grammatical_correctness(input_data))

print("\n e. fluency is:")
print(inspeq_eval.fluency(input_data))

print("\n f. do_not_use_keywords is:")

print(inspeq_eval.do_not_use_keywords(input_data))

print("\n g. word_limit_test is:")
print(inspeq_eval.word_limit_test(input_data))

print("\n h.  conceptual_similarity is:")
print(inspeq_eval.conceptual_similarity(input_data))

```



###  Supported Features 
Metrices: 

-  Factual Consistency:
  Check if the generated text is consistent with known facts.

-  Grammatical Correctness:
  Assess the grammatical accuracy of the generated text.

-  Do Not Use Keywords:
  Identify and evaluate the use of specific keywords or phrases.

-  Fluency:
  Assess the overall smoothness and fluency of the generated text

-  Answer Relevance:
  Determine the relevance of the generated text in the context of a given query or

-  Word Limit Test:
  Check if the generated text adheres to specified word limits.

-  Response Tone:
  Assess the tone and style of the generated response.
  
-  Conceptual Similarity:
  Measure how closely the generated text aligns with the intended conceptual content.

