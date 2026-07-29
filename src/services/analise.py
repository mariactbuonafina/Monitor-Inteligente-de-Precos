from pathlib import Path

def gerar_relatorio(df):

    pasta = Path("relatorios")
    pasta.mkdir(exist_ok=True)

    with open(
        pasta / "resumo.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write("=== RESUMO DA COLETA ===\n\n")

        arquivo.write(f"Total de registros: {len(df)}\n")

        arquivo.write(
            f"Colunas: {', '.join(df.columns)}\n"
        )

        arquivo.write(
            f"Última coleta: {df['data_coleta'].max()}\n"
        )

        arquivo.write(
            f"Tipos de feriado: {df['tipo'].nunique()}\n"
        )