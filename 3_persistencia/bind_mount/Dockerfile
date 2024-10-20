# Definição da imagem python
FROM python:3.10

# Diretorio a ser trabalhado app
WORKDIR /app

# Criar a pasta dir/data na qual vai hospedar os dados persistidos
RUN mkdir -p /app/data

# copiar o requirements.txt para a pasta atual (APP) - [origem -> destino (. or /app/)]
COPY requirements.txt .

# Executar a instalação das dependencias existentes dentro de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copiar o app python principal para dentro da pasta atual (APP) - [origem -> destino (. or /app/)]
COPY ./iss_tracker.py .

# executar o script python
CMD [ "python", "iss_tracker.py" ]