# Check the environment for the OpenAI API key
import sys
sys.path.insert(1, '../../')
import init_creds as creds
 
AZURE_OPENAI_KEY = creds.get_api_key()
AZURE_OPENAI_ENDPOINT = creds.get_endpoint()
 
if not AZURE_OPENAI_KEY:
    raise ValueError("No AZURE_OPENAI_KEY set for Azure OpenAI API")
if not AZURE_OPENAI_ENDPOINT:
    raise ValueError("No AZURE_OPENAI_ENDPOINT set for Azure OpenAI API")

from langchain_openai import AzureChatOpenAI

model = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    model="gpt-4o-mini",
    api_version="2024-07-01-preview"    
)

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You talk like a pirate. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

from typing import Sequence
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    language: str

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

config = {"configurable": {"thread_id": "Conversation00001"}}

from langchain_core.messages import trim_messages

trimmer = trim_messages(
    max_tokens=100000,
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human",
)

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph

# Async function for node:
async def call_model(state: State, config: dict):
    chain = prompt | trimmer | model | parser
    response = await chain.ainvoke(state, config)
    return {"messages": [response]}

# Define graph as before:
workflow = StateGraph(state_schema=State)
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)
app = workflow.compile(checkpointer=MemorySaver())

from langchain_core.messages import HumanMessage, AIMessage

async def chatbot(query):
    message = HumanMessage(query)
    input_messages = [message]
    async for chunk, metadata in app.astream(input={"messages": input_messages}, config=config, stream_mode="messages"):
        if isinstance(chunk, AIMessage):
            yield chunk.content