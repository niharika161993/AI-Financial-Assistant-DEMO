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
