arquivo.write("# Resumo da Coleta\n\n")

arquivo.write(f"- Total de registros: **{len(df)}**\n")

arquivo.write(
    f"- Última coleta: **{df['data_coleta'].max()}**\n"
)

arquivo.write(
    f"- Quantidade de tipos: **{df['tipo'].nunique()}**\n\n"
)

arquivo.write("## Colunas\n\n")

for coluna in df.columns:
    arquivo.write(f"- {coluna}\n")