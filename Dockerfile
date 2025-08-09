# Imagem base Python 3.13 com Alpine 3.22 (leve e rápida)
FROM python:3.13-alpine3.22

# Define diretório de trabalho dentro do container
WORKDIR /app

# Evita criação de arquivos .pyc e buffer de stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copia o arquivo de requisitos e instala dependências Python
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto para o container
COPY . .

# Porta que a aplicação Flask vai usar
EXPOSE 5000

# Comando para rodar a aplicação (ajuste para seu arquivo principal)
CMD ["python", "app.py"]
