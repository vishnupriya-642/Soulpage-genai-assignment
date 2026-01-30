# Conversational Knowledge Bot (LangChain + Groq)

## Overview
This project is a Conversational Knowledge Bot built using Streamlit and Groq LLM.
It can answer questions using a provided knowledge base and remember previous
conversation context across interactions.

## Features
- Conversational chat interface using Streamlit
- Uses Groq LLM for fast inference
- Maintains conversation memory using session state
- Persists memory across page refresh using a local file
- Uses external knowledge from a text file

## Tech Stack
- Python
- Streamlit
- LangChain (Groq integration)
- Groq LLM
- dotenv

## Project Structure
- main.py            : Entry point to run the application
- app.py             : Streamlit application logic
- knowledge.txt      : External knowledge base
- memory.txt         : Stores conversation history
- requirements.txt   : Project dependencies
- .env.example       : Environment variable template
- README.md          : Project documentation

- Setup Instructions
1. Clone the repository:
   git clone https://github.com/vishnupriya-642/Soulpage-genai-assignment.git

2. Navigate to the project directory:
   cd Soulpage-genai-assignment

3. Create and activate virtual environment:
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Create a .env file and add your Groq API key:
   GROQ_API_KEY=your_api_key_here

6. Run the application:
   streamlit run app.py

Example Queries
The following queries demonstrate factual answering and contextual conversation:

- Who is the CEO of OpenAI?
- Where did he study?
- When was OpenAI founded?
- What is LangChain?
- What did I ask you earlier?

These queries show the bot’s ability to answer factual questions and maintain
conversation context using memory.

Technologies Used
- Python
- Streamlit
- LangChain
- Groq LLM
- python-dotenv

Implementation Details
- The bot answers questions only from the provided knowledge base.
- Conversation memory is maintained using session state and a local file.
- The application runs locally as required in the assignment.


 






