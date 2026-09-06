# 🌐 OrgPulse AI

## An Agentic Hybrid RAG System for Organizational Intelligence

> **Don't just search documents. Discover connections, risks, contradictions, and hidden knowledge.**

OrgPulse AI is an advanced **Agentic Hybrid RAG (Retrieval-Augmented Generation)** system designed to transform scattered organizational documents into actionable intelligence.

Unlike a traditional RAG chatbot that simply retrieves documents and generates answers, OrgPulse AI combines **semantic search, keyword search, reranking, corrective retrieval, and AI agents** to analyze organizational knowledge and discover meaningful insights.

---

## 🚀 Problem Statement

Organizations generate large amounts of information across:

- 📄 Project Reports
- 📝 Meeting Notes
- 🚨 Incident Reports
- 📊 Status Reports
- 🚀 Release Documents
- 📚 Technical Documentation
- 📋 Internal Knowledge Bases

Over time, this information becomes scattered across multiple documents and teams.

Employees struggle to answer questions such as:

- Why is a project delayed?
- Are multiple teams solving the same problem?
- What are the biggest risks across projects?
- Are there contradictions between different reports?
- What projects or teams are connected to a particular issue?

Traditional search systems and basic RAG chatbots can retrieve documents, but they cannot effectively discover **cross-document relationships and organizational intelligence**.

---

## 💡 Solution

### OrgPulse AI

OrgPulse AI transforms organizational documents into an intelligent knowledge system.

The system uses an **Agentic Hybrid RAG architecture** to:

- 🔍 Retrieve information using semantic and keyword search
- 🎯 Rerank the most relevant results
- 🔄 Correct poor retrieval automatically
- 🤖 Route questions to specialized AI agents
- 🔗 Discover relationships across documents
- ⚠️ Detect organizational risks
- 🚨 Identify contradictions
- 📄 Provide evidence-backed answers
- 📊 Generate confidence scores

---

## 🧠 Key Features

### 1. 📄 Intelligent Document Processing

Users can upload organizational documents such as:

- PDF
- TXT
- DOCX
- Project Reports
- Meeting Notes
- Incident Reports

```text
Document Upload
      ↓
Document Processing
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embedding Generation
      ↓
PostgreSQL + pgvector
```

---

### 2. 🔍 Hybrid Retrieval

OrgPulse AI combines two retrieval approaches:

#### Semantic Search
Uses vector embeddings to understand the meaning behind a question.

#### Keyword Search
Uses BM25 to find exact terms.

#### Hybrid Search

```text
Vector Search
      +
BM25 Search
      ↓
Hybrid Retrieval
```

This improves retrieval accuracy by combining semantic understanding with exact keyword matching.

---

### 3. 🎯 Reranking

Initial retrieval may return many documents.

```text
Top 20 Results
      ↓
Cross-Encoder Reranker
      ↓
Top 5 Relevant Results
```

The reranker selects the most relevant context before it is sent to the LLM.

---

### 4. 🔄 Self-Corrective RAG

OrgPulse AI evaluates the quality of retrieved information before generating an answer.

```text
User Question
      ↓
Retrieve Documents
      ↓
Evaluate Relevance
      ↓

   Context Good?

     YES       NO
      │         │
      │         ▼
      │    Rewrite Query
      │         ↓
      │    Retrieve Again
      │         │
      └─────────┘
           ↓
    Generate Answer
```

This reduces irrelevant responses and improves answer quality.

---

### 5. 🤖 Agentic Intelligence

The system analyzes the user's question and routes it to the appropriate agent.

```text
                User Question
                     ↓
                Agent Router
                     ↓

        ┌────────────┼────────────┐

        ↓            ↓            ↓

    RAG Agent    Risk Agent   Connection Agent
                     │
                     ↓
               Conflict Agent
```

#### 🔍 RAG Agent
Handles general organizational questions.

#### ⚠️ Risk Agent
Identifies potential risks across documents.

