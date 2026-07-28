# Interview Questions


## Explain your project.

Answer:

I built an AI-powered financial research assistant using Python, FastAPI, RAG architecture, ChromaDB, and Ollama. The system processes financial reports, converts documents into embeddings, retrieves relevant information using semantic search, and generates context-aware answers.


---

## Why did you use RAG?

RAG improves accuracy by grounding the LLM response with retrieved information from the source documents.


---

## Why vector database?

Traditional databases search exact keywords.

Vector databases perform semantic search based on meaning.


---

## Challenges

1. Processing large documents

Solution:

Used embeddings and chunk-based retrieval.


2. Reducing incorrect answers

Solution:

Used RAG to provide relevant context before generation.
