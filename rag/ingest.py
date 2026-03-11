"""Document ingestion pipeline for RAG."""
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config import EMBEDDING_MODEL, VECTOR_STORE_PATH, CHUNK_SIZE, CHUNK_OVERLAP


def ingest_documents(docs_path: str = "data/documents"):
    """Ingest documents into FAISS vector store.
    Args:
        docs_path: Path to directory containing documents
    """
    if not os.path.exists(docs_path):
        os.makedirs(docs_path)
        print(f"Created {docs_path}. Add documents and run again.")
        return

    loader = DirectoryLoader(docs_path, glob="**/*.txt", loader_cls=TextLoader)
    documents = loader.load()

    if not documents:
        print("No documents found. Add .txt files to data/documents/")
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = FAISS.from_documents(chunks, embeddings)

    os.makedirs(os.path.dirname(VECTOR_STORE_PATH), exist_ok=True)
    vectorstore.save_local(VECTOR_STORE_PATH)
    print(f"Vector store saved to {VECTOR_STORE_PATH}")


if __name__ == "__main__":
    ingest_documents()
