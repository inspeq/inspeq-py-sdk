## Project Description
Inspeqai python SDK
## Inspeq
##  More detail 0fficial Documentation
Click <a href="https://docs.inspeq.ai/" target="_blank">Here</a>

### Creating a Virtual Environment in Linux and Windows

### Linux OS / MAC OS

### Using venv (Python 3)

1. Open a terminal.
2. Navigate to the directory where you want to create the virtual environment.
3. Run the following command:
```bash
   python3 -m venv venv
```
#### Activate it 
```bash
  source venv/bin/activate

```
### windows

1. Open a terminal.
2. Navigate to the directory where you want to create the virtual environment.
3. Run the following command:
```bash
   python -m venv venv
```
#### Activate it 
```bash
venv\Scripts\activate
```
#### Make sure your environment is activated everytime you use package


### SDK Installation 
Enter below Command  in terminal

```sh
pip install inspeqai
```

### Get SDK API keys
Get your API keys from <a href="https://app.inspeq.ai/" target="_blank">Here</a>

### Usage

Create main.py and you can use below code snippet
```py

from inspeq.client import Evaluator

#initialization 
API_KEY = "your_sdk_api_key"
inspeq_instance = Evaluator(sdk_api_key=API_KEY)

# Example input data
input_data = {
    "llm_input_query": "your_llm_input_query",
    "llm_input_context": "your_llm_input_context",
    "llm_output": "your_llm_output",
}

'''Note : Do not change the structure of input data keep the structure as it
is. Put your data at places of your_llm_input_context, your_llm_input_query
and your_llm_output .

'''
print("\n   grammatical_correctness is:")
print(inspeq_instance.grammatical_correctness(input_data))
#get all metrices in one function

print(inspeq_instance.get_all_metrices(input_data))

```

### All Metrics provided by Inspeq sdk

```py
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
    print("Clarity:", inspeq_instance.clarity(input_data))
    print("Get all metrics:", inspeq_instance.get_all_metrics(input_data))

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

- Coherence:
  Coherence metric evaluates how well the model generates coherent and logical responses that align with the context of the question.

- Readibility:
  It tells how easy is to read and understand the llm output

- Clarity:
  Clarity here refers to the response’s clarity in terms of language and structure. It's a subjective metric and is based on grammar, readability, concise sentences and words, and less redundancy or diversity at the moment. To add contextual clarity, we need to add topic coherence, response relevance, and word ambiguity.

- Get_all_metrics:
  This is the super metric it will give you result in one go of all metrics but remember it is heavy metrics so it will take time .Right now it is giving all 11 metrics in response

## Official Documentation
Click <a href="https://docs.inspeq.ai/" target="_blank">Here</a>