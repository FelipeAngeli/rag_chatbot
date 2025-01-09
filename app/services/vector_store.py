import os

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from config.settings import PERSIST_DIRECTORY


def load_existing_vector_store():
    if os.path.exists(PERSIST_DIRECTORY):
        vector_store = Chroma(
            persist_directory=PERSIST_DIRECTORY,
            embedding_function=OpenAIEmbeddings(),
        )
        return vector_store
    return None

def add_to_vector_store(chunks, vector_store=None):
    if vector_store:
        vector_store.add_documents(chunks)
    else:
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=OpenAIEmbeddings(),
            persist_directory=PERSIST_DIRECTORY,
        )
    return vector_store