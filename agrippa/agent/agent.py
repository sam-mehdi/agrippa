import os
import sys

# load environment variables from .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Check if OpenAI API key is set
if "OPENAI_API_KEY" not in os.environ:
    print("Agrippa is a fan of Sam Altman. Make sure to set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

# Make the model
from langchain_openai import ChatOpenAI

model = ChatOpenAI()

# Prepare agent messages
from agrippa.agent.prompts import system_message
from langchain import hub

base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=system_message)

# Create agent with tools
from langchain.agents import AgentExecutor, create_openai_functions_agent
from agrippa.tools.all_tools import all_tools

agent = AgentExecutor(agent=create_openai_functions_agent(model, all_tools, prompt), tools=all_tools)

# Add chat history
from agrippa.agent.features.chat_history import add_chat_history

agrippa_agent = add_chat_history(agent)

def call_agrippa(human_message):
    return agrippa_agent.invoke(
        { "input" : human_message },
        config={"configurable": {"session_id": "1"} },
    )
