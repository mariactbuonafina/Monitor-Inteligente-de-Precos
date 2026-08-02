import sqlite3
from config import DATABASE_PATH

def criar_banco():

    conexao = sqlite3.connect(DATABASE_PATH)

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome TEXT NOT NULL,

            categoria TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico_precos(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            produto TEXT NOT NULL,

            categoria TEXT,

            preco REAL,

            avaliacao REAL,

            data_coleta TEXT
        )
    """)

    conexao.commit()

    conexao.close()