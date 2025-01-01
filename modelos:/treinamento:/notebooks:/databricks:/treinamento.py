```python
# Importar bibliotecas necessárias
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
import mlflow

# Carregar configurações
with open('treinamento_config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
# Configurar sessão Spark
spark = SparkSession.builder \
    .appName("FraudDetectionTraining") \
    .getOrCreate()

# Carregar dados de treino
train_data = spark.read \
    .format("delta") \
    .load(config['data']['train_path'])
    
# Carregar dados de teste  
test_data = spark.read \
    .format("delta") \
    .load(config['data']['test_path'])

# Definir features e label
features = config['model']['features']
label = config['model']['label']

# Criar pipeline de pré-processamento
assembler = VectorAssembler(inputCols=features, outputCol="features")
scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")
preprocessor = Pipeline(stages=[assembler, scaler])

# Treinar modelo de floresta aleatória
rf = RandomForestClassifier(labelCol=label, featuresCol="scaledFeatures", numTrees=100)
pipeline = Pipeline(stages=[preprocessor, rf])
model = pipeline.fit(train_data)

# Avaliar o modelo
predictions = model.transform(test_data)
evaluator = BinaryClassificationEvaluator(labelCol=label)
auc = evaluator.evaluate(predictions)
print(f'Test AUC: {auc:.3f}')

# Registrar modelo e métricas no MLflow
with mlflow.start_run(run_name=config['experiment']['name']):
    mlflow.log_param("num_trees", 100)
    mlflow.log_metric("test_auc", auc)  
    mlflow.spark.log_model(model, "model")
    mlflow.set_tags(config['experiment']['tags'])
```
