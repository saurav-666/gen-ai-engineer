# Add context to the conversation so that you can continue the dialog instead of each prompt standing on its own.
# 1) Store conversation history
# 2) Append new user inputs to the conversation history.
# 3) Send the entire conversation history as context in each API call. 
# 4) Add the **temperature** and **top_p**, also experiment with the **max_tokens**, **n**, and **stop** parameters to the function.

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
def chat_completion(prePrompt, prompt, conversation_history, temperature=0.1, top_p=1, max_tokens=5000, n=1, stop=None):
    if conversation_history is None or len(conversation_history) == 0:
        conversation_history = [
            {"role": "system", "content": prePrompt}
        ]
    conversation_history.append(
        {"role": "user", "content": prompt}
    )
    try:
        client = fetch_api_key()
        chat_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            n=n,
            stop=stop
        )
        response = chat_completion.choices[0].message.content
        print(f'ChatGPT Response: {response}\n----------------------------------\n')
        # Append the assistant's response to the conversation history
        conversation_history.append(
            {"role": "assistant", "content": response}
        )

        return response, conversation_history
    except OpenAIError as e:
        return f"Error: An error occurred in the OpenAI API:\n{e}", conversation_history
    except Exception as e:
        return f"Error: An error occurred:\n{e}", conversation_history
    
# Initialize conversation history
conversation_history = []

prePrompt = "You are a helpful assistant that knows about US geography, topography, flora, and fauna."
prompt = """What is the capital of New York?"""
response, conversation_history = chat_completion(prePrompt, prompt, conversation_history)
#print(response)
prompt = """How many people live there?"""
response, conversation_history = chat_completion(None, prompt, conversation_history)
#print(response)
prompt = """What is the weather like?"""
response, conversation_history = chat_completion(None, prompt, conversation_history)
#print(response)
prompt = """What is there to do there?"""
response, conversation_history = chat_completion(None, prompt, conversation_history)
#print(response)