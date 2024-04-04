# Inspeqai python SDK

- **Website:** https://www.inspeq.ai
- **Inspeq app:** https://app.inspeq.ai
- **Detailed Documentation:** https://docs.inspeq.ai

## Quikstart

### Create a Virtual Environment in Linux and Windows

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

Enter below Command in terminal

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
API_KEY = "your_inspeq_sdk_key"

from inspeq.client import InspeqEval

input_data = {
       "prompt":"What is the capital of France?",
       "response": "Paris is the capital of France",
       "context" : "Paris is the capital of France and its largest city"
   }

'''Note : Do not change the structure of input data keep the structure as it
is. Put your data at places of llm_prompt, llm_output
and your_llm_output .

'''
results = inspeq_eval.diversity(input_data= input_data  ,task_name="testing_part_1")
print(results)


```

### All Metrics provided by Inspeq sdk

Different metrics required different parameters you can visit official documentation

Click <a href="https://docs.inspeq.ai/" target="_blank">Here</a>

### Supported Features

Metrices:

- Factual Consistency:
  Factual Consistency (FC) pertains to the precision and correctness of information articulated in text produced by Large Language Models (LLMs). It involves the comparison of generated information with the given context, input, or anticipated factual knowledge.

- Do Not Use Keywords:
  Test the List of keywords that should not be present in the response.
  
- Answer Relevance:
  Answer Relevance assesses the alignment between the model's responses and the intended meaning of the input.

- Word Limit Test:
  Check if the generated text adheres to specified word limits.

- Response Tonality:
  Tonality refers to the type of tone or overall sentiment highlighted in the response.

- Conceptual Similarity:
  This refers to the semantic similarity or relatedness between response generated and provided context.

- Coherence:
  The ability of the LLM to generate text that is organized, well-structured, and easy to understand.

- Readibility:
  Readability scores help assess whether the LLM’s generated text is appropriate for the target audience’s reading level.

- Clarity:
  Clarity is a subjective metric and refers to the response’s clarity in terms of language and structure.

- Model Refusal:
  Model refusal detects whether the model responds with a refusal response or not. Example of a refusal response - "I'm sorry, but I cannot provide you with a credit card number. It is against ethical and legal guidelines to share such sensitive information. If you have any other questions or need assistance with something else, feel free to ask."

- Data Leakage:
  Data leakage detects whether the model response contains any personal information such as credit card numbers, phone numbers, emails, urls etc.

- Creativity:
  Creativity is also a subjective concept, especially in AI-generated content. LLMs can be very creative but the results are mostly evaluated by humans. For our story generation and document summarization use cases, we define this metric as a combination of different metrics that could provide a more comprehensive evaluation. We use lexical diversity score, contextual similarity score and hallucination score to evaluate creativity.

- Diversity:
  Lexical diversity metrics assess the diversity of vocabulary used in a piece of text. Higher lexical diversity generally indicates a broader range of words and can contribute to more natural-sounding language.

- Narrative Continuity:
  Narrative continuity metric is a measure that evaluates whether a generated response maintains coherence and logical flow with the preceding narrative, without introducing abrupt or illogical shifts (ex.- story jumps). It analyzes factors like topic consistency, event/character continuity, and overall coherence to detect discontinuities in the narrative.
