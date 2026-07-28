# Code Execution Flow


Application starts:

app.py


|

Loads PDF

document_loader.py


|

Creates embeddings

embeddings.py


|

Stores vectors

vector_store.py


|

User sends question


|

chatbot.py receives question


|

Searches ChromaDB


|

Retrieves relevant document sections


|

Creates prompt


|

Sends prompt to Ollama


|

Returns answer
