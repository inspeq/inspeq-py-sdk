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
API_KEY = "your_sdk_api_key"
inspeq_instance = Evaluator(sdk_api_key=API_KEY)

# Example input data
input_data={
    "prompt":"llm_prompt",
     "response":" llm_output "
  }

'''Note : Do not change the structure of input data keep the structure as it
is. Put your data at places of llm_prompt, llm_output
and your_llm_output .

'''
print("Word limit test :", inspeq_instance.word_limit_test(input_data))


```

#### Get all metrics

```py

from inspeq.client import Evaluator

#initialization
API_KEY = "your_sdk_api_key"
inspeq_instance = Evaluator(sdk_api_key=API_KEY)

# Example input data
# three parameters are required for get_all_metrics you can see below ,do not change structure inside the input data
input_data={
    "prompt":"your_llm_prompt",
    "context":"your_llm_context",
     "response":"your_llm_output "
  }

'''Note : Do not change the structure of input data keep the structure as it
is you need to include prompt,context,response as it is . Put your data at places of your_llm_prompt, your_llm_context
and your_llm_output .

'''
#get all metrics in one function

print(inspeq_instance.get_all_metrics(input_data))

```

After you run the file all metrics result will print in your terminal or output window.

### All Metrics provided by Inspeq sdk

Different metrics required different parameters you can visit official documentation

Click <a href="https://docs.inspeq.ai/" target="_blank">Here</a>

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

### Supported Features

Metrices:

- Factual Consistency:
  Factual Consistency (FC) pertains to the precision and correctness of information articulated in text produced by Large Language Models (LLMs). It involves the comparison of generated information with the given context, input, or anticipated factual knowledge.

- Grammatical Correctness:
  Assess the grammatical accuracy of the generated text.

- Do Not Use Keywords:
  Identify and evaluate the use of specific keywords or phrases.

- Answer Fluency:
  Fluency refers to the ability of the LLM to generate text that is grammatically correct, natural-sounding, and easy to read.

- Answer Relevance:
  Determine the relevance of the generated text in the context of a given query or

- Word Limit Test:
  Check if the generated text adheres to specified word limits.

- Response Tonality:
  Tonality refers to the type of tone or overall sentiment highlighted in the response.

- Conceptual Similarity:
  This refers to the semantic similarity or relatedness between response generated and provided context.

- Coherence:
  Coherence metric evaluates the ability of the LLM to generate text that is organized, well-structured, and easy to understand.

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

- Get_all_metrics:
  This will provide result of all metrics.
