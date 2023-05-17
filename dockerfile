FROM python:3.9

WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho do contêiner
COPY requirements.txt .

# Instalando as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiando os arquivos do projeto para o diretório de trabalho do contêiner
COPY . .

# Comando para iniciar a aplicação
CMD ["python", "server.py"]
