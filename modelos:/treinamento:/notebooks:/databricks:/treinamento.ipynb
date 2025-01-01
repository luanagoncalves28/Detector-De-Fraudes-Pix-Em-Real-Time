# Importar bibliotecas necessárias
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
import mlflow
import yaml

# Carregar configurações do arquivo YAML
with open('treinamento_config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
# Configurar sessão Spark    
spark = SparkSession.builder \
    .appName("FraudDetectionTraining") \
    .getOrCreate()

# Carregar dados de treinamento e teste do Delta Lake
train_data = spark.read.format("delta").load(config['data']['train_path'])
test_data = spark.read.format("delta").load(config['data']['test_path'])

# Definir features e label
features = config['model']['features']
label = config['model']['label']

# Criar pipeline de pré-processamento
# VectorAssembler combina múltiplas colunas em um vetor de features
# StandardScaler padroniza as features para ter média 0 e variância 1
assembler = VectorAssembler(inputCols=features, outputCol="features")
scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")
preprocessor = Pipeline(stages=[assembler, scaler])

# Treinar modelo RandomForestClassifier
# numTrees é o número de árvores na floresta (um hiperparâmetro)
rf = RandomForestClassifier(labelCol=label, featuresCol="scaledFeatures", numTrees=100) 
pipeline = Pipeline(stages=[preprocessor, rf])
model = pipeline.fit(train_data)

# Avaliar o modelo nos dados de teste
predictions = model.transform(test_data)
evaluator = BinaryClassificationEvaluator(labelCol=label)
auc = evaluator.evaluate(predictions)
print(f"Test AUC: {auc:.3f}")

# Registrar o modelo e as métricas no MLflow
with mlflow.start_run(run_name=config['experiment']['name']):
    mlflow.log_param("num_trees", 100)
    mlflow.log_metric("test_auc", auc)  
    mlflow.spark.log_model(model, "model")
    mlflow.set_tags(config['experiment']['tags'])
