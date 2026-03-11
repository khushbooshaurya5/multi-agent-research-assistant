"""Web Search Tool for Research Agent."""
from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup

@tool
def web_search(query: str, max_results: int = 5) -> str:
    """Search the web for information on a given topic.
    Args:
        query: Search query string
        max_results: Maximum number of results to return
    Returns:
        Formatted search results as string
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Research Assistant Bot)"}
        url = f"https://html.duckduckgo.com/html/?q={query}"
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return f"Search failed with status {response.status_code}"
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for i, result in enumerate(soup.find_all("a", class_="result__a")):
            if i >= max_results:
                break
            title = result.get_text(strip=True)
            href = result.get("href", "")
            results.append(f"[{i+1}] {title}\n    URL: {href}")
        return "\n\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search error: {str(e)}"

@tool
def fetch_webpage(url: str) -> str:
    """Fetch and extract text content from a webpage.
    Args:
        url: URL of the webpage to fetch
    Returns:
        Extracted text content
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Research Assistant Bot)"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        return text[:3000] + "\n...[truncated]" if len(text) > 3000 else text
    except Exception as e:
        return f"Fetch error: {str(e)}"
