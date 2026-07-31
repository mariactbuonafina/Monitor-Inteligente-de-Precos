from pathlib import Path

# solucao p encontrar o caminho do projeto, mesmo que seja exec em outro diretório
BASE_DIR = Path(__file__).resolve().parent.parent

DADOS_DIR = BASE_DIR / "dados"
RELATORIOS_DIR = BASE_DIR / "relatorios"
GRAFICOS_DIR = BASE_DIR / "graficos"
LOGS_DIR = BASE_DIR / "logs"

PRODUTOS_JSON = DADOS_DIR / "produtos.json"
PRECOS_CSV = DADOS_DIR / "precos.csv"
HISTORICO_CSV = DADOS_DIR / "historico.csv"

BASE_URL = "https://dummyjson.com/products/search"