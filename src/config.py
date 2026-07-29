from pathlib import Path

# path das pastas
DADOS_DIR = Path("dados")
LOGS_DIR = Path("logs")
GRAFICOS_DIR = Path("graficos")
RELATORIOS_DIR = Path("relatorios")

# ref dos arquivos path
PRODUTOS_JSON = DADOS_DIR / "produtos.json"
PRECOS_CSV = DADOS_DIR / "precos.csv"
HISTORICO_CSV = DADOS_DIR / "historico.csv"

# urls das APIs
BASE_URL = "https://dummyjson.com/products/search"