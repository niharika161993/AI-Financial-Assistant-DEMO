# File Explanation


## app.py

Main application file.

Responsibilities:

- Creates FastAPI server
- Loads documents
- Initializes database
- Defines API endpoints


---

## document_loader.py

Responsible for reading PDF files.


Input:

annual_report.pdf


Output:

Document objects


---

## embeddings.py

Creates text embeddings.

Uses:

HuggingFace sentence transformer


---

## vector_store.py

Manages ChromaDB.

Responsibilities:

- Create database
- Store embeddings
- Search documents


---

## chatbot.py

AI logic.

Responsibilities:

- Retrieve context
- Build prompt
- Generate answer using Llama
