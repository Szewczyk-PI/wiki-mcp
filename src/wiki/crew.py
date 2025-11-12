from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.mcp import MCPServerStdio
from typing import List
from .tools.custom_tool import clear_markd
import os

@CrewBase
class Wiki():
    """Wiki crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def wiki_agent(self) -> Agent:
        # Get the absolute path to the MCP server
        mcp_server_dir = os.path.join(os.path.dirname(__file__), "wiki-js-mcp")
        mcp_server_script = os.path.join(mcp_server_dir, "src", "wiki_mcp_server.py")
        mcp_venv_python = os.path.join(mcp_server_dir, "venv", "bin", "python3")

        return Agent(
            config=self.agents_config['wiki_agent'],
            verbose=True,
            mcps=[
                MCPServerStdio(
                    command=mcp_venv_python,
                    args=[mcp_server_script],
                    env={**os.environ},  # Pass all environment variables including those from .env
                )
            ],
            tools=[clear_markd]
        )

    @task
    def wiki_task(self) -> Task:
        return Task(
            config=self.tasks_config['wiki_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Wiki crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )
