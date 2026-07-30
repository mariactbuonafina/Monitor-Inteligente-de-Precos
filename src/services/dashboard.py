from pathlib import Path

from config import RELATORIOS_DIR

from services.analise import (
    top_mais_caros,
    top_mais_baratos
)


def gerar_dashboard(df):

    template = Path("templates/dashboard.html")

    html = template.read_text(
        encoding="utf-8"
    )

    conteudo = f"""

<h1>📊 Monitor Inteligente de Produtos</h1>

<div class="kpis">

<div class="kpi">

<h2>{len(df)}</h2>

Produtos

</div>

<div class="kpi">

<h2>{df["categoria"].nunique()}</h2>

Categorias

</div>

<div class="kpi">

<h2>R$ {df["preco"].mean():.2f}</h2>

Preço Médio

</div>

<div class="kpi">

<h2>R$ {df["preco"].max():.2f}</h2>

Maior Preço

</div>

</div>

<div class="card">

<h2>Produtos mais caros</h2>

{top_mais_caros(df).to_html(index=False)}

</div>

<div class="card">

<h2>Produtos mais baratos</h2>

{top_mais_baratos(df).to_html(index=False)}

</div>

<div class="card">

<h2>Preço médio por categoria</h2>

<img src="../graficos/preco_por_categoria.png">

</div>

<div class="card">

<h2>Distribuição das categorias</h2>

<img src="../graficos/categorias.png">

</div>

<div class="card">

<h2>Top 10 maiores preços</h2>

<img src="../graficos/top10_precos.png">

</div>

"""

    html = html.replace(
        "{{conteudo}}",
        conteudo
    )

    RELATORIOS_DIR.mkdir(exist_ok=True)

    with open(
        RELATORIOS_DIR / "dashboard.html",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(html)