#### 🔗 Connection Agent
Discovers relationships between projects, teams, and issues.

#### 🚨 Conflict Agent
Detects contradictions between documents.

---

### 6. 🧠 Cross-Document Intelligence

Instead of analyzing documents individually, OrgPulse AI analyzes information across multiple sources.

```text
Document A
     │
Document B
     │
Document C
     │
Document D
     ↓
Relationship Discovery
     ↓
New Insight
```

---

### 7. 📊 Organizational Risk Intelligence

Example output:

```text
🚨 HIGH RISK

Project:
Payment Migration

Risk Score:
82%

Risk:
Database migration dependency

Impact:
HIGH

Evidence:
📄 Project Status Report
📄 Engineering Meeting Notes
📄 Incident Report
```

---

### 8. 🔗 Knowledge Connections

OrgPulse AI discovers relationships between:

- Projects
- Teams
- Technologies
- Issues
- Dependencies
- Risks

Example:

```text
Payment Migration
        │
        │ depends on
        ↓
Database Team
        │
        │ delayed
        ↓
Infrastructure
       /        \
      ↓          ↓
Cloud Migration  Mobile App
```

---

### 9. 📄 Evidence-Based Answers

Every answer is supported by source evidence.

```text
Answer:
Payment Migration is delayed primarily because
of database migration dependencies and
infrastructure provisioning issues.

Confidence:
92%

Evidence:
📄 Payment_Status_Report.pdf
📄 Engineering_Meeting_Notes.pdf
📄 Migration_Incident_Report.pdf
```

---

## 🏗️ System Architecture

```text
                         USER
                           │
                           ▼
                    STREAMLIT UI
                           │
                           ▼
                       FASTAPI
                           │
                           ▼
                    AGENT ROUTER
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼

      RAG Agent        Risk Agent    Connection Agent

          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                     HYBRID RAG
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
           Vector Search         BM25 Search
                 │                   │
                 └─────────┬─────────┘
                           ▼
                    Hybrid Results
                           │
                           ▼
                      Reranking
                           │
                           ▼
                 Context Evaluation
                           │
                    Good? / Poor?
                           │
                           ▼
                      Query Rewrite
                           │
                           ▼
                  Answer Generation
                           │
                           ▼
                   Evidence + Confidence
```

---

## 🛠️ Technology Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Python

### AI Framework
- LangChain
- LangGraph

### LLM
- OpenAI / Groq / Ollama

### Embeddings
- Sentence Transformers
- HuggingFace Embeddings

### Database
- PostgreSQL
- pgvector

### Retrieval
- Vector Search
- BM25
- Hybrid Search

### Reranking
- Cross-Encoder

---

## 📁 Project Structure

```text
orgpulse-ai/

├── frontend/
│   ├── app.py
│   ├── pages/
│   │   ├── 1_Dashboard.py
│   │   ├── 2_Ask_OrgPulse.py
│   │   ├── 3_Risk_Intelligence.py
│   │   └── 4_Knowledge_Connections.py
│   └── components/
│       ├── metrics.py
│       ├── chat.py
│       ├── evidence.py
│       └── risk_cards.py
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── api/
│       │   ├── documents.py
│       │   └── query.py
│       ├── agents/
│       │   ├── router.py
│       │   ├── rag_agent.py
│       │   ├── risk_agent.py
│       │   ├── connection_agent.py
│       │   └── conflict_agent.py
│       ├── rag/
│       │   ├── ingestion.py
│       │   ├── embeddings.py
│       │   ├── vector_search.py
│       │   ├── bm25_search.py
│       │   ├── hybrid_search.py
│       │   ├── reranker.py
│       │   └── corrective_rag.py
│       ├── database/
│       │   ├── connection.py
│       │   └── models.py
│       └── core/
│           └── config.py
│
├── sample_data/
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🔄 RAG Pipeline

```text
DOCUMENT
   ↓
Text Extraction
   ↓
Chunking
   ↓
