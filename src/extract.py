from pathlib import Path
import pandas as pd

RAW = Path("data/raw")
TABELAS_ESPERADAS = [
    "orders",
    "order_items",
    "products",
    "customers",
    "order_payments",
    "order_reviews",
    "sellers",
]

def carregar_tabelas():
    dados = {}
    for nome in TABELAS_ESPERADAS:
        arquivo = RAW / f"olist_{nome}_dataset.csv"
        assert arquivo.exists(), f"Faltando: {arquivo}"
        dados[nome] = pd.read_csv(arquivo)
    return dados