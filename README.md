# 📊 Monitor Inteligente de Preços

Projeto desenvolvido em Python para monitoramento automático de preços de produtos utilizando APIs públicas, processamento de dados, análises estatísticas, geração de gráficos, dashboard HTML e automação com n8n.

---

# Objetivos

O projeto foi desenvolvido com foco em aprendizado e aplicação prática de Engenharia de Dados, Automação e Análise de Dados.

O pipeline realiza automaticamente:

- coleta de dados em API pública;
- tratamento e limpeza dos dados;
- armazenamento em CSV;
- manutenção de histórico;
- geração de indicadores;
- criação de gráficos;
- geração de dashboard HTML;
- disponibilização através de uma API FastAPI;
- automação utilizando n8n.

---

# Arquitetura

```
               n8n
                │
                ▼
          FastAPI (/executar)
                │
                ▼
        Consulta API pública
                │
                ▼
        Tratamento dos dados
                │
                ▼
        Atualização dos CSVs
                │
                ▼
        Análise estatística
                │
                ▼
         Geração de gráficos
                │
                ▼
       Dashboard HTML atualizado
```

---

# Estrutura do projeto

```
monitor-precos/

dados/
│
├── produtos.json
├── precos.csv
└── historico.csv

graficos/

logs/

relatorios/

src/

│
├── api/
├── core/
├── services/
├── templates/
├── utils/

main.py
requirements.txt
README.md
```

---

# Tecnologias

- Python
- Pandas
- Requests
- Matplotlib
- FastAPI
- Uvicorn
- n8n
- Docker
- HTML
- CSS
- JSON

---

# Fluxo ETL

## Extração

Consulta produtos em API pública.

## Transformação

Padronização dos dados.

Conversão de tipos.

Limpeza.

Normalização.

## Carga

Atualização dos arquivos

- precos.csv
- historico.csv

---

# Dashboard

O sistema gera automaticamente:

- resumo em Markdown;
- dashboard HTML;
- gráficos;
- histórico atualizado.

---

# API

Após iniciar o servidor:

```
uvicorn api.server:app --reload
```

Acesse:

```
http://127.0.0.1:8000/docs
```

ou

```
http://127.0.0.1:8000/executar
```

---

# Automação

O projeto utiliza o **n8n** para executar o pipeline automaticamente.

Fluxo:

```
Schedule Trigger

↓

HTTP Request

↓

FastAPI

↓

Pipeline

↓

Dashboard atualizado
```

---

# Como executar

## Clone

```bash
git clone <repositorio>
```

## Ambiente virtual

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

## Instalação

```bash
pip install -r requirements.txt
```

## Executar

```bash
python src/main.py
```

ou

```bash
uvicorn api.server:app --reload
```

---

# Aprendizados

Durante o desenvolvimento foram utilizados conceitos de:

- Engenharia de Dados
- ETL
- APIs REST
- Pandas
- Visualização de Dados
- Automação
- Docker
- FastAPI
- n8n
- Git
- GitHub

---

# Próximas melhorias

- SQLite
- PostgreSQL
- Docker Compose completo
- Deploy
- Dashboard interativo
- Filtros por categoria
- Histórico por produto
- Alertas automáticos de queda de preço

---

Desenvolvido para fins de estudo e evolução em Engenharia de Dados, Python e Automação.
