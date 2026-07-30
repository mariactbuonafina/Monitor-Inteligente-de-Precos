import pandas as pd

from api.produtos import buscar_produto
from services.produtos import carregar_produtos
from services.tratamento import transformar_dados
from core.pipeline import Pipeline


def main():

    produtos = carregar_produtos()

    dataframes = []

    for produto in produtos:

        resposta = buscar_produto(produto["nome"])

        df = transformar_dados(resposta)

        if not df.empty:
            dataframes.append(df)

    if not dataframes:

        print("Nenhum produto encontrado.")

        return

    df_final = pd.concat(
        dataframes,
        ignore_index=True
    )

    pipeline = Pipeline()

    pipeline.executar(df_final)

    print(df_final.head())


if __name__ == "__main__":
    main()