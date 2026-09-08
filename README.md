# 🌐 OrgPulse AI

## Adaptive GraphRAG for Organizational Intelligence

> **OrgPulse AI is an AI-powered Organizational Intelligence System that dynamically adapts its RAG strategy based on the user's query complexity, intent, and entities.**

Unlike traditional RAG systems that use the same retrieval pipeline for every question, OrgPulse AI intelligently decides **how much retrieval and reasoning is required**.

It combines:

* 🔍 Vector Search
* 📝 Keyword Search
* 🕸️ Knowledge Graph
* 🧠 Adaptive RAG
* 🔀 Fusion RAG
* 🔮 HyDE
* 🎯 Reranking
* 🔄 Corrective RAG
* 🤔 Self Reflection

---

# 🚀 The Problem

Organizations generate large amounts of unstructured information:

* 📄 Project Reports
* 📝 Meeting Notes
* 📊 Status Reports
* 📧 Internal Documents
* ⚠️ Risk Reports
* 📋 Technical Documentation

Important organizational knowledge is often scattered across multiple documents.

Traditional search systems struggle to answer questions such as:

> Why is a project delayed?

> What dependencies are causing a problem?

> Which teams or projects are affected by a particular issue?

> Are there risks hidden across multiple documents?

> Do two organizational documents contain conflicting information?

---

# 💡 The Solution

OrgPulse AI transforms organizational documents into an **intelligent knowledge system**.

The system processes documents through two intelligence layers:

```text
                    ORGANIZATIONAL DOCUMENTS
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼

          🔍 VECTOR MEMORY              🕸️ KNOWLEDGE GRAPH

             FAISS                         Neo4j

        Semantic Knowledge            Relationships

        Document Chunks               Entities

        Embeddings                    Dependencies

                                     Connections
```

This allows OrgPulse AI to understand both:

### 📄 What information exists?

Using:

```text
Vector Search
+
BM25 Keyword Search
```

### 🕸️ How information is connected?

Using:

```text
Knowledge Graph
+
Entity Relationships
+
Multi-Hop Traversal
```

---

# 🧠 What is Adaptive RAG?

Traditional RAG uses a fixed pipeline:

```text
Question
   ↓
Retrieve Documents
   ↓
LLM
   ↓
Answer
```

This approach treats every question the same.

OrgPulse AI uses **Adaptive RAG**.

Before retrieving information, the system analyzes:

```text
User Query
    │
    ▼

🧠 Query Analyzer

    │
    ├── Intent
    │
    ├── Entities
    │
    └── Complexity
```

Then it dynamically selects the best retrieval strategy.

---

# ⚡ Adaptive Retrieval Strategies

## 🟢 Simple Query

Example:

> Who owns Payment Migration?

Pipeline:

```text
User Query
    ↓
Query Analyzer
    ↓
Hybrid Search
    ↓
FAISS + BM25
    ↓
RRF
    ↓
Reranker
    ↓
Answer
```

The system uses a fast retrieval pipeline.

---

## 🟡 Medium Query

Example:

> What blockers are affecting Payment Migration?

Pipeline:

```text
User Query
    ↓
Query Analyzer
    ↓
Hybrid Retrieval
    ↓
FAISS + BM25
    ↓
RRF
    ↓
Reranker
    ↓
Graph Retrieval
    ↓
Context Fusion
    ↓
Answer
```

The system adds Knowledge Graph reasoning.

---

## 🔴 Complex Query

Example:

> Why is Payment Migration delayed, what dependencies caused it, and which other projects are affected?

Pipeline:

```text
User Query
    ↓
🧠 Query Analyzer
    ↓
🔀 Fusion RAG
+
🔮 HyDE
    ↓
🔍 Hybrid Retrieval
    ↓
FAISS + BM25
    ↓
🔥 RRF
    ↓
🎯 Reranker
    ↓
🕸️ Multi-Hop Graph Retrieval
    ↓
🔄 CRAG Evaluation
    ↓
🤔 Self Reflection
    ↓
🚀 Final Answer
```

Advanced techniques are activated **only when required**.

---

# 🏆 Core Architecture

