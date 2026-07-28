# System Architecture


                 User
                   |
                   |
             FastAPI API
                   |
                   |
             User Question
                   |
                   |
          Vector Similarity Search
                   |
                   |
              ChromaDB
                   |
                   |
          Relevant Document Data
                   |
                   |
           Ollama Llama Model
                   |
                   |
              Final Answer


---

# Data Flow

## Step 1: PDF Upload

Input:

annual_report.pdf


Example:

Apple Annual Report


↓

## Step 2: Document Processing

PyPDF extracts:

- Text
- Pages
- Metadata


↓

## Step 3: Embedding Generation

Text is converted into vectors.


Example:

"Revenue increased"

becomes:

[0.23,0.56,0.89]


↓

## Step 4: Vector Storage

Stored inside ChromaDB.


↓

## Step 5: User Question

Example:

"What was revenue?"


↓

## Step 6: Similarity Search

Database finds related information.


↓

## Step 7: LLM Generation

Ollama generates final response.
