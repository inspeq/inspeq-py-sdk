import pytest
import json
from unittest.mock import patch, MagicMock
from inspeq.client import InspeqEval, APIError

@pytest.fixture
def inspeq_client():
    return InspeqEval("test_api_key", "test_project_id")

def test_evaluate_llm_task(inspeq_client):
    # Test successful case
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "status": 200,
        "message": "All LLM evaluations successful",
        "data": [
            {
                "metric_name": "RESPONSE_TONE_EVALUATION",
                "score": "0.75",
                "passed": True,
                "evaluation_details": "base64_encoded_details",
                "metrics_config": "base64_encoded_config"
            },
            {
                "metric_name": "FACTUAL_CONSISTENCY_EVALUATION",
                "score": "0.85",
                "passed": True,
                "evaluation_details": "base64_encoded_details",
                "metrics_config": "base64_encoded_config"
            }
        ]
    }

    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        result = inspeq_client.evaluate_llm_task(
            metrics_list=["RESPONSE_TONE", "FACTUAL_CONSISTENCY"],
            input_data=[{
                "prompt": "What is the capital of France?",
                "response": "Paris is the capital of France.",
                "context": "The user is asking about European capitals."
            }],
            task_name="test_task"
        )

        assert result["status"] == 200
        assert result["message"] == "All LLM evaluations successful"
        assert len(result["data"]) == 2
        
        for item in result["data"]:
            assert "metric_name" in item
            assert "score" in item
            assert "passed" in item
            assert "evaluation_details" in item
            assert "metrics_config" in item
            assert item["metric_name"].replace("_EVALUATION", "") in ["RESPONSE_TONE", "FACTUAL_CONSISTENCY"]

    # Test error case
    mock_response.status_code = 400
    mock_response.text = "Bad Request"
    
    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        with pytest.raises(APIError, match="API call failed with status code 400: Bad Request"):
            inspeq_client.evaluate_llm_task(
                metrics_list=["RESPONSE_TONE"],
                input_data=[{"response": "test_response"}],
                task_name="test_task"
            )

    # Test with custom metrics configuration
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "status": 200,
        "message": "All LLM evaluations successful",
        "data": [
            {
                "metric_name": "RESPONSE_TONE_EVALUATION",
                "score": "0.6",
                "passed": True,
                "evaluation_details": "base64_encoded_details",
                "metrics_config": "base64_encoded_config"
            }
        ]
    }

    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        result = inspeq_client.evaluate_llm_task(
            metrics_list=["RESPONSE_TONE"],
            input_data=[{
                "prompt": "What is the weather like?",
                "response": "The weather is sunny and warm.",
                "context": "The user is asking about current weather conditions."
            }],
            task_name="test_task",
            metrics_config={
                "response_tone_config": {
                    "threshold": 0.6,
                    "custom_labels": ["Negative", "Neutral", "Positive"],
                    "label_thresholds": [0, 0.3, 0.7, 1]
                }
            }
        )

        assert result["status"] == 200
        assert len(result["data"]) == 1
        assert result["data"][0]["metric_name"] == "RESPONSE_TONE_EVALUATION"
        assert float(result["data"][0]["score"]) >= 0.6
