# 🎓 MCQ Generator using Groq LLM

An AI-powered web application that generates **high-quality multiple-choice questions (MCQs)**, **document summaries**, and **learning guides** from **PDFs or raw text** using **Groq Cloud LLMs**.  
Designed to simulate **human-level exam question creation** with adjustable difficulty and a clean, interactive quiz interface.

---

## 🚀 Project Overview

This project transforms unstructured educational content (PDFs or text) into a **complete learning and assessment experience**:

- Upload a **PDF** or paste **text**
- Choose **difficulty level** (Easy / Medium / Hard)
- Generate **context-aware MCQs**
- Attempt the quiz interactively
- Export the quiz as a **PDF**
- Get a **summary + curated learning roadmap**

The system leverages **Groq’s ultra-fast inference** with **LLaMA 3.3 (70B)** to ensure high contextual accuracy and low latency.

---

## 🧠 Key Features

- 📄 **PDF Upload & Text Parsing**
- ✍️ **Human-like MCQ Generation**
- 🎯 **Difficulty Control** (Easy / Medium / Hard)
- 📝 **Interactive Clickable Quiz UI**
- 📌 **Concise Document Summary**
- 📚 **Learning Guide & Resource Suggestions**
- 📤 **Export Quiz as PDF**
- ⚡ **Fast Response Time (< 5 seconds)**

---

## 🏗️ Tech Stack & Tools

### Backend
- **Python**
- **Flask** – Web framework
- **Groq Cloud API**
- **LLaMA 3.3 70B Versatile** (LLM)

### Frontend
- **HTML5**
- **CSS3** (custom responsive styling)

### NLP & Utilities
- **Prompt Engineering**
- **PyPDF2** – PDF text extraction
- **Regex-based MCQ parsing**
- **ReportLab** – PDF export

### Dev & Deployment
- **Git & GitHub**
- **Virtual Environment (venv)**
- **REST-style architecture**

---
---

## 📊 Performance Metrics (Observed)

- **Contextual Accuracy:** ~87% (manual evaluation on academic PDFs)
- **Average Response Time:** 3–5 seconds
- **MCQ Quality:** Conceptual & reasoning-based (not shallow recall)
- **Scalability:** Supports user-defined number of questions

> Note: Accuracy is based on qualitative evaluation of relevance, correctness, and conceptual depth.

---

## 🧪 Example Use Cases

- 📘 Generating quizzes from **research papers**
- 🎓 Exam preparation from **lecture notes**
- 🧠 Self-assessment while learning **ML / NLP / CS topics**
- 🏫 Faculty or coaching material generation
- 📄 Quick understanding of long PDFs

---

🚀 Future Enhancements

Auto-evaluation & scoring

Timer-based quizzes

User authentication & quiz history

Deployment on Render / AWS

Chunking for very large PDFs

Analytics dashboard

