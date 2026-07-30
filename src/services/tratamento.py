import pandas as pd
from datetime import datetime

def transformar_dados(resposta_api):

    produtos = resposta_api.get("products", [])

    if not produtos:
        return pd.DataFrame()

    registros = []

    for produto in produtos:

        registros.append({

            "data_coleta": datetime.now(),

            "produto": produto["title"],

            "categoria": produto["category"],

            "marca": produto.get("brand"),

            "preco": produto["price"],

            "avaliacao": produto["rating"],

            "estoque": produto["stock"],

            "origem": "DummyJSON"

        })

    return pd.DataFrame(registros)