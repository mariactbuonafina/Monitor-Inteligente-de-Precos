from pathlib import Path

# deixe aqui para organizar as pastas
DADOS_DIR = Path("dados")
LOGS_DIR = Path("logs")
RELATORIOS_DIR = Path("relatorios")
GRAFICOS_DIR = Path("graficos")

# referencie os arquivos e caminhos aqui
FERIADOS_CSV = DADOS_DIR / "feriados.csv"
HISTORICO_CSV = DADOS_DIR / "historico.csv"

# links das urls das APIs
BRASIL_API_FERIADOS = "https://brasilapi.com.br/api/feriados/v1/2026"