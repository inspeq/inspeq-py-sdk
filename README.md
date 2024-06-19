# Inspeqai Python SDK

- **Website:** [Inspeq.ai](https://www.inspeq.ai)
- **Inspeq App:** [Inspeq App](https://app.inspeq.ai)
- **Detailed Documentation:** [Inspeq Documentation](https://docs.inspeq.ai)

## Quickstart Guide

### Creating a Virtual Environment

To ensure a clean and isolated environment for your project, it’s recommended to create a virtual environment.

#### Linux/MacOS

1. Open a terminal.
2. Navigate to your project directory.
3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

#### Windows

1. Open a terminal.
2. Navigate to your project directory.
3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    venv\Scripts\activate
    ```

**Note:** Ensure your environment is activated every time you use the package.

### SDK Installation

Install the Inspeqai SDK using pip:

```sh
pip install inspeqai
```

### Obtain SDK API Keys

Get your API keys from [here](https://app.inspeq.ai/).

### Usage

Create a `main.py` file and use the following code snippet to get started:

```python
from inspeq.client import InspeqEval

# Initialization
API_KEY = "your_inspeq_sdk_key"
PROJECT_ID = "your_project_id"

from inspeq.client import InspeqEval

inspeq_eval = InspeqEval(inspeq_api_key=API_KEY, project_id=PROJECT_ID)

input_data = [{
    "llm_input_query": "string", 
    "llm_input_context": "string",  
    "llm_output": "string" 
}]

metrics_config = {
    "response_tone_config": {
        "threshold": 0.5,
        "custom_labels": [
            "Negative",
            "Neutral",
            "Positive"
        ],
        "label_thresholds": [
            0,
            0.5,
            0.7,
            1
        ]
    }
}

try:
    results = inspeq_eval.evaluate_llm_task(
        input_data=input_data,
        task_name="your_task_name",
        metrics_config=metrics_config,
        metrics_list=["response_tone"]
    )
    print(results)
except ValueError as e:
    print(e)

```

### All Metrics Provided by Inspeq SDK

Different metrics require different parameters. You can visit the [official documentation](https://docs.inspeq.ai/) for detailed information.

### Supported Features

**Metrics:**

- **Factual Consistency:** Ensures the precision and correctness of information in the generated text compared to the given context or anticipated factual knowledge.
- **Do Not Use Keywords:** Verifies that certain keywords are not present in the response.
- **Answer Relevance:** Assesses the alignment between the model's responses and the intended meaning of the input.
- **Word Limit Test:** Checks if the generated text adheres to specified word limits.
- **Response Tonality:** Analyzes the type of tone or overall sentiment highlighted in the response.
- **Conceptual Similarity:** Measures the semantic similarity or relatedness between the generated response and the provided context.
- **Coherence:** Evaluates the organization, structure, and ease of understanding of the generated text.
- **Readability:** Assesses if the generated text is appropriate for the target audience’s reading level.
- **Clarity:** Measures the clarity of the response in terms of language and structure.
- **Model Refusal:** Detects if the model responds with a refusal response when appropriate.
- **Data Leakage:** Identifies if the model response contains any personal information such as credit card numbers, phone numbers, emails, URLs, etc.
- **Creativity:** Evaluates the creativity of the generated content based on lexical diversity, contextual similarity, and hallucination score.
- **Diversity:** Measures the diversity of vocabulary used in the text.
- **Narrative Continuity:** Evaluates whether the generated response maintains coherence and logical flow with the preceding narrative.

---

### Additional Resources

For more detailed information and advanced usage, refer to the [Inspeq Documentation](https://docs.inspeq.ai/).

By following these instructions, you will be able to efficiently set up and utilize the Inspeqai Python SDK. If you have any questions or need further assistance, please refer to the official documentation or contact support.

---

This version includes detailed steps for setting up the environment, installing the SDK, and using it, as well as a comprehensive list of features supported by the Inspeq SDK. It also highlights the importance of the `project_id` parameter.