import requests

URL = "https://fakestoreapi.com/products"

def obter_produtos():
    resposta = requests.get(URL, timeout=10)

    resposta.raise_for_status()

    return resposta.json()