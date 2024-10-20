# Definição da imagem python
FROM python:3.10

# Diretorio a ser trabalhado app
WORKDIR /app

# Criar a pasta dir/data na qual vai hospedar os dados persistidos
RUN mkdir -p /app/data

# copiar o app python principal para dentro da pasta atual (APP) - [origem -> destino (. or /app/)]
COPY ./app.py .

# executar o script python
CMD [ "python", "app.py" ]