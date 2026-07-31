from core.executor import executar_pipeline


def main():

    df = executar_pipeline()

    if df is None:
        print("Nenhum produto encontrado.")
        return

    print(df.head())


if __name__ == "__main__":
    main()