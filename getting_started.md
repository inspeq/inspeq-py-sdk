# Getting Started with Inspeq Python SDK

## Overview

The Inspeq Python SDK, `inspeq-py-sdk`, empowers developers with a comprehensive set of tools for evaluating generated text. Whether you're assessing factual consistency, grammatical correctness, or other linguistic aspects, this SDK simplifies the evaluation process. It integrates seamlessly into your Python projects, providing a robust solution for text evaluation.

## Installation

To install the Inspeq Python SDK and the recommended `python-dotenv` package for managing environment variables, use pip:

```bash
pip install inspeqai python-dotenv
```

## Obtaining API Keys

To start using the Inspeq Python SDK, you need API keys. Follow these steps to obtain them:

1. Visit the [Inspeq App](https://platform.inspeq.ai).
2. Sign in or create a new account if you haven't already.
3. Generate your unique API key and Project key from the provided interface.

Remember to keep your API key and Project key secure. They serve as the authentication tokens for accessing the Inspeq APIs from your scripts.

## Integration

The SDK seamlessly integrates into your Python projects, providing a straightforward way to incorporate advanced text evaluation capabilities. Here's a basic example of how to use the SDK:

```python
import os
from dotenv import load_dotenv
from inspeq.client import InspeqEval

# Load environment variables
load_dotenv()

# Initialize the client
INSPEQ_API_KEY = os.getenv("INSPEQ_API_KEY")
INSPEQ_PROJECT_ID = os.getenv("INSPEQ_PROJECT_ID")
INSPEQ_API_URL = os.getenv("INSPEQ_API_URL")  # Required only for on-prem customers

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

## Environment Variables

Create a `.env` file in your project root with your Inspeq credentials:

```
INSPEQ_API_KEY=your_inspeq_sdk_key
INSPEQ_PROJECT_ID=your_project_id
INSPEQ_API_URL=your_inspeq_backend_url
```

## Next Steps

For more detailed information on available metrics, advanced usage, and best practices, refer to the [full documentation](https://docs.inspeq.ai).

If you encounter any issues or have questions, don't hesitate to reach out to our support team through the Inspeq App.
