import sqlite3
import os
import pytest

DB_PATH = "data/processed/olist.db"

def test_database_exists():
    """Valida a existência do banco localmente ou pula se for no CI sem dados raw."""
    if not os.path.exists("data/raw"):
        pytest.skip("Dados raw não presentes no repositório remoto (ignorado no CI).")
    assert os.path.exists(DB_PATH), "O ficheiro olist.db não foi encontrado!"

def test_fato_pedidos_not_empty():
    """Valida registros na tabela fato se o banco existir."""
    if not os.path.exists(DB_PATH):
        pytest.skip("Ficheiro olist.db não presente para teste.")
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM fato_pedidos")
    count = cursor.fetchone()[0]
    assert count > 0, "A tabela fato_pedidos está vazia!"
    
    conn.close()