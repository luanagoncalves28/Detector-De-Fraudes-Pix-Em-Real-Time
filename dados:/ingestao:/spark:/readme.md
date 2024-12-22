# Ingestão de Dados com Apache Spark

## Visão Geral
Este diretório contém o código e as configurações para o componente de ingestão de dados do Apache Spark para o pipeline de detecção de fraudes Pix em tempo real. O Spark complementa minha arquitetura de ingestão em tempo real baseada no Kafka, proporcionando uma maneira eficiente de ingerir e processar grandes lotes de dados. 

## Por que Spark para Ingestão de Dados?
Embora o Apache Kafka seja minha principal plataforma de ingestão de streaming, também utilizo o Apache Spark por alguns motivos chave:

1. **Processamento de Lotes**: O Spark é excepcionalmente bom em processar grandes lotes de dados muito rapidamente. Para fontes de dados que produzem dados em grandes lotes, ao invés de um fluxo contínuo, o modelo de micro-batch do Spark é mais eficiente.

2. **Integração com o Ecossistema Hadoop**: Muitos dos conjuntos de dados históricos residem no HDFS. O Spark pode ler diretamente do HDFS, tornando-o uma ótima escolha para ingerir esses conjuntos de dados.

3. **Ingestão Flexível**: Enquanto o Kafka requer que os dados sejam ingeridos como um fluxo, o Spark nos permite ingerir dados em lote ou em tempo real, tornando-o uma ferramenta versátil.

4. **Pré-processamento Eficiente**: O Spark permite algumas transformações e limpeza de dados durante a fase de ingestão, ajudando a otimizar os dados para análise posterior.

## Fluxo de Trabalho de Ingestão do Spark
O processo de ingestão do Spark geralmente segue estes passos:

1. **Leitura de Dados**: Uso os conectores de dados do Spark para ler dados de várias fontes, como HDFS, S3, bancos de dados etc. 

2. **Transformações Iniciais**: Realizo transformações iniciais nos dados brutos, como parsing de JSON, extração de campos de data, casting de tipos de dados, etc.

3. **Particionamento**: Particiono os dados com base em chaves significativas (por exemplo, timestamp) para otimizar consultas subsequentes.

4. **Escrita de Dados**: Escrevo os dados transformados e particionados em armazenamento de dados brutos (ou seja, a camada Bronze do Delta Lake).

## Organização do Código
- `spark_ingest.py`: Este é o script principal que orquestra o processo de ingestão do Spark. Ele lê as configurações, cria a SparkSession, define as transformações de dados e escreve para o armazenamento de destino.

- `spark_config.yaml`: Este arquivo contém todas as configurações para nosso trabalho de ingestão do Spark, incluindo detalhes da fonte de dados, transformações a serem aplicadas, esquema de particionamento, localização do destino, etc.

## Decisões de Design e Considerações
1. **Escolha de Formato de Dados**: Para armazenamento de dados brutos, optei pelo formato parquet devido à sua eficiência de armazenamento e desempenho de leitura, especialmente para consultas analíticas.

2. **Particionamento**: Implementei um esquema de particionamento baseado no timestamp das transações para otimizar consultas de séries temporais que são comuns em nosso pipeline de detecção de fraudes.

3. **Tratamento de Erros**: Para lidar com registros malformados ou corrompidos durante a ingestão, implementei um mecanismo de "dead letter queue", onde esses registros são segregados para análise e reprocessamento posteriores.

## Monitoramento e Registro
- Todas as execuções do trabalho de ingestão do Spark são registradas, com métricas sobre contagens de registros, tempos de execução, taxas de erro, etc. Esses logs são enviados ao nosso sistema de monitoramento central.

- As métricas de desempenho do Spark, como uso de memória e CPU do executor, são coletadas e visualizadas em dashboards do Grafana para monitoramento em tempo real do desempenho do trabalho.

## Para Recrutadores e Revisores de Código
Ao revisar este código, considere:

1. A abordagem de ingestão de dados em duas vertentes (Kafka + Spark) aproveita os pontos fortes de cada ferramenta e proporciona uma arquitetura de ingestão robusta?

2. As decisões de design, como escolha do formato de dados e esquema de particionamento, são apropriadas e bem fundamentadas?

3. O código segue as melhores práticas do Spark, como o uso eficiente de transformações lazy e cache quando apropriado?

4. Existem mecanismos adequados para tratamento de erros, registro e monitoramento?

Estou entusiasmada para discutir esses e outros aspectos do projeto! Sinta-se à vontade para mergulhar nos detalhes técnicos - estou sempre feliz em falar sobre as compensações e possíveis melhorias.

## Contato
- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
