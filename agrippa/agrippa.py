from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os
import sys

# load environment variables from .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Set up Agrippa's pretty printer and color scheme
os.system('color') # Enable color in Windows terminal
from termcolor import colored
print(colored("Agrippa ", "yellow", attrs=["bold"]) + colored("awaits your command.", "red"))

# Check if OpenAI API key is set
if "OPENAI_API_KEY" not in os.environ:
    print("Agrippa is a fan of Sam Altman. Make sure to set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

# Get prompt from CLI arguments
prompt = sys.argv[1]

# Make the model
model = ChatOpenAI()

messages = [
    SystemMessage(
        content="You are Marcus Vispanius Agrippa, Roman general, state-builder, architect, and problem solver. Your loyalty to Octavian, \
			your best friend anad trusted leader, is unquestioned." +
        "While on campaign in Gaul, you receive the following missive from Octavian. Follow his instructions, and report back your results."
    ),
    HumanMessage(
        content=prompt,
    ),
]

# Invoke the model
response = model.invoke(messages).content

# Print the response, rendering new lines
print(response.replace("\n", "\n"))
