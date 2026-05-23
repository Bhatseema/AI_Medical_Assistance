
---

# MedAI Clinical Decision System

```md
# MedAI Clinical Decision System

An AI-powered healthcare assistant that analyzes medical documents and answers clinical queries using Retrieval-Augmented Generation (RAG).

## Features
- Medical PDF Analysis
- AI Clinical Question Answering
- Context-aware Responses
- FAISS Semantic Search
- Groq LLaMA 3 Integration
- Streamlit Interactive UI

## Tech Stack
- Python
- Streamlit
- FastAPI
- LangChain
- FAISS
- Groq API
- Sentence Transformers

## Workflow
1. Upload Medical PDF
2. Extract Text
3. Generate Embeddings
4. Store in FAISS
5. Retrieve Relevant Context
6. Generate AI Response

## Installation

```bash
pip install -r requirements.txt
Run Backend
uvicorn main:app --reload
Run Frontend
streamlit run app.py
API Endpoints
Upload PDF
POST /upload
Ask Question
POST /ask
Future Enhancements
Multi-language Support
Voice Assistant
Hospital Integration
Patient History Tracking
Disclaimer

This system is for educational and research purposes only and is not a replacement for professional medical advice.

Author

Seema Bhat
