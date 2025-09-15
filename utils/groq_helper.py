from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
import streamlit as st

def consultar_groq(pergunta, contexto):
    llm = ChatGroq(
        groq_api_key=st.secrets["GROQ_API_KEY"],
        model="llama3-8b-8192"
    )
    system_message = SystemMessage(content=contexto)
    human_message = HumanMessage(content=pergunta)
    resposta = llm.invoke([system_message, human_message])
    return resposta.content
