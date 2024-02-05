import unittest
from unittest.mock import patch, MagicMock
from inspeq.client import Inspeq

class TestInspeqSDK(unittest.TestCase):
    @patch('inspeq.client.requests.post')
    def test_process_request_success(self, mock_post):
        # Mock the requests.post method to return a successful response
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"message": "Success"})

        inspeq_instance = Inspeq()
        sdk_api_key = ""
        input_data = {
            "type": "your_type",
            "llm_input_context": "your_llm_input_context",
            "llm_input_query": "your_llm_input_query",
            "llm_output": "your_llm_output",
        }

        # Call the method being tested
        inspeq_instance.process_request(sdk_api_key, input_data)

        # Assert that the mock was called with the correct arguments
        mock_post.assert_called_once_with(
            "",
            params={"secret_key": sdk_api_key},
            json=input_data
        )

    @patch('inspeq.client.requests.post')
    def test_process_request_failure(self, mock_post):
        # Mock the requests.post method to return a failure response
        mock_post.return_value = MagicMock(status_code=500, text="Internal Server Error")

        inspeq_instance = Inspeq()
        sdk_api_key = ""
        input_data = {
            "type": "your_type",
            "llm_input_context": "your_llm_input_context",
            "llm_input_query": "your_llm_input_query",
            "llm_output": "your_llm_output",
        }

        # Call the method being tested
        inspeq_instance.process_request(sdk_api_key, input_data)

        # Assert that the mock was called with the correct arguments
        mock_post.assert_called_once_with(
            "t",
            params={"secret_key": sdk_api_key},
            json=input_data
        )

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
