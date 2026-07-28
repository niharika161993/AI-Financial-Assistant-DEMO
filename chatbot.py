from langchain_community.llms import Ollama


llm = Ollama(
    model="llama3.2"
)


def ask_question(db, question):

    docs = db.similarity_search(question, k=3)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response
