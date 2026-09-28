from extract import carregar_tabelas
from transform import tratar_pedidos
from load import carregar_no_banco

def main():
    print("Extraindo dados...")
    dados = carregar_tabelas()

    print("Transformando dados...")
    fato = tratar_pedidos(
        dados["orders"],
        dados["order_items"],
        dados["order_payments"],
        dados["order_reviews"],
    )

    dim_clientes = dados["customers"]
    dim_produtos = dados["products"]

    print("Carregando no banco SQLite...")
    carregar_no_banco(fato, dim_clientes, dim_produtos)
    print("ETL concluído com sucesso! Banco SQLite gerado em data/processed/")

if __name__ == "__main__":
    main()