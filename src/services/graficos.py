import matplotlib.pyplot as plt

from config import GRAFICOS_DIR


def gerar_graficos(df):

    GRAFICOS_DIR.mkdir(exist_ok=True)

    # -------------------------------
    # Preço médio por categoria
    # -------------------------------

    media_categoria = (
        df.groupby("categoria")["preco"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(8, 5))

    media_categoria.plot(kind="bar")

    plt.title("Preço médio por categoria")

    plt.tight_layout()

    plt.savefig(
        GRAFICOS_DIR / "preco_por_categoria.png"
    )

    plt.close()

    # -------------------------------
    # Quantidade por categoria
    # -------------------------------

    quantidade_categoria = (
        df["categoria"]
        .value_counts()
    )

    plt.figure(figsize=(8, 5))

    quantidade_categoria.plot(kind="pie", autopct="%1.1f%%")

    plt.ylabel("")

    plt.title("Distribuição das categorias")

    plt.tight_layout()

    plt.savefig(
        GRAFICOS_DIR / "categorias.png"
    )

    plt.close()

    # -------------------------------
    # Top 10 preços
    # -------------------------------

    top10 = (
        df.sort_values(
            by="preco",
            ascending=False
        )
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    plt.barh(
        top10["produto"],
        top10["preco"]
    )

    plt.title("Top 10 maiores preços")

    plt.tight_layout()

    plt.savefig(
        GRAFICOS_DIR / "top10_precos.png"
    )

    plt.close()