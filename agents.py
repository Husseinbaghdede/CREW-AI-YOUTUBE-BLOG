from crewai import Agent,LLM
from tools import yt_tool

## Create a senior blog content researcher

from dotenv import load_dotenv



load_dotenv() 

import os


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"





blog_researcher = Agent(
    role='Blog Researcher from youtube videos',
    goal= 'get the relevat video content for the topic {topic} from youtube channel',
    name= 'Senior Blog Content Researcher',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding vidons in AI Data Science ,Machine learning And Gen AI and providing suggestions"

    ),
    

    tools = [yt_tool],
    allow_delegation=True
)

# Creating a senior blog writer agent with YT tool
blog_writer_agent = Agent(
    role="Blog writer",
    goal="Narrate compelling tech stories about the video {topic} from Yt channel",
    verbose=True,
    memory=True,
    backstory="""
        With a flair for simplifying complex topics, you craft
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    """,
    tools=[],

    allow_delegation=False
)
