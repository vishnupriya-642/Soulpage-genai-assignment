import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq



load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found. Please check your .env file.")
    st.stop()


KNOWLEDGE_FILE = "knowledge.txt"
MEMORY_FILE = "memory.txt"


if os.path.exists(KNOWLEDGE_FILE):
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
        knowledge = f.read()
else:
    knowledge = "No external knowledge provided."


if "history" not in st.session_state:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            st.session_state.history = f.read()
    else:
        st.session_state.history = ""


llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=0,
    api_key=GROQ_API_KEY
)


st.title("Conversational Knowledge Bot")

user_input = st.text_input("Ask a question:")

if user_input:
    prompt = f"""
You are a conversational knowledge assistant.

Use the provided knowledge when relevant.
Remember the conversation history.

Knowledge:
{knowledge}

Conversation History:
{st.session_state.history}

Human: {user_input}
AI:
"""

    response = llm.invoke(prompt).content

   
    st.session_state.history += f"\nHuman: {user_input}\nAI: {response}\n"

    
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        f.write(st.session_state.history)

    st.write(response)
