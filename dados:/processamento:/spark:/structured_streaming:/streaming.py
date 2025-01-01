from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Definir o esquema para os dados de transação JSON
transaction_schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("user_id", StringType()), 
    StructField("amount", DoubleType()),
    StructField("timestamp", StringType())
])

def start_streaming(spark, config):
    """
    Inicia o processamento de streaming de dados de transação usando Spark Structured Streaming.
    
    Args:
        spark (SparkSession): A sessão Spark.
        config (dict): As configurações para o processamento de streaming.
    """
    # Ler os dados de transação do Kafka
    transactions_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", config["kafka"]["bootstrap_servers"]) \
        .option("subscribe", config["kafka"]["topic"]) \
        .option("startingOffsets", config["kafka"]["starting_offsets"]) \
        .load()
    
    # Analisar os dados JSON
    parsed_df = transactions_df.select(
        from_json(col("value").cast("string"), transaction_schema).alias("transaction"), 
        col("timestamp").alias("processing_time")
    )
    
    # Selecionar as colunas necessárias e converter os tipos
    transformed_df = parsed_df.select(
        col("transaction.transaction_id").alias("transaction_id"),
        col("transaction.user_id").alias("user_id"),
        col("transaction.amount").alias("amount"),
        to_timestamp(col("transaction.timestamp"), "yyyy-MM-dd HH:mm:ss").alias("transaction_time"),
        col("processing_time")
    )
    
    # Definir a janela deslizante e calcular a soma dos valores
    windowed_df = transformed_df \
        .withWatermark("transaction_time", config["processing"]["watermark"]) \
        .groupBy(
            window(col("transaction_time"), config["processing"]["window_duration"]),
            col("user_id")
        ) \
        .sum("amount") \
        .alias("total_amount")
        
    # Configurar o sink de saída para o Kafka
    kafka_output = windowed_df \
        .selectExpr("to_json(struct(*)) AS value") \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", config["kafka"]["bootstrap_servers"]) \
        .option("topic", config["kafka"]["output_topic"]) \
        
    # Configurar o mode de saída e iniciar a query de streaming
    query = kafka_output \
        .outputMode(config["processing"]["output_mode"]) \
        .option("checkpointLocation", config["processing"]["checkpoint_location"]) \
        .trigger(processingTime=config["processing"]["trigger_interval"]) \
        .start()
        
    # Imprimir o progresso da query
    query.awaitTermination()
    
if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("FraudDetectionStreaming") \
        .getOrCreate()
        
    with open("streaming_config.yaml", "r") as file:
        config = yaml.safe_load(file)
        
    start_streaming(spark, config)
