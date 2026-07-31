from services.database import criar_banco
from core.executor import executar_pipeline


def main():

    criar_banco()

    df = executar_pipeline()

    print(df.head())


if __name__ == "__main__":
    main()