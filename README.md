# Inspeq Python SDK : inspeq-pysdk

Python SDK for Inspeq APIS.

### make venv and activate it

#### for linux based system

```sh
python3 -m venv venv

```

```sh
source venv/bin/actiavte

```

#### for windows

```sh
python3 -m venv venv
```

```sh
venv\Scripts\actiavte

```

### Installation

```sh
pip install inspeq-py-sdk
```

#### Features

- Evaluate Factual Consistency:
  Check if the generated text is consistent with known facts.

- Evaluate Grammatical Correctness:
  Assess the grammatical accuracy of the generated text.

- Evaluate Do Not Use Keywords:
  Identify and evaluate the use of specific keywords or phrases.

- Evaluate Fluency:

  Assess the overall smoothness and fluency of the generated text

- Evaluate Answer Relevance:

  Determine the relevance of the generated text in the context of a given query or

- Evaluate Word Limit Test:

  Check if the generated text adheres to specified word limits.

### Usage

#### Get API keys

Get your API keys from <a href="" target="_blank">Here</a>

#### Use api key to create your own script.

```py

#import client from Inseq
import os
from dotenv import load_dotenv
from client import Inspeq

# load env file and store your api key variable
load_dotenv()
API_KEY=os.getenv("YOUR_INSPEQ_SDK_API_KEY")

#initialization of Inspeq Instance
inspeq_instance = Inspeq(API_key)

# now use this instance to access functions provided by sdk

# Example input data
input_data = {
    "llm_input_query": "your_llm_input_query",
    "llm_input_context": "your_llm_input_context",
    "llm_output": "your_llm_output",
}

'''Note : Do not change the structure of input data keep the structure as it
is. Put your data at places of your_llm_input_context, your_llm_input_query
and your_llm_output to evaluate with the help of our evaluation metrices.

'''
inspeq_instance.evalaute_grammatical_correctness(input_data)
print("\n   grammatical_correctness is:")

```

### All Metrics provided by Inspeq sdk

```py

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

```




## TODO

How to user api key method

SSL enable-
