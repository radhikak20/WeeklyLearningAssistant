import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapeWebsiteTool,
	ArxivPaperTool
)





@CrewBase
class WeeklyLearningAssistantCrew:
    """WeeklyLearningAssistant crew"""

    
    @agent
    def learning_content_researcher(self) -> Agent:
        
        return Agent(
            config=self.agents_config["learning_content_researcher"],
            
            
            tools=[				ScrapeWebsiteTool(),
				ArxivPaperTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    
    @agent
    def learning_plan_strategist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["learning_plan_strategist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    
    @agent
    def progress_tracker_and_motivator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["progress_tracker_and_motivator"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    

    
    @task
    def research_weekly_learning_content(self) -> Task:
        return Task(
            config=self.tasks_config["research_weekly_learning_content"],
            markdown=False,
            
            
        )
    
    @task
    def create_structured_learning_plan(self) -> Task:
        return Task(
            config=self.tasks_config["create_structured_learning_plan"],
            markdown=False,
            
            
        )
    
    @task
    def generate_learning_progress_summary(self) -> Task:
        return Task(
            config=self.tasks_config["generate_learning_progress_summary"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the WeeklyLearningAssistant crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


