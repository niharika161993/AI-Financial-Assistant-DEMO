# Setup Guide


## Requirements

Install:

- Python 3.11+
- Ollama


---

## Install Dependencies


pip install -r requirements.txt


---

## Start Ollama


ollama serve


---

## Download Model


ollama pull llama3.2


---

## Run Application


uvicorn app:app --reload


---

## Open Browser


http://127.0.0.1:8000/docs


---

## Test API


POST /chat


Example:


{
"question":"What was revenue?"
}
