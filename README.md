# Pipeline de Dados de Tratores de Esteiras
Este repositório armazena o conteúdo dos resultados mostrados na dissertação de Mestrado em Engenharia de Software sobre padrões de desgaste de materiais rodantes de tratores de esteiras.

## 📑 Sumário
- 🧑‍💻 [**Quero rodar este projeto localmente**](#🧑‍💻-Rodar-localmente)
- 📊 [**Quero apenas visualizar os dados**](#📊-Visualizar-os-dados)

## 📁 Estrutura do projeto
```plaintext
data-pipeline-crawler-dozers/
├── data/
│   ├── raw/
│   ├── processed/
├── notebooks/
│   ├── 01_extract.ipynb
│   ├── 02_transform.ipynb
│   ├── 03_load.ipynb
│   └── 04_analyze.ipynb
├── scripts/
│   └── pipeline.py
├── .gitignore
├── docker-compose.yml
├── README.md
├── requirements.txt
```

## 🧑‍💻 Rodar localmente
### 🛠️ Requisitos
- 🐍 Python 3.11
- 🐳 Docker 25.0.3+

### ⚙️ Configurando ambiente (Windows)

- Clonando o projeto
```bash
git clone <Colar link aqui> && cd data-pipeline-crawler-dozers
```
- Criando ambiente virtual
```bash
python -m venv venv
```
- Acessando o ambiente virtual
```bash
venv\scripts\activate
```

- Instalando dependências
```bash
pip install -r requirements.txt
```

### 💻 Iniciando Container do MinIO (Armazenamento de Objetos)

```bash
docker-compose up -d
```

### 🔁 Executando pipeline

```bash
python pipeline.py
```

## 📊 Visualizar os dados

Abra o arquivo [`04_analyze.ipynb`](notebooks/04_analyze.ipynb) dentro da pasta `notebooks`.
