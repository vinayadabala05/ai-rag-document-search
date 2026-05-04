# AI RAG Document Search

An AI-powered document question-answering system built using Retrieval-Augmented Generation (RAG). This project enables users to query documents using semantic search and receive context-aware responses powered by Large Language Models (LLMs).

---

## 🚀 Features

- Retrieval-Augmented Generation (RAG) pipeline  
- Embedding-based semantic search using FAISS  
- Context-aware response generation using LLM  
- End-to-end pipeline: ingestion → chunking → retrieval → generation  

---

## 🏗️ Architecture

User Query → FAISS Vector Search → Retrieve Relevant Chunks → LLM → Final Answer  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- FAISS (Vector Database)  
- OpenAI API  
- PyPDF  

---

## ⚙️ How It Works

1. Load PDF document  
2. Split text into smaller chunks  
3. Convert chunks into vector embeddings  
4. Store embeddings in FAISS  
5. Perform semantic search on user query  
6. Retrieve relevant context  
7. Generate final response using LLM  

---

## 📦 Setup

1. Clone the repository
