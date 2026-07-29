import matplotlib.pyplot as plt
from config import GRAFICOS_DIR

GRAFICOS_DIR.mkdir(exist_ok=True)


def gerar_grafico_tipos(df):

    contagem = df["tipo"].value_counts()

    plt.figure(figsize=(6, 4))

    contagem.plot(kind="bar")

    plt.title("Quantidade por tipo de feriado")

    plt.xlabel("Tipo")

    plt.ylabel("Quantidade")

    plt.tight_layout()

    plt.savefig(GRAFICOS_DIR / "tipos_feriados.png")

    plt.close()