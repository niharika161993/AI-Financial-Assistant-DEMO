# Technology Explanation


# Python

Used as the primary programming language.

Reasons:

- Large AI ecosystem
- Easy integration with ML libraries
- Fast development


---

# FastAPI

Purpose:

Creates REST APIs.

Example:

POST /chat


User sends:

{
"question":"What was revenue?"
}


API returns:

{
"answer":"Revenue was..."
}


Advantages:

- Fast
- Lightweight
- Automatic Swagger documentation


---

# LangChain

Purpose:

Framework for building LLM applications.

Used for:

- Document loading
- Embeddings
- Vector search
- LLM integration


---

# ChromaDB

Purpose:

Vector database.


Stores:

Document embeddings


Used for:

Semantic search


---

# HuggingFace Embeddings

Purpose:

Convert text into numerical vectors.


Example:


Text:

"Company profit increased"


Vector:

[0.234,0.556,0.789]


---

# Ollama

Purpose:

Runs local Large Language Models.


Model used:

Llama 3.2


Advantages:

- Free
- No API key
- Runs locally


---

# PyPDF

Purpose:

Extract text from PDF documents.
