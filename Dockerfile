# Use uma imagem base do Python
FROM python:3.8

# Define o diretório de trabalho na imagem
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y sqlite3  \
    wget \
    gnupg \
    curl \
    unzip \
    ca-certificates \
    fonts-liberation

# Adicione o repositório do Google Chrome
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && apt-get update

# Instale o Google Chrome
RUN apt-get install -y google-chrome-stable

# Copia o restante do código-fonte para o diretório de trabalho
COPY . .
