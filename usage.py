# Quick Start Guide for Inspeq Python SDK

## Installation

1. **Create a Virtual Environment:**

   For Linux-based systems:
   ```bash
   python3 -m venv venv
   source venv/bin/activate


For Windows:

bash

python3 -m venv venv
venv\Scripts\activate

    Install the SDK:

    Use pip to install the Inspeq Python SDK:

    bash

pip install inspeq-py-sdk

Initialize the SDK:

python

    import os
    from dotenv import load_dotenv
    from client import Inspeq

    # Load environment variables and store your API key
    load_dotenv()
    API_KEY = os.getenv("YOUR_INSPEQ_SDK_API_KEY")

    # Initialization of Inspeq Instance
    inspeq_instance = Inspeq(API_KEY)

Usage Example

python

# Example input data
input_data = {
    "llm_input_query": "your_llm_input_query",
    "llm_input_context": "your_llm_input_context",
    "llm_output": "your_llm_output",
}

# Evaluate grammatical correctness
inspeq_instance.evaluate_grammatical_correctness(input_data)
print("\n   grammatical_correctness is:")

# ... (continue with other metrics)

Explore the available metrics and customize them based on your evaluation needs.
