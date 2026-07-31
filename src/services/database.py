import sqlite3

from config import DADOS_DIR

DB_PATH = DADOS_DIR / "monitor.db"


def conectar():
    return sqlite3.connect(DB_PATH)


def criar_banco():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT
        )
    """)

    conexao.commit()
    conexao.close()