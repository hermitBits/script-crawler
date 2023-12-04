# Use uma imagem base do Python
FROM python:3.8

# Define o diretório de trabalho na imagem
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instale o SQLite
RUN apt-get update && apt-get install -y sqlite3

# Copia o restante do código-fonte para o diretório de trabalho
COPY . .
