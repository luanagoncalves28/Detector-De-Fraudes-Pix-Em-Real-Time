from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Definir esquema para dados JSON
transaction_schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("user_id", IntegerType()),
    StructField("amount", DoubleType()),
    StructField("timestamp", StringType())
])

def spark_ingestion(spark, config):
    """
    Ingere dados de um tópico Kafka usando Spark Structured Streaming.

    Args:
        spark (SparkSession): A sessão Spark.
        config (dict): As configurações para a ingestão Spark.

    Returns:
        None
    """
    # Ler dados do Kafka
    kafka_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", config['bootstrap_servers']) \
        .option("subscribe", config['topic']) \
        .option("startingOffsets", config['starting_offsets']) \
        .load()

    # Converter valor da mensagem de binário para string
    kafka_df_string = kafka_df.selectExpr("CAST(value AS STRING)")

    # Analisar dados JSON
    parsed_df = kafka_df_string.select(from_json(col("value"), transaction_schema).alias("data")).select("data.*")

    # Processar dados aqui (por exemplo, agregações, transformações, etc.)

    # Gravar dados no console para fins de depuração
    query = parsed_df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("FraudDetectionIngestion") \
        .getOrCreate()

    # Carregar configurações de spark_config.yaml
    with open('spark_config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    spark_ingestion(spark, config)
