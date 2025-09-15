import streamlit as st
from views import cadastro_produto, dashboard, assistente_ia, carrinho

st.set_page_config(page_title="🛒 Loja Online", layout="wide")

st.sidebar.title("Menu")
pagina = st.sidebar.radio("Escolha:", ["Cadastro de Produtos", "Carrinho", "Dashboard", "Assistente IA"])

if pagina == "Cadastro de Produtos":
    cadastro_produto.exibir()
elif pagina == "Carrinho":
    carrinho.exibir()
elif pagina == "Dashboard":
    dashboard.exibir()
else:
    assistente_ia.exibir()
