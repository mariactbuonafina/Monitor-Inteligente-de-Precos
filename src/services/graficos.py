import matplotlib.pyplot as plt

from config import GRAFICOS_DIR


def gerar_graficos(df):

    GRAFICOS_DIR.mkdir(exist_ok=True)

    plt.style.use("ggplot")

    media_categoria = (
        df.groupby("categoria")["preco"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(9, 5))

    media_categoria.plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title(
        "Preço médio por categoria",
        fontsize=16,
        weight="bold"
    )

    plt.xlabel("Categoria")
    plt.ylabel("Preço (R$)")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(
        GRAFICOS_DIR / "preco_por_categoria.png",
        dpi=200
    )

    plt.close()

    quantidade_categoria = (
        df["categoria"]
        .value_counts()
    )

    plt.figure(figsize=(7, 7))

    quantidade_categoria.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.ylabel("")

    plt.title(
        "Distribuição das categorias",
        fontsize=16,
        weight="bold"
    )

    plt.tight_layout()

    plt.savefig(
        GRAFICOS_DIR / "categorias.png",
        dpi=200
    )

    plt.close()

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

    plt.title(
        "Top 10 maiores preços",
        fontsize=16,
        weight="bold"
    )

    plt.xlabel("Preço (R$)")

    plt.tight_layout()

    plt.savefig(
        GRAFICOS_DIR / "top10_precos.png",
        dpi=200
    )

    plt.close()