import pandas as pd
import os

PRODUTOS_PATH = "data/produtos.csv"

def adicionar_produto(nome, preco):
    produto = pd.DataFrame([[nome, preco]], columns=["Produto", "Preço"])
    if os.path.exists(PRODUTOS_PATH):
        produto.to_csv(PRODUTOS_PATH, mode="a", header=False, index=False)
    else:
        produto.to_csv(PRODUTOS_PATH, index=False)

def listar_produtos():
    if os.path.exists(PRODUTOS_PATH):
        return pd.read_csv(PRODUTOS_PATH)
    return pd.DataFrame(columns=["Produto", "Preço"])
