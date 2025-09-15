import pandas as pd
import os

VENDAS_PATH = "data/vendas.csv"

def registrar_venda(produto, quantidade, preco_unitario):
    venda = pd.DataFrame([[produto, quantidade, preco_unitario, quantidade * preco_unitario]],
                         columns=["Produto", "Quantidade", "Preço Unitário", "Total"])
    if os.path.exists(VENDAS_PATH):
        venda.to_csv(VENDAS_PATH, mode="a", header=False, index=False)
    else:
        venda.to_csv(VENDAS_PATH, index=False)

def listar_vendas():
    if os.path.exists(VENDAS_PATH):
        return pd.read_csv(VENDAS_PATH)
    return pd.DataFrame(columns=["Produto", "Quantidade", "Preço Unitário", "Total"])
