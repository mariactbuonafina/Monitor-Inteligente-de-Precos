from api.brasilapi import obter_feriados
from core.pipeline import Pipeline


def main():

    dados = obter_feriados()

    pipeline = Pipeline()

    df = pipeline.executar(dados)

    print(df.head())


if __name__ == "__main__":
    main()