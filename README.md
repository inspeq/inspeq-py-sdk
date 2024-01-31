# inspeq-py-sdk
Inspeq python SDK

# make venv
python3 -m venv venv 




# How to use 

Mention python version compatibility. 

## Installation

pip install inspeq-py-sdk

# Initialization
inspeq_inst = Inspeq(api_key="your_api_key", chatgpt_api_key="your_chatgpt_api_key")

# Usage
result = inspeq_inst.get_factual_correctness("context", "question", "output")
print(result)


## TODO
 How to user api key method 



 SSL enable- 