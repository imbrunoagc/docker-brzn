FROM python:3.9-slim

WORKDIR /app

COPY app /app/app
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
RUN mkdir -p /data

CMD ["python", "app/main.py"]