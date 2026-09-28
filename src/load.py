from pathlib import Path
import sqlite3

def carregar_no_banco(fato_df, dim_clientes, dim_produtos):
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect("data/processed/olist.db")
    fato_df.to_sql("fato_pedidos", con, if_exists="replace", index=False)
    dim_clientes.to_sql("dim_clientes", con, if_exists="replace", index=False)
    dim_produtos.to_sql("dim_produtos", con, if_exists="replace", index=False)
    con.close()