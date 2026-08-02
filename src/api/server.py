from fastapi import FastAPI
from core.executor import executar_pipeline
from services.database import criar_banco
from services.produtos_db import (
    listar_produtos,
    inserir_produto,
    excluir_produto
)

app = FastAPI(
    title="Monitor de Preços",
    version="1.0"
)

criar_banco()


@app.get("/")
def home():

    return {
        "mensagem": "API Monitor de Preços"
    }


@app.get("/executar")
def executar():

    df = executar_pipeline()

    return {
        "status": "ok",
        "registros": len(df)
    }


@app.get("/produtos")
def produtos():

    return listar_produtos()


@app.post("/produtos")
def adicionar_produto(
    nome: str,
    categoria: str = ""
):

    inserir_produto(
        nome,
        categoria
    )

    return {
        "mensagem": "Produto cadastrado."
    }


@app.delete("/produtos/{nome}")
def remover_produto(nome: str):

    excluir_produto(nome)

    return {
        "mensagem": "Produto removido."
    }