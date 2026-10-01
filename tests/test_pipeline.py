import sqlite3
import os
import pytest

DB_PATH = "data/processed/olist.db"

def test_database_exists():
    """Garante que o banco de dados SQLite foi gerado."""
    assert os.path.exists(DB_PATH), "O ficheiro olist.db não foi encontrado!"

def test_fato_pedidos_not_empty():
    """Valida se a tabela fato possui registros e sem valores nulos na chave."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM fato_pedidos")
    count = cursor.fetchone()[0]
    assert count > 0, "A tabela fato_pedidos está vazia!"
    
    cursor.execute("SELECT COUNT(*) FROM fato_pedidos WHERE order_id IS NULL")
    null_orders = cursor.fetchone()[0]
    assert null_orders == 0, "Existem order_id nulos na fato_pedidos!"
    
    conn.close()