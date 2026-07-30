import pandas as pd
from pandas.errors import EmptyDataError

from config import PRECOS_CSV, HISTORICO_CSV


def salvar_csv(df):

    df.to_csv(
        PRECOS_CSV,
        index=False,
        encoding="utf-8"
    )

    try:

        historico = pd.read_csv(HISTORICO_CSV)

        historico = pd.concat(
            [historico, df],
            ignore_index=True
        )

    except (FileNotFoundError, EmptyDataError):

        historico = df

    historico.to_csv(
        HISTORICO_CSV,
        index=False,
        encoding="utf-8"
    )