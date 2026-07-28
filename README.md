# AI-Financial-Assistant-DEMO

-----------------------------
brew --version

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### install ollama

brew install ollama
ollama --version

## Start Ollama

ollama serve
output - Listening on 127.0.0.1:11434

## wait 
ollama pull llama3.2

## check 
ollama list

## activate
cd AI-Financial-Assistant
source venv/bin/activate

## install 
pip install langchain-community

## from app folder run 
uvicorn app:app --reload

Uvicorn running on http://127.0.0.1:8000
http://127.0.0.1:8000/docs
POST /chat

## question 


{
  "question": "What was the company's revenue?"
}

### TREE STRUCTURE 


annual_report.pdf
        ↓
PDF Loader
        ↓
Embeddings
        ↓
ChromaDB
        ↓
RAG Search
        ↓
Llama 3.2 (Local AI)
        ↓
FastAPI Response
