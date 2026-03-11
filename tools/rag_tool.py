"""RAG Retrieval Tool for grounded responses."""
from langchain_core.tools import tool

@tool
def retrieve_from_knowledge_base(query: str, top_k: int = 3) -> str:
    """Retrieve relevant documents from the knowledge base using RAG.
    Args:
        query: Search query for document retrieval
        top_k: Number of top results to return
    Returns:
        Retrieved document chunks
    """
    try:
        from rag.retriever import get_retriever
        retriever = get_retriever()
        if retriever is None:
            return "Knowledge base not initialized. Ingest documents first."
        docs = retriever.invoke(query)
        if not docs:
            return "No relevant documents found."
        results = []
        for i, doc in enumerate(docs[:top_k], 1):
            source = doc.metadata.get("source", "Unknown")
            results.append(f"[Doc {i}] ({source})\n{doc.page_content}")
        return "\n\n---\n\n".join(results)
    except Exception as e:
        return f"RAG error: {str(e)}"
