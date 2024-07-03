# load environment variables from .env file
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Make sure weather env vars are set
import os
import sys
if "OPENWEATHERMAP_API_KEY" not in os.environ:
    print("Make sure to set the OPENWEATHERMAP_API_KEY environment variable.")
    sys.exit(1)

# Make the tool
from langchain_community.agent_toolkits.load_tools import load_tools

def get_weather_tools():
    return load_tools(['openweathermap-api'])
