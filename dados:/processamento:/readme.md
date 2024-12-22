# Processamento de Dados - Detector de Fraudes Pix
## Visão Geral
Bem-vindo ao coração do meu pipeline de detecção de fraudes Pix em tempo real - o estágio de processamento de dados! É aqui que eu pego os dados brutos ingeridos pelo Kafka e Spark, e os transformo em informações acionáveis que podem ser usadas para identificar atividades fraudulentas.
Este diretório contém todo o código e configurações relacionadas ao processamento de dados. Eu utilizo duas ferramentas principais para este estágio:
1. **Apache Spark com PySpark**: Para processamento distribuído em larga escala de dados em batch. 
2. **Spark Structured Streaming**: Para processamento em tempo real de dados de streaming do Kafka.
## Importância do Processamento de Dados
O processamento de dados é um passo crucial em qualquer pipeline de detecção de fraudes porque é aqui que os padrões e anomalias começam a emergir dos dados brutos. Algumas das tarefas chave que eu realizo neste estágio incluem:
- **Limpeza de Dados**: Remover quaisquer dados incorretos, incompletos ou duplicados.
- **Transformação de Dados**: Converter os dados em um formato adequado para análise. Isso pode envolver parsing, agregação, junção de datasets, etc.
- **Enriquecimento de Dados**: Aumentar os dados com informações adicionais de fontes externas, como dados demográficos do cliente ou dados geográficos.
- **Engenharia de Features**: Criar novas features derivadas que podem ser úteis para os modelos de machine learning, como razões, taxas de mudança, ou medidas estatísticas.
O objetivo é transformar os dados brutos em um formato limpo, estruturado e rico em informações que possa ser efetivamente usado pelos meus modelos de detecção de fraude a jusante.
## Decisões Arquiteturais e Técnicas
### Apache Spark e PySpark
Eu escolhi usar o Apache Spark para processamento em batch devido à sua capacidade de lidar com grandes volumes de dados de forma eficiente. Especificamente:
- **Processamento Distribuído**: O Spark permite processar dados em múltiplos nós de um cluster, tornando-o altamente escalável.
- **Velocidade**: Com seu motor de execução em memória, o Spark pode ser 100x mais rápido que o MapReduce do Hadoop para processamento em batch.
- **API PySpark**: Eu uso PySpark, a API Python do Spark, que fornece uma interface simples e expressiva para manipulação de dados.
Dentro do diretório `pyspark/`, você encontrará meus scripts PySpark que leem dados das camadas Bronze/Silver do Delta Lake, realizam as transformações necessárias, e gravam os resultados de volta para as camadas Silver/Gold.
### Spark Structured Streaming
Para processamento em tempo real de dados de streaming do Kafka, eu utilizo o Spark Structured Streaming. Isso me permite tratar os dados de streaming como se fossem uma tabela estruturada infinita e aplicar operações complexas como junções, agregações e condições de janela.
O diretório `spark/structured_streaming/` contém meus jobs de streaming que leem dados dos tópicos Kafka, realizam o processamento em tempo real e gravam os resultados de volta ao Kafka ou ao Delta Lake para consumo posterior.
### Databricks
Para gerenciar e executar meus workloads Spark, eu uso a plataforma Databricks. O Databricks fornece um ambiente gerenciado para desenvolvimento e implantação de aplicativos Spark, com suporte integrado para notebooks, gerenciamento de cluster, monitoramento de jobs, e mais.
Minhas configurações e scripts Databricks podem ser encontrados no diretório `pyspark/databricks/`.
## Organização do Código
O código neste diretório está organizado da seguinte forma:
```
processamento/
├── pyspark/
│   ├── databricks/
│   │   ├── processamento.py
│   │   └── processamento_config.yaml
│   └── readme.md
└── spark/
    ├── structured_streaming/
    │   ├── streaming.py
    │   ├── streaming_config.yaml
    │   └── readme.md
    └── readme.md
```
- O diretório `pyspark/` contém todos os scripts e configurações relacionadas ao processamento PySpark em batch.
  - O subdiretório `databricks/` contém scripts e configurações específicos da plataforma Databricks.
- O diretório `spark/` contém código relacionado ao processamento Spark em geral.
  - O subdiretório `structured_streaming/` contém scripts e configurações para processamento Spark Structured Streaming.
Cada diretório tem seu próprio `readme.md` que fornece detalhes sobre seu conteúdo específico.
## Monitoramento e Confiabilidade
Para garantir que meu pipeline de processamento de dados esteja sempre operando de forma eficiente e confiável, implementei um extenso sistema de monitoramento e recuperação de falhas:
- **Métricas de Desempenho do Spark**: Eu acompanho métricas chave como tempo de processamento de tarefas, uso de memória e I/O de disco para cada job Spark. Anomalias disparam alertas para investigação.
- **Verificações de Qualidade de Dados**: Eu executo verificações de qualidade de dados nos dados processados para identificar quaisquer inconsistências introduzidas durante o processamento. Se descobertos, problemas de qualidade são registrados e disparados alertas.
- **Recuperação de Falhas**: Meus jobs Spark são projetados para serem resilientes a falhas. Se um job falhar devido a um erro transitório, ele será reiniciado automaticamente a partir do último checkpoint. Os dados processados até o ponto da falha não serão perdidos.
Esses sistemas garantem que quaisquer problemas no processamento de dados sejam detectados e resolvidos rapidamente, minimizando o impacto nas fases subsequentes do pipeline.
## Para Recrutadores e Revisores de Código
Como engenheira de machine learning trabalhando para construir um sistema de detecção de fraude de última geração, acredito que o processamento de dados é uma das peças mais críticas do quebra-cabeça. Se você está revisando esta parte do meu projeto, convido você a considerar:
1. **Escolha de Ferramentas**: O Spark é a ferramenta certa para os requisitos de processamento de dados deste projeto? Estou fazendo uso eficaz de suas capacidades de processamento em batch e streaming?
2. **Qualidade do Código**: Meu código PySpark e Structured Streaming é limpo, legível, e segue as melhores práticas?  Eu lidei com casos de borda e erros com graciosidade?
3. **Desempenho e Otimização**: Meus jobs Spark são eficientes no uso de recursos? Há oportunidades para melhorar o desempenho através de técnicas como particionamento, caching ou ajuste de configurações?
4. **Confiabilidade e Monitoramento**: Implementei verificações e equilíbrios suficientes para garantir a confiabilidade do processamento de dados? Os sistemas de monitoramento e alerta são abrangentes e eficazes?
Como a única engenheira neste projeto, tive que tomar muitas dessas decisões de arquitetura e design de forma independente. Eu ficaria muito feliz em aprofundar meu raciocínio e discutir possíveis melhorias.
## Próximos Passos
Procurando para o futuro, algumas áreas onde eu gostaria de melhorar ainda mais este componente incluem:
- **Processamento de Dados mais Avançado**: Experimentar técnicas mais avançadas de limpeza de dados, transformação e engenharia de features, possivelmente incorporando abordagens de aprendizado de máquina.
- **Otimização de Desempenho**: Realizar benchmarking e ajuste para otimizar ainda mais o desempenho dos meus jobs Spark, particularmente em torno de particionamento e uso de memória.
- **Automação End-to-End**: Integrar completamente o processamento de dados nos meus pipelines de CI/CD para implantações automatizadas e atualizações contínuas.
Espero que este overview tenha dado a você um bom insight sobre como estou abordando o processamento de dados para detecção de fraudes em tempo real no Pix. Se você tiver alguma dúvida ou feedback, eu adoraria ouvir de você! Sinta-se à vontade para me contatar:
- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
