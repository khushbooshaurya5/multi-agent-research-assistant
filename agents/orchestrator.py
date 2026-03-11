"""Orchestrator Agent - coordinates multi-agent research workflow."""
from typing import Dict, List
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.report_agent import ReportAgent


class OrchestratorAgent:
    """Main orchestrator that coordinates research workflow via A2A communication."""

    def __init__(self):
        self.research_agent = ResearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.report_agent = ReportAgent()
        self.message_log: List[Dict] = []

    def _log_message(self, sender: str, receiver: str, content: str):
        """Log A2A communication between agents."""
        self.message_log.append({
            "from": sender,
            "to": receiver,
            "content": content[:200] + "..." if len(content) > 200 else content
        })

    def run(self, query: str, use_rag: bool = False) -> Dict:
        """Execute full research workflow.
        
        Args:
            query: User research query
            use_rag: Whether to use RAG knowledge base
            
        Returns:
            Dict with research results, analysis, report, and message log
        """
        results = {"query": query, "stages": {}, "message_log": []}

        # Stage 1: Research
        self._log_message("Orchestrator", "ResearchAgent", f"Research: {query}")
        research_results = self.research_agent.research(query, use_rag=use_rag)
        results["stages"]["research"] = research_results
        self._log_message("ResearchAgent", "Orchestrator", research_results)

        # Stage 2: Analysis
        self._log_message("Orchestrator", "AnalysisAgent", "Analyze research findings")
        analysis = self.analysis_agent.analyze(research_results)
        results["stages"]["analysis"] = analysis
        self._log_message("AnalysisAgent", "Orchestrator", analysis)

        # Stage 3: Report Generation
        self._log_message("Orchestrator", "ReportAgent", "Generate research report")
        report = self.report_agent.generate(
            query=query,
            research=research_results,
            analysis=analysis
        )
        results["stages"]["report"] = report
        self._log_message("ReportAgent", "Orchestrator", "Report generated")

        results["message_log"] = self.message_log
        return results
