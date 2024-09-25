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

@pytest.fixture
def random_task_name():
    return generate_random_task_name()

@pytest.fixture
def inspeq_client():
    return InspeqEval(inspeq_api_key=INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID, inspeq_api_url=INSPEQ_API_URL)

def validate_result_structure(result):
    assert "status" in result
    assert "message" in result
    assert "results" in result
    assert isinstance(result["results"], list)

    for item in result["results"]:
        assert "id" in item
        assert "project_id" in item
        assert "task_id" in item
        assert "task_name" in item
        assert "model_name" in item
        assert "source_platform" in item
        assert "data_input_id" in item
        assert "data_input_name" in item
        assert "metric_set_input_id" in item
        assert "metric_set_input_name" in item
        assert "response" in item
        assert "context" in item
        assert "metric_name" in item
        assert "score" in item
        assert "passed" in item
        assert isinstance(item["passed"], bool)
        assert "evaluation_details" in item
        assert "metrics_config" in item
        assert "created_at" in item
        assert "updated_at" in item
        assert "created_by" in item
        assert "updated_by" in item
        assert "is_deleted" in item
        assert "metric_evaluation_status" in item

    assert "user_id" in result
    assert "remaining_credits" in result

def run_test(inspeq_client, metrics_list, input_data, task_name):
    try:
        result = inspeq_client.evaluate_llm_task(
            metrics_list=metrics_list,
            input_data=input_data,
            task_name=task_name
        )
        print(f"Task result: {json.dumps(result, indent=2)}")
        
        validate_result_structure(result)
        return result
        
    except APIError as e:
        pytest.fail(f"API Error occurred: {str(e)}")
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {str(e)}")

def test_evaluate_llm_task_generation_metrics(inspeq_client, random_task_name):
    generation_metrics = [
        "RESPONSE_TONE", "ANSWER_RELEVANCE", "FACTUAL_CONSISTENCY", "CONCEPTUAL_SIMILARITY",
        "READABILITY", "COHERENCE", "CLARITY", "DIVERSITY", "CREATIVITY", "NARRATIVE_CONTINUITY",
        "GRAMMATICAL_CORRECTNESS", "PROMPT_INJECTION", "DATA_LEAKAGE", "INSECURE_OUTPUT",
        "INVISIBLE_TEXT", "TOXICITY"
    ]
    input_data = [
        {
            "prompt": "What are the benefits of renewable energy?",
            "response": "Renewable energy sources like solar and wind power offer numerous benefits. They reduce greenhouse gas emissions, decrease dependence on fossil fuels, create jobs in the green energy sector, and can lead to long-term cost savings for consumers and businesses.",
            "context": "The user is researching sustainable energy solutions."
        }
    ]
    
    run_test(inspeq_client, generation_metrics, input_data, random_task_name)

def test_evaluate_llm_task_summarization_metrics(inspeq_client, random_task_name):
    summarization_metrics = [
        "BLEU_SCORE", "COMPRESSION_SCORE", "COSINE_SIMILARITY_SCORE",
        "FUZZY_SCORE", "METEOR_SCORE", "ROUGE_SCORE"
    ]
    input_data = [
        {
            "context": "Climate change is a global challenge that affects all aspects of our lives. It is caused by the increase in greenhouse gases in the atmosphere, primarily due to human activities such as burning fossil fuels and deforestation. The effects of climate change include rising temperatures, more frequent extreme weather events, sea-level rise, and disruptions to ecosystems. To address this issue, countries around the world are working to reduce their carbon emissions and transition to renewable energy sources.",
            "response": "Climate change, driven by human activities, causes global temperature rise and extreme weather. Countries are working to reduce emissions and adopt renewable energy to combat it.",
            "reference_summary": "Climate change, caused by increased greenhouse gases from human activities, leads to rising temperatures and extreme weather. Global efforts focus on reducing emissions and adopting renewable energy."
        }
    ]
    
    run_test(inspeq_client, summarization_metrics, input_data, random_task_name)

def test_evaluate_llm_task_special_cases(inspeq_client, random_task_name):
    special_metrics = ["CREATIVITY", "DIVERSITY", "PROMPT_INJECTION", "INSECURE_OUTPUT", "INVISIBLE_TEXT", "TOXICITY"]
    input_data = [
        {
            "prompt": "Write a creative short story about a time-traveling scientist.",
            "response": "Dr. Amelia Chronos adjusted her temporal goggles, heart racing as she prepared to make her first jump through time. The lab hummed with energy as she activated the chrono-field generator. In a flash of blue light, she vanished from 2023 and reappeared in ancient Egypt. To her amazement, she found herself face-to-face with Cleopatra, who mistook her for a goddess from the future. Amelia's scientific curiosity battled with her ethical training as she considered the potential consequences of interacting with such a pivotal historical figure. In the end, she chose to observe silently, gathering invaluable data about the past while safeguarding the timeline. As she returned to her own time, Amelia realized that the true power of time travel lay not in changing history, but in understanding it.",
            "context": "The user is participating in a creative writing contest."
        }
    ]
    
    run_test(inspeq_client, special_metrics, input_data, random_task_name)
