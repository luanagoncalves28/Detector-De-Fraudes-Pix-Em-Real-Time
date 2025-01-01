# Notebook Databricks para Treinamento de Modelos de Detecção de Fraudes Pix

# Importar bibliotecas necessárias
import pyspark
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Criar Sessão Spark 
spark = SparkSession.builder \
    .appName("Training Fraud Detection Models") \
    .getOrCreate()

# Ler dados de treinamento do Delta Lake
train_data = spark.read \
    .format("delta") \
    .load("/delta/pix_transactions_silver")

# Dividir em conjuntos de treinamento e validação 
(train, validation) = train_data.randomSplit([0.8, 0.2], seed=42)

# Definir features e target
features = ["transaction_amount", "transaction_time", "payer_id", "payee_id", ...]  
target = "is_fraud"

# Criar pipeline de transformação de feature 
assembler = VectorAssembler(inputCols=features, outputCol="features")

# Indexar coluna target
indexer = StringIndexer(inputCol=target, outputCol="label")

# Definir modelo Random Forest
rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=100)

# Montar pipeline
pipeline = Pipeline(stages=[assembler, indexer, rf])

# Treinar modelo
model = pipeline.fit(train)

# Fazer predições no conjunto de validação
predictions = model.transform(validation)

# Avaliar performance do modelo
evaluator = BinaryClassificationEvaluator(labelCol="label", rawPredictionCol="prediction", metricName="areaUnderROC")
auc = evaluator.evaluate(predictions)
print(f"Area Under ROC: {auc:.4f}")

# Registrar modelo no MLflow Model Registry
from mlflow.tracking import MlflowClient

client = MlflowClient()
run = client.create_run(experiment_id="1")
client.log_artifact(run.info.run_id, "model")
model_version = mlflow.register_model(f"runs:/{run.info.run_id}/model", "FraudDetectionModel")

# Transicionar modelo para stage "Staging"
client.transition_model_version_stage(model_version, stage="Staging")

# Exibir métricas e parâmetros do modelo registrado
print(f"Model Name: {model_version.name}")
print(f"Model Version: {model_version.version}")
print(f"AUC: {auc:.4f}")

# Salvar notebook no DBFS
dbutils.notebook.exit("success")