```text
                           USER QUERY
                               │
                               ▼

                       🧠 QUERY ANALYZER

                  Intent + Entities + Complexity

                               │

                ┌──────────────┴──────────────┐

                │                             │

                ▼                             ▼

           SIMPLE QUERY                  COMPLEX QUERY

                │                             │

                ▼                             ▼

          FAST RETRIEVAL              ADVANCED RETRIEVAL

                                              │

                                  ┌───────────┴───────────┐

                                  │                       │

                                  ▼                       ▼

                             🔀 Fusion RAG             🔮 HyDE

                             Multi Query         Hypothetical Document

                                  │                       │

                                  └───────────┬───────────┘

                                              │

                ┌─────────────────────────────┴──────────────────────┐

                │                                                    │

                ▼                                                    ▼

         🔍 VECTOR RETRIEVAL                                   🕸️ GRAPH RAG

             FAISS                                               Neo4j

                │                                                    │

                ▼                                                    ▼

         Semantic Search                                    Relationships

                │                                             Multi-Hop

                │                                             Dependencies

                │                                                    │

                └─────────────────────────────┬──────────────────────┘

                                              │

                                              ▼

                                      🔍 HYBRID SEARCH

                                     FAISS + BM25

                                              │

                                              ▼

                                           🔥 RRF

                                 Reciprocal Rank Fusion

                                              │

                                              ▼

                                         🎯 RERANKER

                                              │

                                              ▼

                                        CONTEXT FUSION

                                              │

                                              ▼

                                         🔄 CRAG

                                   Context Evaluation

                                      │           │

                                   GOOD          BAD

                                      │           │

                                      ▼           ▼

                                  GENERATE    RETRIEVE AGAIN

                                      │

                                      ▼

                                🤔 SELF REFLECTION

                                      │

                                      ▼

                                  🚀 FINAL ANSWER

                                      +

                                  📄 SOURCES

                                      +

                                  🕸️ GRAPH PATH

                                      +

                                  📊 CONFIDENCE
```

---

# 🔥 Advanced RAG Techniques

## 🔍 Hybrid Search

OrgPulse combines:

```text
FAISS
  +
BM25
```

### FAISS

Used for semantic search.

Example:

```text
User Query:

Why is the project delayed?

Can retrieve:

Infrastructure dependency is blocking completion.
```

Even if the word **delay** does not appear.

---

### BM25

Used for exact keyword matching.

Example:

```text
Payment Migration
Infrastructure
Database
Delay
```

---

# 🔥 Reciprocal Rank Fusion

RRF combines results from multiple retrieval systems.

```text
FAISS Results

     +

BM25 Results

     ↓

RRF

     ↓

Unified Ranking
```

Formula:

```text
RRF Score = Σ 1 / (k + rank)
```

This improves retrieval reliability.

---

# 🎯 Reranking

After retrieval:

```text
Top 20 Documents
       ↓
Cross Encoder
       ↓
Top 5 Relevant Documents
```

OrgPulse uses a Cross Encoder to compare:

```text
User Question
+
Document Chunk
```

This improves answer precision.

---

# 🔀 Fusion RAG

Fusion RAG generates multiple perspectives of a complex question.

Example:

```text
Original Question

Why is Payment Migration delayed?
```

Generated queries:

```text
What blockers affect Payment Migration?

What dependencies are unresolved?

What infrastructure problems affect the project?

What is preventing project completion?
```

Each query retrieves information.

Results are combined using:

```text
RRF
```

### Why?

Different documents often use different terminology for the same problem.

Fusion RAG improves **retrieval recall**.

---

# 🔮 HyDE

HyDE stands for:

> Hypothetical Document Embeddings

The system generates a hypothetical document related to the question.

Example:

```text
Question:

Why is Payment Migration delayed?
```

Hypothetical document:

```text
Payment Migration may be delayed because of unresolved
infrastructure dependencies, unavailable environments,
database validation issues, or blocked testing.
```

The hypothetical document is embedded and used for semantic retrieval.

```text
Question
    ↓
Generate Hypothetical Document
    ↓
Embedding
    ↓
FAISS Search
    ↓
Relevant Real Documents
```

HyDE improves semantic retrieval for difficult queries.

---

# 🕸️ Knowledge Graph Intelligence

OrgPulse uses Neo4j to store organizational relationships.

## Nodes

```text
Project
Team
Person
Issue
Risk
Technology
Document
Dependency
```

## Relationships

```text
DEPENDS_ON

BLOCKED_BY

AFFECTS

OWNED_BY

RELATED_TO

MENTIONED_IN
```

Example:

```text
Payment Migration

        │

        │ DEPENDS_ON

        ▼

Database Team

        │

        │ BLOCKED_BY

        ▼

Infrastructure Delay

        │

        │ AFFECTS

        ▼

Cloud Migration
```

