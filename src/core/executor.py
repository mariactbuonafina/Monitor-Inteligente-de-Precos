import pandas as pd

from api.produtos import buscar_produto
from services.produtos import carregar_produtos
from services.tratamento import transformar_dados
from core.pipeline import Pipeline


def executar_pipeline():

    produtos = carregar_produtos()

    dataframes = []

    for produto in produtos:

        resposta = buscar_produto(produto["nome"])

        df = transformar_dados(resposta)

        if not df.empty:
            dataframes.append(df)

    if not dataframes:
        return None

    df_final = pd.concat(
        dataframes,
        ignore_index=True
    )

    Pipeline().executar(df_final)

    return df_final