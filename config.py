"""Configuration for Multi-Agent Research Assistant."""

import os
from dotenv import load_dotenv

load_dotenv()

# Embedding model for RAG
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# FAISS vector store path
VECTOR_STORE_PATH = "data/faiss_index"

# Chunk settings for document ingestion
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Agent settings
MAX_AGENT_ITERATIONS = 10
AGENT_TEMPERATURE = 0.1

# Streamlit settings
PAGE_TITLE = "Multi-Agent Research Assistant"
PAGE_ICON = "🔬"
