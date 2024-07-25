# Inspeq Python SDK

- **Website:** [Inspeq.ai](https://www.inspeq.ai)
- **Inspeq App:** [Inspeq App](https://platfom.inspeq.ai)
- **Detailed Documentation:** [Inspeq Documentation](https://docs.inspeq.ai)

## Quickstart Guide

### Installation

Install the Inspeq SDK using pip:

```bash
pip install inspeqai
```

### Obtain SDK API Key and Project key 

Get your API keys from the [Inspeq App](https://platfom.inspeq.ai)

### Usage
Here's a basic example of how to use the Inspeq SDK:


```
from inspeq.client import InspeqEval

# Initialize the client
INSPEQ_API_KEY = "your_inspeq_sdk_key"
INSPEQ_PROJECT_ID = "your_project_id"
INSPEQ_API_URL = "your_inspeq_backend_url" # Required only for our on-prem customers


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


## Features

The Inspeq SDK provides a range of metrics to evaluate language model outputs:

1. **Response Tone:** Analyzes the overall sentiment of the response.
2. **Factual Consistency:** Checks the accuracy of information against the given context.
3. **Answer Relevance:** Assesses how well the response addresses the input query.
4. **Conceptual Similarity:** Measures semantic similarity between the response and context.
5. **Readability:** Evaluates the complexity and readability of the text.
6. **Coherence:** Assesses the logical flow and organization of the response.
7. **Clarity:** Measures how clear and understandable the response is.
8. **Do Not Use Keywords:** Checks for the presence of specified keywords.
9. **Word Count Limit:** Verifies if the response adheres to specified word limits.
10. **Model Refusal:** Detects if the model appropriately refuses to answer certain queries.
11. **Data Leakage:** Identifies potential leakage of sensitive information.
12. **Creativity:** Evaluates the originality and inventiveness of the response.
13. **Diversity:** Measures the variety of vocabulary and concepts used.
14. **Narrative Continuity:** Checks if the response maintains a consistent narrative.

## Advanced Usage
### Custom Configurations

You can provide custom configurations for metrics:

```
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

### The SDK uses custom exceptions for different types of errors:


 **APIErrory:** For API related issues
 **ConfigError:** For invalid  config related issues
 **InputError:** For invalid input data


## Additional Resources

For detailed API documentation, visit [Inspeq Documentation](https://docs.inspeq.ai).
For support or questions, contact our support team through the Inspeq App.


## License

This SDK is distributed under the terms of the Apache License 2.0.
