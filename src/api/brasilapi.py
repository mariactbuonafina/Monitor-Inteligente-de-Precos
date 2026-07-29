import requests
from config import BRASIL_API_FERIADOS


def obter_feriados():
    resposta = requests.get(BRASIL_API_FERIADOS, timeout=10)
    resposta.raise_for_status()
    return resposta.json()