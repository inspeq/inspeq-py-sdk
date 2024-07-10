import os
import pytest
import json
import base64
from dotenv import load_dotenv
from inspeq.client import InspeqEval, APIError

# Load environment variables
load_dotenv()

INSPEQ_API_KEY = os.getenv("INSPEQ_API_KEY")
INSPEQ_PROJECT_ID = os.getenv("INSPEQ_PROJECT_ID")
INSPEQ_API_URL = os.getenv("INSPEQ_API_URL")

def generate_random_task_name(prefix="task", length=8):
    """Generate a random task name with a given prefix and length."""
    import random
    import string
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{prefix}_{random_string}"

def metric_name_matches(actual_name, expected_names):
    """Check if the actual metric name matches any of the expected names."""
    actual_name = actual_name.replace('_EVALUATION', '').lower()
    return any(expected.lower() in actual_name for expected in expected_names)


@pytest.fixture
def random_task_name():
    return generate_random_task_name()

@pytest.fixture
def inspeq_client():
    return InspeqEval(inspeq_api_key= INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID, inspeq_api_url=INSPEQ_API_URL)

# customizable_metrics
def test_evaluate_llm_task_more_thresholds(inspeq_client, random_task_name):
    customizable_metrics = ["ANSWER_FLUENCY","GRAMMATICAL_CORRECTNESS", "RESPONSE_TONE", "ANSWER_RELEVANCE", "FACTUAL_CONSISTENCY", "CONCEPTUAL_SIMILARITY", "READABILITY", "COHERENCE", "CLARITY", "DIVERSITY", "CREATIVITY"]
    input_data = [
        {
            "prompt": "What is the capital of France?",
            "response": "Paris is the capital of France.",
            "context": "The user is asking about European capitals."
        }
    ]
    
    try:
        result = inspeq_client.evaluate_llm_task(
            metrics_list=customizable_metrics,
            input_data=input_data,
            task_name=random_task_name
        )
        print(f"More thresholds task result: {json.dumps(result, indent=2)}")
        
        assert isinstance(result, dict)
        assert result["status"] == 200
        assert isinstance(result["data"], list)
        
        for item in result["data"]:
            assert item["metric_name"] in [f"{metric}_EVALUATION" for metric in customizable_metrics]
            config = json.loads(base64.b64decode(item["metrics_config"]))
            assert len(config["label_thresholds"]) == len(config["custom_labels"]) + 1
        
    except APIError as e:
        pytest.fail(f"API Error occurred: {str(e)}")

# binary_metrics
def test_evaluate_llm_task_equal_thresholds(inspeq_client, random_task_name):
    
    binary_metrics = [ "DATA_LEAKAGE", "DO_NOT_USE_KEYWORDS", "MODEL_REFUSAL",  "NARRATIVE_CONTINUITY", "WORD_COUNT_LIMIT"] 
    
    input_data = [
        {
            "prompt": "Summarize the benefits of exercise in 50 words.",
            "response": "Exercise improves cardiovascular health, strengthens muscles, enhances mental well-being, boosts energy levels, aids weight management, reduces disease risks, improves sleep quality, increases longevity, enhances cognitive function, and promotes overall quality of life.",
            "context": "The user is writing a short article about health."
        }
    ]
    
    try:
        result = inspeq_client.evaluate_llm_task(
            metrics_list=binary_metrics,
            input_data=input_data,
            task_name=random_task_name
        )
        print(f"Equal thresholds task result: {json.dumps(result, indent=2)}")
        
        assert isinstance(result, dict)
        assert result["status"] == 200
        assert isinstance(result["data"], list)
        
        for item in result["data"]:
            assert metric_name_matches(item["metric_name"], binary_metrics), \
                f"Unexpected metric name: {item['metric_name']}"
            config = json.loads(base64.b64decode(item["metrics_config"]))
            assert len(config["label_thresholds"]) == len(config["custom_labels"]), \
                f"Mismatch in label_thresholds and custom_labels for {item['metric_name']}"
        
    except APIError as e:
        pytest.fail(f"API Error occurred: {str(e)}")
        

# special metrics
def test_evaluate_llm_task_special_cases(inspeq_client, random_task_name):
    metrics_list = ["CREATIVITY", "DIVERSITY"]
    input_data = [
        {
            "prompt": "Write a creative short story about a time-traveling scientist.",
            "response": "Dr. Amelia Chronos adjusted her temporal goggles, heart racing as she prepared to make her first jump through time. The lab hummed with energy as she activated the chrono-field generator. In a flash of blue light, she vanished from 2023 and reappeared in ancient Egypt. To her amazement, she found herself face-to-face with Cleopatra, who mistook her for a goddess from the future. Amelia's scientific curiosity battled with her ethical training as she considered the potential consequences of interacting with such a pivotal historical figure. In the end, she chose to observe silently, gathering invaluable data about the past while safeguarding the timeline. As she returned to her own time, Amelia realized that the true power of time travel lay not in changing history, but in understanding it.",
            "context": "The user is participating in a creative writing contest."
        }
    ]
    
    try:
        result = inspeq_client.evaluate_llm_task(
            metrics_list=metrics_list,
            input_data=input_data,
            task_name=random_task_name
        )
        print(f"Special cases task result: {json.dumps(result, indent=2)}")
        
        assert isinstance(result, dict)
        assert result["status"] == 200
        assert isinstance(result["data"], list)
        
        for item in result["data"]:
            assert item["metric_name"] in [f"{metric}_EVALUATION" for metric in metrics_list]
            config = json.loads(base64.b64decode(item["metrics_config"]))
            assert len(config["label_thresholds"]) == 3
            assert len(config["custom_labels"]) == 2
        
    except APIError as e:
        pytest.fail(f"API Error occurred: {str(e)}")
