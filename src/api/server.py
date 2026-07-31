from fastapi import FastAPI
from core.executor import executar_pipeline
from pydantic import BaseModel
from services.produtos_db import (
    inserir_produto,
    listar_produtos
)

app = FastAPI(
    title="Monitor Inteligente de Produtos"
)

class Produto(BaseModel):

    nome: str

    categoria: str

@app.get("/")
def home():

    return {
        "status": "Servidor funcionando."
    }


@app.get("/executar")
def executar():

    df = executar_pipeline()

    if df is None:

        return {
            "status": "Nenhum produto encontrado."
        }

    return {
        "status": "Pipeline executado com sucesso.",
        "produtos": len(df)
    }
    
@app.post("/produtos")
def cadastrar_produto(produto: Produto):

    inserir_produto(
        produto.nome,
        produto.categoria
    )

    return {
        "mensagem": "Produto cadastrado com sucesso."
    }

@app.get("/produtos")
def obter_produtos():

    return listar_produtos()