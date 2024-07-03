from agrippa.tools.gmail import get_gmail_tools
from agrippa.tools.youtube import get_youtube_tools
from agrippa.tools.weather import get_weather_tools

all_tools = get_gmail_tools() + get_weather_tools() + get_youtube_tools()
