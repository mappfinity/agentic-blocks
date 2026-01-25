# Local LangChain AI Demos

A bunch of concise, production-ready examples showcasing **local LLM applications with LangChain, LangGraph, Ollama, vector databases (Chroma, FAISS, ...) and more**.


## 1. [🔬 Research Synthesizer Assistant](langchain/research-synthesizer/Research-Synthesizer-Demo-LangChain-v1-Ollama-FAISS.ipynb)

![Overview](langchain/research-synthesizer/img/research-synthesizer.png)

**AI-powered research assistant that synthesizes comprehensive answers from multiple sources.**

## Features
- 📂 **Local Documents**: Index and search PDFs/TXT files via FAISS vector database
- 📚 **arXiv Papers**: Automatic academic paper retrieval and analysis
- 🌐 **Web Search**: Real-time information via Tavily API (optional)
- 🤖 **Smart RAG Pipeline**: HuggingFace embeddings + cross-encoder reranking
- 💬 **Modern UI**: Gradio interface with collapsible sidebar and report management

## Tech Stack
- **LLM**: Ollama (Qwen, Mistral) via LangChain/LangGraph
- **Vector DB**: FAISS with `all-MiniLM-L6-v2` embeddings
- **Reranking**: Cross-encoder `ms-marco-MiniLM-L-6-v2`
- **Interface**: Gradio 6.1+

## Quick Start
1. Place documents in `./research_docs`
2. Configure `CONFIG` dictionary (model, API keys, retrieval settings)
3. Run the app - it auto-indexes documents and launches web UI
4. Ask research questions - reports saved to `./report_docs`

*Research tool for educational purposes. Verify important information from primary sources.*

---

## 4. [Piper TTS Voice Showcase](piper-tts-demo/piper-tts-demo.ipynb)
Interactive demo of 4 high-quality neural TTS voices with 904 LibriTTS speaker variants.

**Highlights**
- 🎙️ 4 voice models (Heather, Michael, Lessac, LibriTTS)
- 🎚️ 904 unique speakers in LibriTTS multi-speaker model
- 🔧 Smart preprocessing (tables, citations, markdown cleanup)
- 🎵 Auto-generate & cache WAV files locally
- 📊 Table linearization for natural speech rendering
- 🔄 Interactive player with voice/speaker selection

**Voice Samples:**
### Heather
*Natural, conversational female voice (medium quality)*

📥 [Download heather.wav](wav/heather.wav) *(~500KB)*

### Michael
*Balanced, natural male voice (medium quality)*

📥 [Download mike.wav](wav/mike.wav) *(~500KB)*

*Audio players available in the interactive notebook*

**Use cases:** local TTS synthesis, voice comparison, accessibility tools, audio content generation.

---
## 3. [Chatbot Assistant with Persistent Memory](chatbot-with-memory/Chatbot-with-Memory-and-Tools-Demo-w-LangChain-v1-Ollama-Gradio.ipynb)

![Overview](chatbot-with-memory/img/cba-with-memory.png)

A fully local, tool-enabled chatbot with session-isolated, persistent memory.

**Highlights**
- 🧠 Persistent memory via LangGraph `MemorySaver`
- 🔧 Tool calling (Wikipedia, Tavily, custom tools)
- 🤖 Local LLMs via Ollama (e.g. `qwen2.5:3b`)
- 🎨 Gradio UI with session state
- 🔒 Privacy-first, offline-capable

**Use cases:** personal assistants, research bots, privacy-sensitive apps.

---

## 4. [LangChain RAG](rag-demo/RAG-Demo-w-LangChain-v1-Ollama.ipynb)
A lightweight Retrieval-Augmented Generation (RAG) pipeline for grounded Q&A.

**Highlights**
- 📚 In-memory vector store with semantic search
- ✂️ Automatic document chunking + embeddings
- 🤖 Ollama-powered LLM (Mistral 7B)
- 💬 Single-turn and multi-turn chat modes
- 🧩 Pluggable embeddings (HF or fallback)

**Use cases:** document Q&A, knowledge assistants, RAG prototyping.

---

## Tech Stack
- LangChain (v1.0+)
- Ollama (local LLM inference)
- Gradio (chat UI)
- HuggingFace embeddings (optional)

**Goal:** demonstrate clean, modern patterns for building **local, private, LLM-powered systems** with memory, tools, and retrieval.

