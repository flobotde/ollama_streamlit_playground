# utils/crew.py
import os
import re
import time
from config.config import settings
import streamlit as st
from streamlit import expander
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
#from langchain_community.tools import DuckDuckGoSearchRun

# Uncomment the following line to use an example of a custom tool
# from surprise_travel.tools.custom_tool import MyCustomTool

# Check our tools documentation for more information on how to use them
#from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field
from typing import List, Optional

#websearch_tool = DuckDuckGoSearchRun()

#display the console processing on streamlit UI
# coffee goes to https://github.com/AbubakrChan/crewai-UI-business-product-launch/blob/main/main.py
class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  # Define a list of colors
        self.color_index = 0  # Initialize color index

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        if task_value:
            st.toast("New Task" + task_value, icon="🤖")

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            # Apply different color and switch color index
            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f':<font color="{self.colors[self.color_index]}">[Entering new CrewAgentExecutor chain]</font>')

        if "Forschungsexperte" in cleaned_data:
            # Apply different color 
            self.color_index = 0
            cleaned_data = cleaned_data.replace("Forschungsexperte", f':<font color="{self.colors[self.color_index]}">[Forschungsexperte]</font>')
        if "Zusammenfassungsanalyst" in cleaned_data:
            self.color_index = 1
            cleaned_data = cleaned_data.replace("Zusammenfassungsanalyst", f':<font color="{self.colors[self.color_index]}">[Zusammenfassungsanalyst]</font>')

        cleaned_data = '<div style="font-size: 0.7em">' + cleaned_data + '</div>'

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []


# e.g. Models to use from the agents
#class Topic(BaseModel):
#    question: str = Field(..., description="Question from the user for this research")
#    name: str = Field(..., description="Name of the topic of this research")
    
@CrewBase
class ResearcherCrew:
    """Researcher crew"""
    basedir=os.path.abspath(os.path.join(os.path.dirname(__file__)))
    agents_config = basedir + '/../config/agents.yml'
    tasks_config = basedir + '/../config/tasks.yml'

    def __init__(self, topic):
        self.topic = topic
    
    @agent
    def researcher(self) -> Agent:
        try:
            model = f"ollama/{st.session_state.selected_model}"
            return Agent(
                llm=model, # fixme for not ollama
                config=self.agents_config['researcher'],
                verbose=True,
#               tools=[websearch_tool],
            )
        except Exception as e:
            st.error(
                f"""Failed to ´create Researcher Agent with model: {model}. Error: {str(e)}""",
                icon="😳",
                )

    @agent
    def summarizer(self) -> Agent:
        try:
            model = f"ollama/{st.session_state.selected_model}"
            return Agent(
                llm=model, # fixme for not ollama
                config=self.agents_config['summarizer'],
                verbose=True,
            )
        except Exception as e:
            st.error(
                f"""Failed to ´create Summarizer Agent with model: {model}. Error: {str(e)}""",
                icon="😳",
                )
        
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            )

    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_task'],
    )

    @crew
    def crew(self) -> Crew:
        """Creates the Researcher crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you want to use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

    