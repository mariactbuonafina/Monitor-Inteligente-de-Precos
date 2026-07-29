import pandas as pd
from datetime import datetime


def transformar_feriados(dados_api):

    df = pd.DataFrame(dados_api)

    df = df.rename(columns={
        "date": "data",
        "name": "feriado",
        "type": "tipo"
    })

    df["data_coleta"] = datetime.now()

    return df