from crewai import Crew,Process


from agents import blog_researcher,blog_writer_agent
from tasks import research_task,write_task


crew = Crew(
    agents = [blog_researcher,blog_writer_agent],
    tasks= [research_task,write_task],
    process= Process.sequential,
    memory = True,
    cache = True,
    max_rpm=100,
    share_crew=True
)


## Start task execution process with enhanced feedback

topic =[]

result = crew.kickoff(inputs= {'topic':'AI VS ML VS DL VS Data Science'})
print(result)