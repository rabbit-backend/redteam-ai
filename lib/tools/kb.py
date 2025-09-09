from langchain_core.tools import tool
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
import chromadb

embedding_model = OllamaEmbeddings(
    model="llama3.2"
)

chroma_client = chromadb.HttpClient(
    host="127.0.0.1",
    port=8888,
    ssl=False
)
vector_store = Chroma(
    client=chroma_client,
    collection_name="kb_cyber_security",
    embedding_function=embedding_model
)

@tool(description="search for the knowledge base for any existing tools that can be used from pen testing")
def cyber_kb(q: str):
    results = vector_store.similarity_search(
        q,
        k=2,
    )

    response = []
    for result in results:
        response.append(result.metadata)

    return response