---

# 🧠 Multi-Hop Reasoning

Knowledge Graph allows OrgPulse to discover hidden relationships.

Example:

```text
Payment Migration

        ↓

Database Team

        ↓

Infrastructure Delay

        ↓

Cloud Migration
```

This enables questions such as:

> What other projects may be affected by this delay?

Traditional Vector RAG alone cannot reliably perform this type of relationship reasoning.

---

# 🔄 Corrective RAG (CRAG)

Before generating an answer, OrgPulse evaluates retrieved context.

```text
Retrieved Context

       ↓

CRAG Evaluator

       ↓

GOOD

PARTIAL

BAD
```

If the context is poor:

```text
Query Rewrite

      ↓

Retrieve Again
```

This allows the system to self-correct retrieval.

---

# 🤔 Self Reflection

Before returning the answer, OrgPulse evaluates its own response.

Checks include:

```text
✓ Is the answer supported by retrieved evidence?

✓ Did the answer address the user question?

✓ Is information missing?

✓ Is there a possible hallucination?

✓ Should the system retrieve more information?
```

---

# 💎 OrgPulse AI Unique Features

## 🟢 1. Adaptive Retrieval

The system dynamically selects:

```text
Simple Query
    ↓
Fast Retrieval
```

```text
Medium Query
    ↓
Graph + Hybrid Retrieval
```

```text
Complex Query
    ↓
Advanced Adaptive RAG
```

---

## ⚠️ 2. Risk Intelligence

OrgPulse analyzes organizational knowledge to identify risks.

Example:

```text
🔴 Payment Migration

Risk:

Infrastructure dependency delay

Affected Projects:

Cloud Migration

Confidence:

92%
```

---

## 🚨 3. Contradiction Detection

OrgPulse can detect conflicting information across documents.

Example:

### Document A

```text
Project completion: September 20
```

### Document B

```text
Project completion delayed until October
```

OrgPulse:

```text
🚨 Timeline Contradiction Detected

Project:
Payment Migration

Conflict:
September 20 vs October
```

---

## 🕸️ 4. Dependency Intelligence

Users can ask:

> What projects depend on the Database Team?

> What issues are affecting multiple projects?

> Which dependency creates the highest organizational risk?

OrgPulse uses Knowledge Graph traversal to answer.

---

## 📊 5. Evidence-Based Answers

Every answer includes:

```text
📄 Document Sources

🕸️ Graph Relationships

📊 Confidence Score
```

---

# 🛠️ Technology Stack

| Layer               | Technology    |
| ------------------- | ------------- |
| Frontend            | Streamlit     |
| Backend             | FastAPI       |
| LLM                 | OpenAI        |
| Embeddings          | HuggingFace   |
| Vector Store        | FAISS         |
| Keyword Search      | BM25          |
| Knowledge Graph     | Neo4j         |
| Reranker            | Cross Encoder |
| Document Processing | PyPDF         |
| DOCX Processing     | python-docx   |

---

# 📁 Project Structure

```text
orgpulse-ai/
│
├── frontend/
│   │
│   ├── app.py
│   │
│   ├── pages/
│   │   ├── 1_Ask_OrgPulse.py
│   │   ├── 2_Knowledge_Graph.py
│   │   ├── 3_Risk_Intelligence.py
│   │   └── 4_System_Insights.py
│   │
│   └── components/
│       ├── api_client.py
│       ├── evidence.py
│       ├── metrics.py
│       └── graph_view.py
│
│
├── backend/
│   └── app/
│       │
│       ├── main.py
│       │
│       ├── core/
│       │   └── config.py
│       │
│       ├── api/
│       │   ├── documents.py
│       │   ├── query.py
│       │   └── graph.py
│       │
│       ├── schemas/
│       │   ├── document.py
│       │   └── query.py
│       │
│       ├── rag/
│       │   │
│       │   ├── ingestion.py
│       │   ├── chunker.py
│       │   ├── embeddings.py
│       │   │
│       │   ├── query_analyzer.py
│       │   ├── strategy_router.py
│       │   │
│       │   ├── fusion_rag.py
│       │   ├── hyde.py
│       │   │
│       │   ├── vector_search.py
│       │   ├── bm25_search.py
│       │   ├── hybrid_search.py
│       │   ├── rrf.py
│       │   ├── reranker.py
│       │   │
│       │   ├── crag.py
│       │   └── self_reflection.py
│       │
│       ├── vectorstore/
│       │   └── faiss_store.py
│       │
│       ├── graph/
│       │   ├── connection.py
│       │   ├── schema.py
│       │   ├── entity_extractor.py
│       │   ├── relationship_extractor.py
│       │   └── graph_retriever.py
│       │
│       └── services/
│           ├── document_service.py
│           └── query_service.py
│
├── sample_data/
│
├── uploads/
│
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>

cd orgpulse-ai
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment

Copy:

```text
.env.example
```

Create:

```text
.env
```

Add:

```env
OPENAI_API_KEY=your_openai_api_key

