import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
import yaml

# Carregar configurações do arquivo yaml
with open('kafka_config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Configurar consumidor Kafka
consumer = KafkaConsumer(
    config['kafka']['topic'],
    bootstrap_servers=config['kafka']['bootstrap_servers'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Configurar produtor Kafka
producer = KafkaProducer(
    bootstrap_servers=config['kafka']['bootstrap_servers'],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

# Consumir mensagens do tópico de entrada
for message in consumer:
    # Processar a mensagem (aqui você pode adicionar sua lógica de processamento)
    processed_message = message.value
    
    # Enviar a mensagem processada para o tópico de saída
    producer.send(config['kafka']['output_topic'], processed_message)

# Fechar o consumidor e o produtor
consumer.close()
producer.close()
