from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

llm = ChatOllama(
    model="llama3.2"
)

agent = create_react_agent(
    model=llm,
    tools=[],
    checkpointer=InMemorySaver()
)
