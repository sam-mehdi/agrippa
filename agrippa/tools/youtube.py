from langchain_community.tools import YouTubeSearchTool

tool = YouTubeSearchTool()

print(tool.run("skyrim with guns"))
