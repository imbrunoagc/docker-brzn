
1. Subir os serviços em container

```bash
> docker compose up -d
```

2. Copiar o script para o container **spark-master**
```bash
> docker cp -L pyspark_job.py 7_processamento_dados_spark-spark-master-1:/opt/bitnami/spark/pyspark_job.py
```

3. Executar o script no **spark-master**

```bash
> docker exec 7_processamento_dados_spark-spark-master-1 spark-submit --master spark://3401f9d6899d:7077 pyspark_job.py
```