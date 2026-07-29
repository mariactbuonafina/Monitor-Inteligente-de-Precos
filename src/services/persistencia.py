import pandas as pd

from config import (
    DADOS_DIR,
    FERIADOS_CSV,
    HISTORICO_CSV
)


def salvar_csv(df):

    DADOS_DIR.mkdir(exist_ok=True)

    # Estado atual
    df.to_csv(
        FERIADOS_CSV,
        index=False,
        encoding="utf-8"
    )

    # Histórico
    if HISTORICO_CSV.exists():

        historico = pd.read_csv(HISTORICO_CSV)

        historico = pd.concat(
            [historico, df],
            ignore_index=True
        )

    else:

        historico = df

    historico.to_csv(
        HISTORICO_CSV,
        index=False,
        encoding="utf-8"
    )