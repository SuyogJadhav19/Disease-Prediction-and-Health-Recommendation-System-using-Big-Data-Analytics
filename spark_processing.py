from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DiseasePrediction") \
    .getOrCreate()

df = spark.read.csv("dataset.csv", header=True, inferSchema=True)

print("Dataset Loaded Successfully")
df.show(5)

pandas_df = df.toPandas()

print(pandas_df.head())
