# Inspeq Python SDK : inspeq-py-sdk

Python SDK for Inspeq APIS.

### make venv and activate it

#### for linux based system

```sh
python3 -m venv venv

```

```sh
source venv/bin/activate

```

#### for windows

```sh
python3 -m venv venv
```

```sh
venv\Scripts\activate

```

### Installation

```sh
pip install inspeq-py-sdk
```

#### Features
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

INSPEQ_SDK_API_KEY=os.getenv("YOUR_INSPEQ_SDK_API_KEY")

#initialization of Inspeq Instance
inspeq_instance = Inspeq(sdk_api_key=INSPEQ_SDK_API_KEY)

# now use this instance to access functions provided by sdk

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
print(inspeq_instance.grammatical_correctness(input_data))
print("\n   grammatical_correctness is:")

```

### All Metrics provided by Inspeq sdk

```py

print("\n  a. factual_consistency is:")
print(inspeq_instance.factual_consistency(input_data))

print("\n b. answer_relevance is:")
print(inspeq_instance.answer_relevance(input_data))

print("\n c. response_tone is:")
print(inspeq_instance.response_tone(input_data))

print("\n  d. grammatical_correctness is:")
print(inspeq_instance.grammatical_correctness(input_data))

print("\n e. fluency is:")
print(inspeq_instance.fluency(input_data))

print("\n f. do_not_use_keywords is:")

print(inspeq_instance.do_not_use_keywords(input_data))

print("\n g. word_limit_test is:")
print(inspeq_instance.word_limit_test(input_data))

print("\n h.  conceptual_similarity is:")
print(inspeq_instance.conceptual_similarity(input_data))

```