import os
from langchain.vectorstores.chroma import Chroma
from app.chat.embeddings.ollama import embeddings

vector_store = Chroma(
    collection_name=os.getenv("CHROMA_COLLECTION_NAME", "default_collection"),
    embedding_function=embeddings,
    persist_directory=os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")
)