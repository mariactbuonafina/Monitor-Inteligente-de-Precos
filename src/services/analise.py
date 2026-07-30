from config import RELATORIOS_DIR


def top_mais_caros(df, quantidade=5):

    return (
        df.sort_values(
            by="preco",
            ascending=False
        )
        .head(quantidade)
    )


def top_mais_baratos(df, quantidade=5):

    return (
        df.sort_values(
            by="preco",
            ascending=True
        )
        .head(quantidade)
    )


def gerar_relatorio(df):

    RELATORIOS_DIR.mkdir(exist_ok=True)

    arquivo = RELATORIOS_DIR / "resumo.md"

    mais_caros = top_mais_caros(df)
    mais_baratos = top_mais_baratos(df)

    with open(arquivo, "w", encoding="utf-8") as md:

        md.write("# 📊 Relatório da Coleta\n\n")

        md.write("## Indicadores Gerais\n\n")

        md.write(f"- **Produtos encontrados:** {len(df)}\n")
        md.write(f"- **Categorias:** {df['categoria'].nunique()}\n")
        md.write(f"- **Marcas:** {df['marca'].nunique()}\n")
        md.write(f"- **Preço médio:** R$ {df['preco'].mean():.2f}\n")
        md.write(f"- **Menor preço:** R$ {df['preco'].min():.2f}\n")
        md.write(f"- **Maior preço:** R$ {df['preco'].max():.2f}\n")
        md.write(f"- **Maior avaliação:** {df['avaliacao'].max()}\n")
        md.write(f"- **Data da coleta:** {df['data_coleta'].max()}\n")

        md.write("\n---\n\n")

        md.write("## 💰 Top 5 produtos mais caros\n\n")

        md.write(
            mais_caros[
                ["produto", "preco"]
            ].to_markdown(index=False)
        )

        md.write("\n\n---\n\n")

        md.write("## 🛒 Top 5 produtos mais baratos\n\n")

        md.write(
            mais_baratos[
                ["produto", "preco"]
            ].to_markdown(index=False)
        )