import streamlit as st
import pandas as pd
from views import cadastro_produto, carrinho, dashboard, assistente_ia

st.set_page_config(page_title="Loja Sofia", layout="centered")

st.title("Bem-vindo à Loja Sofia")
st.write("Explore nossos produtos, faça compras e interaja com nosso assistente virtual.")

st.sidebar.title("Menu")
pagina = st.sidebar.radio("Escolha uma opção:", ["Produtos", "Carrinho", "Dashboard", "Assistente Virtual"])

if pagina == "Produtos":
    cadastro_produto.exibir_produtos()
elif pagina == "Carrinho":
    carrinho.exibir_carrinho()
elif pagina == "Dashboard":
    dashboard.exibir_dashboard()
elif pagina == "Assistente Virtual":
    assistente_ia.interagir_com_assistente()
