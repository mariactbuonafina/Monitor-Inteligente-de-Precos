from pathlib import Path

from config import RELATORIOS_DIR


def gerar_dashboard(df):

    RELATORIOS_DIR.mkdir(exist_ok=True)

    menor = df["preco"].min()
    maior = df["preco"].max()
    media = round(df["preco"].mean(), 2)

    tabela = df.to_html(
        index=False,
        classes="tabela",
        border=0
    )

    html = f"""
<!DOCTYPE html>

<html lang="pt-BR">

<head>

<meta charset="UTF-8">

<title>Monitor Inteligente de Produtos</title>

<style>

body{{
font-family:Arial;
background:#F5F5F5;
margin:40px;
}}

h1{{
color:#1976D2;
}}

.cards{{
display:flex;
gap:20px;
margin:30px 0;
flex-wrap:wrap;
}}

.card{{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0 0 8px rgba(0,0,0,.15);
width:220px;
}}

.card h2{{
margin:0;
font-size:17px;
}}

.card p{{
font-size:28px;
font-weight:bold;
margin-top:15px;
}}

.tabela{{
width:100%;
border-collapse:collapse;
background:white;
}}

.tabela th{{
background:#1976D2;
color:white;
padding:10px;
}}

.tabela td{{
padding:8px;
border:1px solid #ddd;
}}

img{{
margin-top:40px;
width:90%;
max-width:900px;
}}

</style>

</head>

<body>

<h1>Monitor Inteligente de Produtos</h1>

<div class="cards">

<div class="card">

<h2>Produtos</h2>

<p>{len(df)}</p>

</div>

<div class="card">

<h2>Menor preço</h2>

<p>R$ {menor}</p>

</div>

<div class="card">

<h2>Maior preço</h2>

<p>R$ {maior}</p>

</div>

<div class="card">

<h2>Média</h2>

<p>R$ {media}</p>

</div>

</div>

<h2>Tabela de produtos</h2>

{tabela}

<h2>Gráfico</h2>

<img src="../graficos/precos.png">

</body>

</html>
"""

    with open(
        RELATORIOS_DIR / "dashboard.html",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(html)