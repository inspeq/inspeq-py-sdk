import requests


class Inspeq:
    def __init__(self, api_key, chatgpt_api_key):
        self.api_key = api_key
        self.chatgpt_api_key = chatgpt_api_key
        self.base_url = "https://api.example.com/inspeq/"
        # 

    def _make_request(self, endpoint, params):
        # Make HTTP request to the API endpoint
        # Handle authentication and error handling
        # pass
                # response = requests.get('https://example.com', verify=True)
                # response = requests.get('https://example.com', timeout=5)  # Timeout set to 5 seconds
#         try:
#     response = requests.get('https://example.com')
#     response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx status codes)
# except requests.exceptions.RequestException as e:
#     print(f"Error: {e}")
        return 30
        

    def get_factual_correctness(self, input_context, input_question, output):
        
        # endpoint = "metrics/factual_correctness"
        # params = {
        #     "input_context": input_context,
        #     "input_question": input_question,
        #     "output": output,
        # }
        # return self._make_request(endpoint, params)
        return 1
    
    def get_get_answer_relevance(self, input_context, input_question, output):
        
        pass
    

    # Define similar methods for other metrics
