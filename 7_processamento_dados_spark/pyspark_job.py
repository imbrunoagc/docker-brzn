from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = (
    SparkSession
        .builder
        .appName("Pyspark Job Estudo Apoena")
        .getOrCreate()
)

rdd = spark.sparkContext.parallelize(range(1, 100))

even_rdd = rdd.filter(lambda x: x % 2 == 0)

even_count = even_rdd.count()
even_sum = even_rdd.sum()
average = even_rdd.mean()

print("Pyspark Job Calculations")
print("Results:")
print("Quantidade de Números Pares:", even_count)
print("Soma dos Números Pares:", even_sum)
print("Média de Números Pares:", average)

spark.stop()