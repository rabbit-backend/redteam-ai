from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

llm = ChatOllama(
    model="llama3.2"
)
