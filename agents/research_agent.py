"""Research Agent - handles web search and document retrieval."""
from tools.search_tool import web_search, fetch_webpage
from tools.rag_tool import retrieve_from_knowledge_base


class ResearchAgent:
    """Agent specialized in gathering information from multiple sources."""

    def __init__(self):
        self.tools = {
            "web_search": web_search,
            "fetch_webpage": fetch_webpage,
            "rag_retrieve": retrieve_from_knowledge_base
        }

    def research(self, query: str, use_rag: bool = False) -> str:
        """Conduct research on a topic.
        
        Args:
            query: Research query
            use_rag: Whether to also search knowledge base
            
        Returns:
            Compiled research findings
        """
        findings = []

        # Tool call: Web search
        search_results = self.tools["web_search"].invoke({"query": query})
        findings.append(f"WEB SEARCH RESULTS:\n{search_results}")

        # Tool call: RAG retrieval (if enabled)
        if use_rag:
            rag_results = self.tools["rag_retrieve"].invoke({"query": query})
            findings.append(f"KNOWLEDGE BASE RESULTS:\n{rag_results}")

        return "\n\n===\n\n".join(findings)
