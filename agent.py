from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver
from lib.mitm.startup import start_mitm_proxy
import threading

proxy = threading.Thread(target=start_mitm_proxy)
proxy.start()

checkpointer = InMemorySaver()

llm = ChatOllama(
    model="llama3.2"
)

print("[x] creating an agent")
agent = create_react_agent(
    model=llm,
    tools=[],
    checkpointer=InMemorySaver()
)

proxy.join()