OPENAI_MODEL=gpt-4.1-mini

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

NEO4J_URI=your_neo4j_uri

NEO4J_USERNAME=neo4j

NEO4J_PASSWORD=your_password

NEO4J_DATABASE=neo4j

CHUNK_SIZE=800

CHUNK_OVERLAP=150

VECTOR_TOP_K=10

BM25_TOP_K=10

RERANK_TOP_K=5
```

---

# ▶️ Run Backend

From:

```text
backend/
```

Run:

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

---

# 🎨 Run Frontend

From:

```text
frontend/
```

Run:

```bash
streamlit run app.py
```

---

# 🔄 Document Processing Pipeline

```text
PDF / DOCX / TXT

        │

        ▼

TEXT EXTRACTION

        │

        ▼

CHUNKING

        │

        ├───────────────────┐

        │                   │

        ▼                   ▼

VECTOR PIPELINE       GRAPH PIPELINE

Embeddings            Entity Extraction

FAISS                 Relationship Extraction

                         Neo4j

        │                   │

        └───────────┬───────┘

                    ▼

           DOCUMENT INDEXED
```

---

# 🔍 Query Processing Pipeline

```text
USER QUESTION

      │

      ▼

QUERY ANALYZER

      │

Intent
Entities
Complexity

      │

      ▼

STRATEGY ROUTER

      │

      ├──────────────┐

      │              │

      ▼              ▼

SIMPLE          COMPLEX

      │              │

      ▼              ▼

FAST         ADVANCED

      │              │

      │       Fusion RAG

      │       HyDE

      │              │

      └──────┬───────┘

             ▼

      HYBRID RETRIEVAL

      FAISS + BM25

             │

             ▼

            RRF

             │

             ▼

         RERANKER

             │

             ▼

       GRAPH RETRIEVAL

             │

             ▼

       CONTEXT FUSION

             │

             ▼

            LLM

             │

             ▼

       FINAL RESPONSE
```

---

# 🏆 Why OrgPulse AI?

Traditional RAG:

```text
Question

↓

Retrieve

↓

Answer
```

OrgPulse AI:

```text
Question

↓

Understand

↓

Analyze Complexity

↓

Select Strategy

↓

Retrieve Knowledge

↓

Explore Relationships

↓

Evaluate Evidence

↓

Generate

↓

Validate

↓

Answer
```

---

# 🎯 Buildathon Innovation

## OrgPulse AI is not just a chatbot.

It is an:

> **Adaptive Organizational Intelligence System powered by Vector Search, Knowledge Graphs, and Advanced RAG.**

The system dynamically decides:

```text
HOW TO SEARCH

WHAT TO RETRIEVE

WHEN TO USE ADVANCED RAG

WHEN TO EXPLORE RELATIONSHIPS

WHEN TO RETRIEVE AGAIN
```

---

# 🚀 Future Enhancements

* Multi-agent architecture
* Real-time document updates
* Graph visualization dashboard
* Organizational risk prediction
* Automated dependency analysis
* Team intelligence
* Historical trend analysis
* Role-based access control
* Enterprise authentication
* Cloud deployment
* Real-time collaboration

---

# 👩‍💻 Author

**Suguna Jayaram**

Senior Software Engineer | React Developer | AI Engineering Enthusiast

---

# ⭐ Final Vision

```text
                ORGPULSE AI

      Understand Organization Knowledge

                  ↓

         Discover Relationships

                  ↓

           Detect Risks

                  ↓

        Identify Dependencies

                  ↓

        Adapt Retrieval Strategy

                  ↓

          Provide Evidence

                  ↓

            Intelligent Answer
```

> **"From Documents to Organizational Intelligence."**

🚀 **Built with Adaptive RAG + GraphRAG + Advanced Retrieval**