Generate Embeddings
   ↓
PostgreSQL + pgvector


USER QUESTION
   ↓
Query Understanding
   ↓
Agent Router
   ↓
Hybrid Search
   ↓
Vector Search + BM25
   ↓
Reranking
   ↓
Context Evaluation
   ↓
Query Rewrite (if required)
   ↓
AI Agent Analysis
   ↓
Generate Response
   ↓
Evidence + Confidence
```

---

## 🎨 Streamlit Application

### 🏠 Dashboard
Displays:

- Total Documents
- Detected Risks
- Knowledge Connections
- Recent Insights

### 🤖 Ask OrgPulse

Users can ask:

```text
Why is Payment Migration delayed?

What are the biggest risks across projects?

Are multiple teams solving the same problem?

Which projects are affected by the infrastructure delay?
```

### ⚠️ Risk Intelligence

Displays:

- Risk Score
- Impact Level
- Affected Projects
- Evidence
- AI Recommendations

### 🔗 Knowledge Connections

Visualizes relationships between:

- Projects
- Teams
- Issues
- Dependencies

---

## 🎯 Example Use Cases

### Root Cause Analysis

**Question:**
> Why is the Payment Migration project delayed?

**Example Insight:**

```text
Root Cause Analysis

1. Database migration dependency
2. Infrastructure provisioning delay
3. Testing environment unavailable

Potential Impact:
Cloud Migration may also be affected.

Confidence: 91%
```

### Duplicate Work Detection

**Question:**
> Are multiple teams building similar solutions?

The system compares cross-document information and identifies similar work across teams.

### Risk Analysis

**Question:**
> What are the biggest risks across projects?

The Risk Agent analyzes project reports, meeting notes, and incidents to identify potential risks.

### Contradiction Detection

**Question:**
> Are there conflicting release dates?

Example:

```text
🚨 CONTRADICTION DETECTED

Document A:
Release Date: September 10

Document B:
Release Date: September 25

Recommendation:
Verify the latest project release plan.
```

---

## 🧠 RAG Strategy

OrgPulse AI uses:

# Agentic Hybrid RAG with Corrective Retrieval

```text
Hybrid Search
      +
Reranking
      +
Corrective Retrieval
      +
Agent Routing
      +
Cross-Document Intelligence
```

---

## 🔥 Why OrgPulse AI?

### Traditional RAG

```text
Question
   ↓
Retrieve
   ↓
Generate
```

### OrgPulse AI

```text
Search
   ↓
Validate
   ↓
Correct
   ↓
Analyze
   ↓
Connect
   ↓
Discover
   ↓
Answer with Evidence
```

OrgPulse AI goes beyond document question answering and helps organizations discover meaningful insights hidden across their data.

---

## 🚀 Future Enhancements

- 📧 Email Integration
- 💬 Slack Integration
- 📊 Advanced Analytics
- 🕸️ Interactive Knowledge Graph
- 👥 Role-Based Access Control
- 🔔 Risk Alerts
- 🔄 Real-Time Document Updates
- 📈 Organizational Trend Analysis

---

## 🏆 Buildathon Highlights

### Advanced RAG
- Hybrid Retrieval
- Reranking
- Corrective Retrieval

### Agentic AI
- Agent Router
- Specialized Agents

### Organizational Intelligence
- Risk Detection
- Connection Discovery
- Contradiction Detection

### Evidence-Based AI
- Source Citations
- Confidence Scores
- Verification

---

## 📌 Project Vision

> **OrgPulse AI is designed to evolve from a document question-answering system into an intelligent organizational knowledge engine capable of discovering risks, relationships, contradictions, and actionable insights across scattered organizational information.**

---

## 👩‍💻 Author

**Suguna Jayaram**

Senior Software Engineer | AI Engineering Enthusiast

---

## ⭐ Final Thought

> **OrgPulse AI does not just answer questions. It helps organizations understand what their documents are collectively trying to say.**
