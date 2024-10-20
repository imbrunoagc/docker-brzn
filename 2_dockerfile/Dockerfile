# base da imagem
FROM python:3.10.8

# Definir qual será o diretório de trabalho da aplicação -> Container
WORKDIR /app

# Copiar o arquivo de configuração de dependências
# Requirements.txt
COPY requirements.txt requirements.txt

# copiando o arquivo da aplicação
COPY iss_tracker.py app.py

# instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Execução de entrada do container/app
CMD [ "python", "app.py" ]