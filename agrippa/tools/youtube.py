from langchain_community.tools import YouTubeSearchTool

tool = YouTubeSearchTool()

def get_youtube_tools():
    return [tool]
