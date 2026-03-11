"""FAISS retriever for RAG pipeline."""
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config import EMBEDDING_MODEL, VECTOR_STORE_PATH


def get_retriever(top_k: int = 3):
    """Get FAISS retriever instance.
    Args:
        top_k: Number of documents to retrieve
    Returns:
        FAISS retriever or None if not initialized
    """
    if not os.path.exists(VECTOR_STORE_PATH):
        return None
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = FAISS.load_local(
        VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True
    )
    return vectorstore.as_retriever(search_kwargs={"k": top_k})
