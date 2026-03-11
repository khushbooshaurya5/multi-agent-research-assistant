"""Streamlit UI for Multi-Agent Research Assistant."""
import streamlit as st
from agents.orchestrator import OrchestratorAgent
import json

st.set_page_config(page_title="Multi-Agent Research Assistant", page_icon="🔬", layout="wide")

st.title("🔬 Multi-Agent Research Assistant")
st.markdown(
    "A multi-agent AI system with **A2A communication**, **tool calling**, "
    "and **RAG** for automated research workflows."
)

# Sidebar
with st.sidebar:
    st.header("Settings")
    use_rag = st.checkbox("Use Knowledge Base (RAG)", value=False)
    st.markdown("---")
    st.markdown("### Architecture")
    st.markdown("""
    ```
    User Query
        |
    [Orchestrator]
        |
        +-- [Research Agent]
        |   Tools: web_search, RAG
        |
        +-- [Analysis Agent]
        |   Tools: key_points, summarize
        |
        +-- [Report Agent]
            Output: Structured Report
    ```
    """)
    st.markdown("---")
    st.markdown("**Built by:** Khushboo Kumari")
    st.markdown("**Stack:** LangChain, FAISS, Streamlit")

# Main interface
query = st.text_input("Enter your research query:", placeholder="e.g., Latest advances in multi-agent AI systems")

if st.button("🚀 Start Research", type="primary"):
    if not query:
        st.warning("Please enter a research query.")
    else:
        orchestrator = OrchestratorAgent()

        with st.spinner("Research Agent gathering information..."):
            results = orchestrator.run(query, use_rag=use_rag)

        # Display results in tabs
        tab1, tab2, tab3, tab4 = st.tabs(["📄 Report", "🔍 Research", "📊 Analysis", "💬 A2A Messages"])

        with tab1:
            st.text(results["stages"]["report"])

        with tab2:
            st.markdown("### Raw Research Findings")
            st.text(results["stages"]["research"])

        with tab3:
            st.markdown("### Analysis Results")
            st.text(results["stages"]["analysis"])

        with tab4:
            st.markdown("### Agent-to-Agent Communication Log")
            for msg in results["message_log"]:
                with st.chat_message("assistant"):
                    st.markdown(f"**{msg['from']}** → **{msg['to']}**")
                    st.text(msg["content"])
