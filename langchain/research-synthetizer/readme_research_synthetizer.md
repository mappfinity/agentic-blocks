# 🔬 Research Synthetizer

A powerful AI-powered research assistant that synthesizes comprehensive answers from multiple sources including local documents, arXiv papers, and web search. Built with LangChain, LangGraph, and Gradio for an intuitive research experience.

## ✨ Features

- **Multi-Source Research**: Combines information from:
  - 📂 Local documents (PDF, TXT)
  - 📚 arXiv academic papers
  - 🌐 Web search (via Tavily API)

- **Advanced RAG Pipeline**:
  - FAISS vector database for efficient semantic search
  - Cross-encoder reranking for improved retrieval accuracy
  - HuggingFace embeddings for document indexing
  - Configurable retrieval parameters (top-k, temperature)

- **Modern Web Interface**:
  - Clean, responsive Gradio UI with collapsible sidebar
  - Real-time research status tracking
  - Automatic report generation and saving
  - Browse and reload previous research results
  - Active research topic display

- **Flexible LLM Support**:
  - Multiple model options (Qwen, Mistral, GPT-OSS)
  - Runs locally via Ollama
  - Configurable context window and temperature

- **Research Management**:
  - Automatic markdown report generation with timestamps
  - Organized report storage
  - Load and review previous research
  - Clear chat functionality

## 🏗️ Architecture

### Tech Stack

- **LLM Framework**: LangChain v1 with LangGraph for orchestration
- **Vector Database**: FAISS for similarity search
- **Embeddings**: HuggingFace `all-MiniLM-L6-v2`
- **Reranking**: Cross-encoder `ms-marco-MiniLM-L-6-v2`
- **LLM Backend**: Ollama (local inference)
- **Web Interface**: Gradio 6.1+
- **Document Processing**: PyPDFLoader, TextLoader, RecursiveCharacterTextSplitter
- **Search APIs**: ArxivAPIWrapper, TavilySearchAPIRetriever

### Core Components

1. **ResearchSynthetizer**: Main orchestrator handling research workflow
2. **FAISS Vector Store**: Semantic search over local documents
3. **LangGraph State Machine**: Manages multi-step research process
4. **Cross-Encoder Reranker**: Improves retrieval relevance
5. **Gradio Interface**: User-facing web application

## 📋 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- Downloaded LLM models via Ollama (e.g., `ollama pull qwen2.5:3b`)

## 🚀 Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd research-synthetizer
```

2. **Install dependencies**
```bash
pip install gradio langchain langchain-ollama langchain-community langchain-huggingface
pip install sentence-transformers faiss-cpu arxiv
pip install tavily-python  # Optional, for web search
```

3. **Install and start Ollama**
```bash
# Download from https://ollama.ai/
# Pull desired models
ollama pull qwen2.5:3b
ollama pull mistral:7b
```

4. **Set up directory structure**
```bash
mkdir -p research_docs report_docs vector_db
```

## ⚙️ Configuration

Edit the `CONFIG` dictionary in your main script:

```python
CONFIG = {
    # LLM Configuration
    "model_name": "qwen2.5:3b",  # or "mistral:7b", "gpt-oss:20b"
    "temperature": 0.2,
    "context_window": 8192,
    
    # Embedding Models
    "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
    "reranker_model": "cross-encoder/ms-marco-MiniLM-L-6-v2",
    
    # API Keys
    "tavily_api_key": None,  # Add your Tavily API key for web search
    
    # Directories
    "faiss_dir": "./vector_db",
    "docs_dir": "./research_docs",
    "reports_dir": "./report_docs",
    
    # Retrieval Settings
    "use_reranking": True,
    "top_k_initial": 30,  # Initial retrieval count
    "top_k_final": 7,     # After reranking
}
```

### Configuration Options

- **model_name**: Ollama model to use for generation
- **embedding_model**: HuggingFace model for document embeddings
- **reranker_model**: Cross-encoder for result reranking
- **tavily_api_key**: API key for web search (optional)
- **use_reranking**: Enable/disable cross-encoder reranking
- **top_k_initial**: Number of documents to retrieve before reranking
- **top_k_final**: Number of documents to keep after reranking
- **temperature**: LLM sampling temperature (0.0 = deterministic, 1.0 = creative)
- **context_window**: Maximum context length for the LLM

## 🎯 Usage

1. **Add documents to research**
   - Place PDF or TXT files in `./research_docs`
   - The system will automatically index them on startup

2. **Start the application**
```bash
python app.py
```

3. **Open in browser**
   - Navigate to the URL shown in terminal (e.g., `http://127.0.0.1:7860`)

4. **Conduct research**
   - Enter your research question in the text box
   - Click "🔍 Research" or press Enter
   - Watch as the system synthesizes information from multiple sources

5. **Manage results**
   - Reports are automatically saved to `./report_docs` with timestamps
   - Use "📂 Saved Research Results" dropdown to load previous research
   - Click "🗑️ Clear Chat" to start fresh

## 📁 Project Structure

```
research-synthetizer/
├── app.py                    # Main application file
├── research_docs/            # Local documents for indexing
├── report_docs/              # Generated research reports
├── vector_db/                # FAISS vector database
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```

## 🔍 How It Works

1. **Document Indexing**:
   - Local documents are chunked and embedded
   - Stored in FAISS vector database for quick retrieval

2. **Query Processing**:
   - User query is embedded and matched against vector database
   - ArXiv papers are searched for relevant research
   - Web search provides current information (if Tavily enabled)

3. **Reranking** (optional):
   - Retrieved documents are reranked using cross-encoder
   - Most relevant documents are selected

4. **Synthesis**:
   - LLM generates comprehensive answer using retrieved context
   - Response includes citations and sources

5. **Report Generation**:
   - Answer is formatted as markdown
   - Saved with timestamp and query title

## 🎨 UI Features

- **Collapsible Sidebar**: Toggle with ◀/▶ button for more screen space
- **Active Research Display**: Shows current query being processed
- **Status Indicator**: Real-time system status updates
- **Report Browser**: Access and reload previous research sessions
- **Modern Design**: Clean, responsive interface with gradient styling

## 🔧 Troubleshooting

**Port already in use**
- The app auto-finds available ports starting from 7860

**Ollama connection error**
- Ensure Ollama is running: `ollama serve`
- Verify model is downloaded: `ollama list`

**Slow performance**
- Reduce `context_window` for faster inference
- Use smaller models (qwen2.5:3b instead of 20b)
- Disable reranking by setting `use_reranking: False`

**No web search results**
- Add your Tavily API key to config
- Get free key at [tavily.com](https://tavily.com)

## 📝 Example Queries

- "What are the latest developments in transformer architectures?"
- "Explain quantum computing for beginners"
- "Compare different approaches to few-shot learning"
- "What are the ethical implications of large language models?"

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional document loaders (DOCX, HTML, etc.)
- More LLM backend options (OpenAI, Anthropic, etc.)
- Enhanced citation formatting
- Multi-language support
- Export to different formats (PDF, DOCX)

## 📄 License

[Your License Here]

## 🙏 Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain)
- UI powered by [Gradio](https://github.com/gradio-app/gradio)
- Local inference via [Ollama](https://ollama.ai/)
- Embeddings from [HuggingFace](https://huggingface.co/)

---

**Note**: This tool is for research and educational purposes. Always verify important information from primary sources.