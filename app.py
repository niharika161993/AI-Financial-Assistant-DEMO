
from fastapi import FastAPI
from pydantic import BaseModel

from document_loader import load_pdf
from embeddings import get_embedding
from vector_store import create_vector_db, load_db
from chatbot import ask_question


app = FastAPI(
    title="AI Financial Research Assistant",
    description="RAG-based chatbot for financial documents",
    version="1.0"
)


# Load document and create vector database
print("Loading financial document...")

documents = load_pdf("data/annual_report.pdf")

print(f"Loaded {len(documents)} pages")


# Create embeddings
embedding_model = get_embedding()


# Create vector database
print("Creating vector database...")

create_vector_db(
    documents,
    embedding_model
)


# Load vector database
db = load_db(
    embedding_model
)

print("AI Assistant is ready!")


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Financial Research Assistant is running"
    }


@app.post("/chat")
def chat(query: Query):

    answer = ask_question(
        db,
        query.question
    )

    return {
        "question": query.question,
        "answer": answer
    }
