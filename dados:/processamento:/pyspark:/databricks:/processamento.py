from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp, window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Definir o esquema para os dados de transação JSON
transaction_schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("user_id", IntegerType()),
    StructField("amount", DoubleType()),
    StructField("timestamp", StringType())
])

def process_transactions(spark, kafka_source, kafka_target, db_target):
    """
    Processa os dados de transação do Kafka, agrega eles em uma janela de tempo,
    e escreve os resultados de volta para o Kafka e para um banco de dados.

    Args:
        spark (SparkSession): A sessão Spark.
        kafka_source (str): A string de conexão de origem do Kafka.
        kafka_target (str): A string de conexão de destino do Kafka.
        db_target (str): A string de conexão do banco de dados de destino.
    """
    # Ler os dados de transação do Kafka
    transactions_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_source) \
        .option("subscribe", "transactions") \
        .load()

    # Analisar os dados JSON
    transactions_df = transactions_df \
        .select(from_json(col("value").cast("string"), transaction_schema).alias("data")) \
        .select("data.*")

    # Converter o timestamp para um tipo de timestamp
    transactions_df = transactions_df \
        .withColumn("timestamp", to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss"))

    # Agregar as transações por usuário em uma janela de tempo de 5 minutos
    agg_df = transactions_df \
        .groupBy(
            window(col("timestamp"), "5 minutes"),
            col("user_id")
        ) \
        .agg({"amount": "sum"}) \
        .selectExpr("window", "user_id", "sum(amount) as total_amount")

    # Escrever os resultados agregados de volta para o Kafka
    agg_df \
        .selectExpr("to_json(struct(*)) AS value") \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_target) \
        .option("topic", "transactions_aggregated") \
        .option("checkpointLocation", "/path/to/checkpoint") \
        .start()

    # Escrever os resultados agregados para um banco de dados
    agg_df \
        .writeStream \
        .format("jdbc") \
        .option("url", db_target) \
        .option("dbtable", "transactions_aggregated") \
        .option("checkpointLocation", "/path/to/checkpoint") \
        .start()

    # Aguardar a terminação das consultas de streaming
    spark.streams.awaitAnyTermination()

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("TransactionProcessing") \
        .getOrCreate()

    # Carregar configurações de processamento_config.yaml
    with open('processamento_config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    process_transactions(
        spark,
        config['kafka']['source'],
        config['kafka']['target'],
        config['db']['target']
    )
