from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

llm = ChatOpenAI(temperature=0, model="gpt-5.4-mini")
tools = [TavilySearch(max_results=5)]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 job postings for an AI engineer using langchain in the bay area on linkedin and list their details")]})
    print(result)


if __name__ == "__main__":
    main()
