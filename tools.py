from crewai_tools import YoutubeChannelSearchTool


from dotenv import load_dotenv



load_dotenv() 
import os


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"


yt_tool = YoutubeChannelSearchTool(youtube_channel_handle="@krishnaik06")

