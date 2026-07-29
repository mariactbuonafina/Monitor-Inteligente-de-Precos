import json

from config import PRODUTOS_JSON


def carregar_produtos():

    with open(PRODUTOS_JSON, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)