"""Web Search Tool for Research Agent."""
from langchain_core.tools import tool
import os

@tool
def web_search(query: str, max_results: int = 5) -> str:
    """Search the web for information on a given topic."""
    try:
        from tavily import TavilyClient
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "TAVILY_API_KEY not set in secrets."
        client = TavilyClient(api_key=api_key)
        response = client.search(query, max_results=max_results)
        results = []
        for i, r in enumerate(response["results"], 1):
            results.append(
                f"[{i}] {r['title']}\n"
                f"    {r['content']}\n"
                f"    URL: {r['url']}"
            )
        return "\n\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search error: {str(e)}"

@tool
def fetch_webpage(url: str) -> str:
    """Fetch and extract text content from a webpage."""
    try:
        from tavily import TavilyClient
        api_key = os.getenv("TAVILY_API_KEY")
        client = TavilyClient(api_key=api_key)
        response = client.extract(urls=[url])
        return response["results"][0]["raw_content"][:3000]
    except Exception as e:
        return f"Fetch error: {str(e)}"
