# Reduzindo superfice de ataque
FROM python:3.10.8-slim

#Atualizações e limpeza de cache
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        lib-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#Utilização de usuarios nao previlegiados
RUN groupadd -r groupuser && useradd -r -g groupuser myuser
USER myuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]