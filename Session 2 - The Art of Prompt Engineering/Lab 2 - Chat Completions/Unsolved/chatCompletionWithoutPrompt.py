# create a chat completion with Python
import os
from openai import AzureOpenAI

import sys
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import init_creds as creds
 
AZURE_OPENAI_KEY = creds.get_api_key()
AZURE_OPENAI_ENDPOINT = creds.get_endpoint()

print(AZURE_OPENAI_KEY)
print(AZURE_OPENAI_ENDPOINT)
if not AZURE_OPENAI_KEY:
    raise ValueError("No AZURE_OPENAI_KEY set for Azure OpenAI API")
if not AZURE_OPENAI_ENDPOINT:
    raise ValueError("No AZURE_OPENAI_ENDPOINT set for Azure OpenAI API")

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-07-01-preview"
)

def chatPrompt():


    conversation=[{"role": "system", "content": "You are a helpful assistant."}]
 
    while True:
        user_input = input("Q:")   
        if user_input.lower() == "exit":
            break   
        conversation.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini", # model = "deployment_name".
            messages=conversation
        )

        conversation.append({"role": "assistant", "content": response.choices[0].message.content})
        print("\n" + response.choices[0].message.content + "\n")
        

if __name__ == "__main__":
    chatPrompt()
    