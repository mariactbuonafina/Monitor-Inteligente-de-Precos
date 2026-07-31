from pathlib import Path

from config import RELATORIOS_DIR


def gerar_dashboard(df):

    RELATORIOS_DIR.mkdir(exist_ok=True)

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

<title>Monitor de Produtos</title>

<style>

body{{
    font-family:Arial,sans-serif;
    margin:40px;
    background:#f4f4f4;
}}

h1{{
    color:#222;
}}

.tabela{{
    width:100%;
    border-collapse:collapse;
    background:white;
}}

.tabela th,
.tabela td{{
    border:1px solid #ddd;
    padding:10px;
    text-align:left;
}}

.tabela th{{
    background:#1976D2;
    color:white;
}}

</style>

</head>

<body>

<h1>Dashboard de Produtos</h1>

<p>Total de produtos: {len(df)}</p>

{tabela}

</body>

</html>
"""

    with open(
        RELATORIOS_DIR / "dashboard.html",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(html)