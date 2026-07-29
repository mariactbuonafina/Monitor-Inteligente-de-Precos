from datetime import datetime
import csv

data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

dados = [
    ["data_coleta", "produto", "categoria", "preco", "loja"],
    [data_atual, "Mouse Gamer", "Periféricos", 129.90, "Loja Tech"],
    [data_atual, "Teclado Mecânico", "Periféricos", 299.90, "Loja Tech"],
    [data_atual, "Monitor 24", "Monitores", 899.90, "Loja Digital"],
]

with open("dados/precos.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print("Arquivo CSV criado com sucesso!")