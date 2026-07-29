import pandas as pd

dados = pd.read_csv("dados/precos.csv")

print("=" * 50)
print("DataFrame completo")
print(dados)

print("=" * 50)
print("Primeiras linhas")
print(dados.head())

print("=" * 50)
print("Últimas linhas")
print(dados.tail())

print("=" * 50)
print(dados.info())

print("=" * 50)
print(dados.describe())