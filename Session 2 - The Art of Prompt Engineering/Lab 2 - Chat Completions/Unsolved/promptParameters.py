# Add the **temperature** and **top_p**, also experiment with the **max_tokens**, **n**, and **stop** parameters to the function.
# Separate the code from jupyter

import openai
from openai import OpenAIError
import os
from openai import AzureOpenAI
import sys
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import init_creds as creds


def fetch_api_key():

    AZURE_OPENAI_KEY = creds.get_api_key()
    AZURE_OPENAI_ENDPOINT = creds.get_endpoint()
    
    if not AZURE_OPENAI_KEY:
        raise ValueError("No AZURE_OPENAI_KEY set for Azure OpenAI API")
    if not AZURE_OPENAI_ENDPOINT:
        raise ValueError("No AZURE_OPENAI_ENDPOINT set for Azure OpenAI API")

    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_KEY,
        api_version="2024-07-01-preview"
    )
    return client

def chat_completion(prePrompt, prompt, temperature=0.7, top_p=1, max_tokens=150, n=1, stop=None):
    messages = [
        {"role": "system", "content": prePrompt},
        {"role": "user", "content": prompt}
    ]
    try:
        client = fetch_api_key()    
        chat_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            n=n,
            stop=stop
        )
        return chat_completion.choices[0].message.content
    except OpenAIError as e:
        return f"Error: An error occurred in the OpenAI API:\n{e}"
    except Exception as e:
        return f"Error: An error occurred:\n{e}"
    
prePrompt = "You are a helpful assistant that knows how to tell a good story, spin a great yarn, and write a tall tale."
prompt = """Write a short story about a robot learning to understand human emotions."""
print("temperature=0.7, top_p=1, max_tokens=500, n=1, stop=None")
print(chat_completion(prePrompt, prompt, temperature=0.7, top_p=1, max_tokens=500, n=1, stop=None))
print('-----------------------------------')
print("temperature=0.2, top_p=1, max_tokens=500, n=1, stop=None")
print(chat_completion(prePrompt, prompt, temperature=0.2, top_p=1, max_tokens=500, n=1, stop=None))