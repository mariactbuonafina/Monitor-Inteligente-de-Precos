from services.database import conectar

def inserir_produto(nome, categoria=None):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO produtos
        (nome, categoria)
        VALUES (?, ?)
        """,
        (nome, categoria)
    )

    conexao.commit()

    conexao.close()