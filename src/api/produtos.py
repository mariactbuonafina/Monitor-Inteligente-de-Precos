import requests

from config import BASE_URL


def buscar_produto(nome_produto):

    resposta = requests.get(
        BASE_URL,
        params={"q": nome_produto},
        timeout=10
    )

    resposta.raise_for_status()

    return resposta.json()