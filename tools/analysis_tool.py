"""Analysis Tools for Analysis Agent."""
from langchain_core.tools import tool
import re

@tool
def extract_key_points(text: str, max_points: int = 5) -> str:
    """Extract key points from a text passage.
    Args:
        text: Input text to analyze
        max_points: Maximum number of key points
    Returns:
        Extracted key points as formatted string
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    importance_words = ["important", "key", "significant", "found", "showed", "new", "novel", "first", "critical"]
    scored = []
    for sentence in sentences:
        score = sum(1 for w in importance_words if w in sentence.lower())
        score += len(sentence.split()) / 50
        scored.append((score, sentence))
    scored.sort(key=lambda x: x[0], reverse=True)
    result = "KEY POINTS:\n"
    for i, (_, point) in enumerate(scored[:max_points], 1):
        result += f"{i}. {point}\n"
    return result

@tool
def summarize_text(text: str, target_length: int = 150) -> str:
    """Create a concise summary of the input text.
    Args:
        text: Text to summarize
        target_length: Target word count for summary
    Returns:
        Condensed summary
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    if not sentences:
        return "No content to summarize."
    summary_sentences = []
    word_count = 0
    for sentence in sentences:
        words = len(sentence.split())
        if word_count + words <= target_length:
            summary_sentences.append(sentence)
            word_count += words
        else:
            break
    return ". ".join(summary_sentences) + "."

@tool
def compare_sources(source_a: str, source_b: str) -> str:
    """Compare information from two different sources.
    Args:
        source_a: Text from first source
        source_b: Text from second source
    Returns:
        Comparison analysis
    """
    words_a = set(source_a.lower().split())
    words_b = set(source_b.lower().split())
    common = words_a & words_b
    overlap = len(common) / max(len(words_a | words_b), 1)
    level = "High" if overlap > 0.3 else "Moderate" if overlap > 0.15 else "Low"
    return f"SOURCE COMPARISON:\n- Overlap: {overlap:.2%}\n- Agreement: {level}"
