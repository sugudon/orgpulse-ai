import streamlit as st
import requests


# ==========================================
# Configuration
# ==========================================

API_URL = "http://localhost:8000"


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="OrgPulse AI",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==========================================
# API Health Check
# ==========================================

def check_api_health():
    """
    Check whether the FastAPI backend is running.
    """

    try:
        response = requests.get(
            f"{API_URL}/health",
            timeout=3,
        )

        if response.status_code == 200:
            return True

        return False

    except requests.exceptions.RequestException:
        return False


# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.title("🌐 OrgPulse AI")

    st.caption(
        "Organizational Intelligence Platform"
    )

    st.divider()

    st.subheader("System Status")

    api_running = check_api_health()

    if api_running:
        st.success("🟢 Backend Connected")
    else:
        st.error("🔴 Backend Offline")

    st.divider()

    st.caption("Agentic Hybrid RAG")

    st.markdown(
        """
        **Powered by**

        - 🔍 Hybrid Retrieval
        - 🎯 Reranking
        - 🔄 Corrective RAG
        - 🤖 AI Agents
        - 🧠 Cross-Document Intelligence
        """
    )


# ==========================================
# Header
# ==========================================

st.title("🌐 OrgPulse AI")

st.subheader(
    "Turn scattered organizational knowledge "
    "into connected intelligence."
)

st.divider()


# ==========================================
# Metrics
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📄 Documents",
        value="0",
        delta="Upload documents",
    )

with col2:
    st.metric(
        label="🔗 Connections",
        value="0",
        delta="Discover relationships",
    )

with col3:
    st.metric(
        label="⚠️ Risks",
        value="0",
        delta="AI analysis",
    )

with col4:
    st.metric(
        label="🧠 Insights",
        value="0",
        delta="Ask OrgPulse",
    )


st.divider()


# ==========================================
# Main Question Section
# ==========================================

st.subheader("🧠 Ask Your Organization")

question = st.text_area(
    label="Ask OrgPulse anything about your organization",
    placeholder=(
        "Example: Why is the Payment Migration "
        "project delayed?"
    ),
    height=120,
)


# ==========================================
# Analyze Button
# ==========================================

if st.button(
    "🚀 Analyze with OrgPulse",
    type="primary",
    use_container_width=True,
):

    if not question.strip():

        st.warning(
            "Please enter a question first."
        )

    elif not api_running:

        st.error(
            "FastAPI backend is offline. "
            "Please start the backend first."
        )

    else:

        with st.spinner(
            "🧠 OrgPulse is analyzing organizational knowledge..."
        ):

            st.info(
                "RAG pipeline will be connected in the next phase."
            )


# ==========================================
# Example Questions
# ==========================================

st.divider()

st.subheader("💡 Try These Questions")

example_col1, example_col2 = st.columns(2)

with example_col1:

    st.info(
        "🔍 Why is the Payment Migration "
        "project delayed?"
    )

    st.info(
        "⚠️ What are the biggest risks "
        "across projects?"
    )


with example_col2:

    st.info(
        "🔗 Which projects are affected "
        "by infrastructure delays?"
    )

    st.info(
        "🚨 Are there contradictions "
        "between project reports?"
    )


# ==========================================
# Footer
# ==========================================

st.divider()

st.caption(
    "OrgPulse AI • Agentic Hybrid RAG • "
    "Organizational Intelligence"
)