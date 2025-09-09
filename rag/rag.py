import glob
from langchain_core.documents import Document
from langchain_ollama.embeddings import OllamaEmbeddings
from uuid import uuid4
from langchain_chroma import Chroma
import chromadb

doc_paths = glob.glob("rag/kb/*.txt")

def get_toolname_from_path(path: str):
    return path.split("/")[-1].split(".")[0]

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

documents = []
ids = []
for id, kb_doc in enumerate(doc_paths):
    with open(kb_doc, "r") as f:
        doc = f.read()

    tool_name = get_toolname_from_path(kb_doc)
    document = Document(
        page_content=doc,
        metadata={
            "tool_name": tool_name,
            "content": doc
        },
        id=id
    )

    documents.append(document)
    ids.append(str(uuid4()))

vector_store.add_documents(
    documents=documents,
    ids=ids
)
