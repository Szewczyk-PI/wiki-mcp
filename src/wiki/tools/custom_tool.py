from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import tool


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."


@tool("Clear_markd")
def clear_markd(tekst: str) -> str:
    """Clean tekst from markdown style"""
    tekst_new = tekst.replace("*", "")
    tekst_new = tekst_new.replace("**", "")
    tekst_new = tekst_new.replace("*", "")
    tekst_new = tekst_new.replace("`","")
    tekst_new = tekst_new.replace("#","")
    tekst_new = tekst_new.replace("|","")
    tekst_new = tekst_new.replace("--","")
    """Clear tekst from markdown signs"""
    return tekst_new
