import unittest
from inspeq.client import Inspeq

class TestInspeqSDK(unittest.TestCase):
    def setUp(self):
        # Set up any necessary resources or configurations for tests
        pass

    def tearDown(self):
        # Clean up after each test
        pass


    def test_get_factual_correctness(self):
        inspeq_inst = Inspeq(api_key="test_key", chatgpt_api_key="test_chatgpt_key")
        result = inspeq_inst.get_factual_correctness("context", "question", "output")
        self.assertEqual(result, 30)
        

    def test_get_answer_relevance(self):
        inspeq_inst = Inspeq(api_key="test_key", chatgpt_api_key="test_chatgpt_key")
        result = inspeq_inst.get_get_answer_relevance("context", "question", "output")
        self.assertEqual(result, 30)
    
    
    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
