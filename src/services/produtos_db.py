import sqlite3

from config import DATABASE_PATH


def listar_produtos():

    conexao = sqlite3.connect(DATABASE_PATH)

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, categoria
        FROM produtos
        ORDER BY nome
    """)

    produtos = cursor.fetchall()

    conexao.close()

    return [
        {
            "nome": nome,
            "categoria": categoria
        }
        for nome, categoria in produtos
    ]


def inserir_produto(nome, categoria):

    conexao = sqlite3.connect(DATABASE_PATH)

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO produtos(nome, categoria)
        VALUES(?, ?)
        """,
        (nome, categoria)
    )

    conexao.commit()

    conexao.close()


def excluir_produto(nome):

    conexao = sqlite3.connect(DATABASE_PATH)

    cursor = conexao.cursor()

    cursor.execute(
        """
        DELETE FROM produtos
        WHERE nome=?
        """,
        (nome,)
    )

    conexao.commit()

    conexao.close()