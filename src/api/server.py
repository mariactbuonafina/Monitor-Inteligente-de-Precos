from fastapi import FastAPI

from core.executor import executar_pipeline

app = FastAPI(
    title="Monitor Inteligente de Produtos"
)


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