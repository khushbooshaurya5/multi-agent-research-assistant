# Multi-Agent Research Assistant

A multi-agent AI system built with LangChain demonstrating Agent-to-Agent (A2A) communication, tool calling, and RAG (Retrieval-Augmented Generation) for automated research workflows.

## Architecture

```
User Query
    |
    v
[Orchestrator Agent]
    |
    ├── [Research Agent] -- Web search, document retrieval
    |
    ├── [Analysis Agent] -- Data analysis, summarization
    |
    └── [Report Agent] -- Structured report generation
```

## Features

- **Multi-Agent Orchestration:** Orchestrator agent delegates tasks to specialized sub-agents
- **Agent-to-Agent (A2A) Communication:** Agents pass context and results between each other
- **Tool Calling:** Each agent has access to specialized tools (search, analyze, write)
- **RAG Pipeline:** Document ingestion with FAISS vector store for context-aware responses
- **MCP-Style Patterns:** Tool use patterns inspired by Model Context Protocol
- **Streamlit UI:** Interactive web interface for research queries

## Tech Stack

- **LangChain** - Agent framework and orchestration
- **FAISS** - Vector similarity search for RAG
- **Hugging Face** - Embeddings (sentence-transformers)
- **Streamlit** - Web UI
- **Python 3.10+**

## Installation

```bash
git clone https://github.com/khushbooshaurya5/multi-agent-research-assistant.git
cd multi-agent-research-assistant
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## Project Structure

```
├── app.py                  # Streamlit UI
├── agents/
│   ├── __init__.py
│   ├── orchestrator.py     # Main orchestrator agent
│   ├── research_agent.py   # Web search and document retrieval
│   ├── analysis_agent.py   # Data analysis and summarization
│   └── report_agent.py     # Structured report generation
├── tools/
│   ├── __init__.py
│   ├── search_tool.py      # Web search tool
│   ├── rag_tool.py         # RAG retrieval tool
│   └── analysis_tool.py    # Data analysis tool
├── rag/
│   ├── __init__.py
│   ├── ingest.py           # Document ingestion pipeline
│   └── retriever.py        # FAISS retriever
├── config.py               # Configuration
├── requirements.txt
└── README.md
```

## How It Works

1. **User submits a research query** via Streamlit UI
2. **Orchestrator Agent** analyzes the query and creates a research plan
3. **Research Agent** searches for relevant information using web search and RAG tools
4. **Analysis Agent** processes gathered information, extracts key insights
5. **Report Agent** compiles findings into a structured research report
6. Agents communicate results via **A2A message passing**

## Key Concepts Demonstrated

- **Multi-Agent Systems:** Specialized agents with distinct roles
- **A2A Communication:** Structured message passing between agents
- **Tool Calling:** Function calling with defined schemas
- **RAG:** Document retrieval for grounded responses
- **MCP Patterns:** Tool use inspired by Model Context Protocol

## Author

Khushboo Kumari - M.Sc. Machine Learning & Data Analytics, Aalen University
