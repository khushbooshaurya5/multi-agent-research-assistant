"""Analysis Agent - processes and analyzes research findings."""
from tools.analysis_tool import extract_key_points, summarize_text, compare_sources


class AnalysisAgent:
    """Agent specialized in analyzing and synthesizing information."""

    def __init__(self):
        self.tools = {
            "extract_key_points": extract_key_points,
            "summarize": summarize_text,
            "compare": compare_sources
        }

    def analyze(self, research_data: str) -> str:
        """Analyze research findings.
        
        Args:
            research_data: Raw research data from Research Agent
            
        Returns:
            Analysis results
        """
        # Tool call: Extract key points
        key_points = self.tools["extract_key_points"].invoke({"text": research_data})

        # Tool call: Summarize
        summary = self.tools["summarize"].invoke({"text": research_data})

        return f"ANALYSIS RESULTS:\n\n{key_points}\n\nSUMMARY:\n{summary}"
