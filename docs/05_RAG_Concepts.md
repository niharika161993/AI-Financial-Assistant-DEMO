# Retrieval Augmented Generation (RAG)


## What is RAG?

RAG combines:

1. Information Retrieval
2. Language Generation


Instead of asking AI directly:


User Question

↓

LLM

↓

Answer


RAG does:


User Question

↓

Search Documents

↓

Retrieve Relevant Information

↓

Send Context + Question

↓

LLM

↓

Answer


---

## Why use RAG?

Advantages:

- Reduces hallucination
- Uses private documents
- Provides accurate answers
- Keeps information updated


---

## RAG Components


Retriever:

Finds relevant documents


Generator:

Creates final response
