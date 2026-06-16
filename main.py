from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """Schema for a response from the agent"""

    answer: str = Field(description="The agent's answer to the user's question")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")


def main():
    print("Hello from langchain-course!")
    llm = ChatOpenAI(temperature=0, model="gpt-5.4-mini")
    tools = [TavilySearch(max_results=5)]
    agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 job postings for an AI engineer using langchain in the bay area on linkedin and list their details")]})
    print(result)

if __name__ == "__main__":
    main()
