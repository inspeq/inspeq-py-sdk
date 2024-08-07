# Inspeq Python SDK

- **Website:** [Inspeq.ai](https://www.inspeq.ai)
- **Inspeq App:** [Inspeq App](https://platform.inspeq.ai)
- **Detailed Documentation:** [Inspeq Documentation](https://docs.inspeq.ai)

## Quickstart Guide

### Installation

Install the Inspeq SDK and python-dotenv using pip:

```bash
pip install inspeqai python-dotenv
```

The `python-dotenv` package is recommended for securely managing your environment variables, such as API keys.

### Obtain SDK API Key and Project Key

Get your API key and Project Key from the [Inspeq App](https://platform.inspeq.ai)

### Usage

Here's a basic example of how to use the Inspeq SDK with environment variables:

```python
import os
from dotenv import load_dotenv
from inspeq.client import InspeqEval

# Load environment variables
load_dotenv()

# Initialize the client
INSPEQ_API_KEY = os.getenv("INSPEQ_API_KEY")
INSPEQ_PROJECT_ID = os.getenv("INSPEQ_PROJECT_ID")
INSPEQ_API_URL = os.getenv("INSPEQ_API_URL")  # Required only for our on-prem customers

inspeq_eval = InspeqEval(inspeq_api_key=INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID)

# Prepare input data
input_data = [{
    "prompt": "What is the capital of France?",
    "response": "Paris is the capital of France.",
    "context": "The user is asking about European capitals."
}]

# Define metrics to evaluate
metrics_list = ["RESPONSE_TONE", "FACTUAL_CONSISTENCY", "ANSWER_RELEVANCE"]

try:
    results = inspeq_eval.evaluate_llm_task(
        metrics_list=metrics_list,
        input_data=input_data,
        task_name="capital_question"
    )
    print(results)
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

Make sure to create a `.env` file in your project root with your Inspeq credentials:

```
INSPEQ_API_KEY=your_inspeq_sdk_key
INSPEQ_PROJECT_ID=your_project_id
INSPEQ_API_URL=your_inspeq_backend_url
```

### Available Metrics 

```python
metrics_list = [
    "RESPONSE_TONE",
    "ANSWER_RELEVANCE",
    "FACTUAL_CONSISTENCY",
    "CONCEPTUAL_SIMILARITY",
    "READABILITY",
    "COHERENCE",
    "CLARITY",
    "DIVERSITY",
    "CREATIVITY",
    "NARRATIVE_CONTINUITY",
    "GRAMMATICAL_CORRECTNESS"
]
```

## Features

The Inspeq SDK provides a range of metrics to evaluate language model outputs:

1. **Response Tone:** Assesses the tone and style of the generated response.

2. **Answer Relevance:** Measures the degree to which the generated content directly addresses and pertains to the specific question or prompt provided by the user.

3. **Factual Consistency:** Measures the extent of the model hallucinating i.e. model is making up a response based on its imagination or response is grounded in the context supplied.

4. **Conceptual Similarity:** Measures the extent to which the model response aligns with and reflects the underlying ideas or concepts present in the provided context or prompt.

5. **Readability:** Assesses whether the model response can be read and understood by the intended audience, taking into account factors such as vocabulary complexity, sentence structure, and overall clarity.

6. **Coherence:** Evaluates how well the model generates coherent and logical responses that align with the context of the question.

7. **Clarity:** Assesses the response's clarity in terms of language and structure, based on grammar, readability, concise sentences and words, and less redundancy or diversity.

8. **Diversity:** Assesses the diversity of vocabulary used in a piece of text.

9. **Creativity:** Assesses the ability of the model to generate imaginative, and novel responses that extend beyond standard or expected answers.

10. **Narrative Continuity:** Measures the consistency and logical flow of the response throughout the generated text, ensuring that the progression of events remains coherent and connected.

11. **Grammatical Correctness:** Checks whether the model response adherence to the rules of syntax, is free from errors and follows the conventions of the target language.

## Advanced Usage

### Custom Configurations

You can provide custom configurations for metrics:

```python
metrics_config = {
    "response_tone_config": {
        "threshold": 0.5,
        "custom_labels": ["Negative", "Neutral", "Positive"],
        "label_thresholds": [0, 0.5, 0.7, 1]
    }
}

results = inspeq_eval.evaluate_llm_task(
    metrics_list=["RESPONSE_TONE"],
    input_data=input_data,
    task_name="custom_config_task",
    metrics_config=metrics_config
)
```

## Error Handling

The SDK uses custom exceptions for different types of errors:

- **APIError:** For API related issues
- **ConfigError:** For invalid config related issues
- **InputError:** For invalid input data

## Additional Resources

For detailed API documentation, visit [Inspeq Documentation](https://docs.inspeq.ai).
For support or questions, contact our support team through the Inspeq App.

## License

This SDK is distributed under the terms of the Apache License 2.0.
