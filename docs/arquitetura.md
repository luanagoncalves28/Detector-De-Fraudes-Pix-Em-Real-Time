# Arquitetura Geral do Sistema de Detecção de Fraudes Pix

## Visão Geral

A arquitetura do sistema de detecção de fraudes em transações Pix foi projetada com foco em escalabilidade, resiliência e baixo acoplamento, visando atender aos rigorosos requisitos de performance e confiabilidade impostos pelo alto volume de transações e pela criticidade do domínio de fraude.

A solução adota uma abordagem de arquitetura orientada a serviços e baseada em eventos, onde os componentes são organizados em camadas com responsabilidades bem definidas e se comunicam através de tópicos de um barramento de eventos central. Essa arquitetura desacoplada permite que cada serviço evolua independentemente e que o sistema como um todo seja facilmente escalado horizontalmente.

## Diagrama de Arquitetura de Alto Nível

![Diagrama de Arquitetura de Alto Nível](![image](https://github.com/user-attachments/assets/1553cd81-3c1d-4f53-8e05-fc0dc5b0e1bb)
)

O diagrama acima apresenta uma visão de alto nível dos principais componentes da arquitetura e seus fluxos de comunicação:

- **Camada de Ingestão de Dados**: Responsável por consumir dados de transações Pix de múltiplas fontes (como APIs de instituições financeiras e arquivos batch), aplicar validações básicas e publicar as transações brutas em tópicos Kafka para processamento posterior.

- **Camada de Processamento de Stream**: Consome as transações dos tópicos Kafka, enriquece os dados com informações de bases auxiliares (como dados cadastrais de clientes), aplica as regras de detecção de fraude em tempo real usando modelos de machine learning servidos como microsserviços, e publica as transações enriquecidas e classificadas em novos tópicos.

- **Camada de Armazenamento de Dados**: Persiste os dados processados no Google Cloud Storage seguindo a arquitetura medallion (Bronze, Silver, Gold) com o Delta Lake para posterior análise exploratória, treinamento de modelos e servição de consultas.

- **Camada de Serviços**: Expõe APIs REST para consulta dos resultados da análise de fraude em tempo real e para integração com sistemas consumidores, como aplicações de monitoramento e sistemas de tomada de ação (bloqueio de transações suspeitas, envio de alertas, etc.).

- **Camada de Machine Learning**: Orquestra o treinamento contínuo dos modelos de detecção de fraude a partir dos dados históricos armazenados no Google Cloud Storage com o Delta Lake, servindo os modelos treinados como endpoints gRPC para inferência em tempo real na camada de processamento de stream.

## Fluxos de Dados e Pipelines Principais

O principal fluxo de dados no sistema segue o seguinte caminho:

1. Transações Pix brutas são ingeridas de múltiplas fontes pela **Camada de Ingestão de Dados** e publicadas em tópicos Kafka raw.

2. A **Camada de Processamento de Stream** consome as transações dos tópicos raw, enriquece com dados adicionais, aplica as regras de detecção de fraude invocando os modelos da **Camada de Machine Learning**, e publica as transações processadas em tópicos Kafka enriquecidos.

3. A **Camada de Armazenamento de Dados** consome as transações enriquecidas e as persiste no Google Cloud Storage usando o Delta Lake, particionando os dados de acordo com o estágio de processamento (Bronze: dados brutos, Silver: dados limpos e conformados, Gold: dados agregados e sumarizados prontos para consumo).

4. A **Camada de Serviços** consulta os dados processados no Google Cloud Storage com o Delta Lake para servir chamadas síncronas de sistemas consumidores através de APIs REST.

5. A **Camada de Machine Learning** periodicamente treina novos modelos a partir dos dados históricos no Google Cloud Storage com o Delta Lake e publica as versões atualizadas dos modelos para inferência em tempo real.

Esse é o principal fluxo de dados, mas há vários outros pipelines auxiliares, como fluxos para ingestão batch, pipelines de transformação e agregação de dados no Google Cloud Storage com o Delta Lake (ETL/ELT), exportação de datasets para treinamento dos modelos, monitoramento, etc.

## Decisões Arquiteturais para Requisitos Não-Funcionais 

### Escalabilidade e Alta Performance

- Uso de uma arquitetura orientada a eventos e baseada em serviços, permitindo o processamento assíncrono e a escalabilidade independente de cada componente.
- Adoção do Apache Kafka como plataforma central de streaming, garantindo alta vazão e baixa latência no processamento de eventos.
- Utilização do Apache Spark como motor de processamento distribuído, permitindo a análise em tempo real de grandes volumes de dados.
- Servição dos modelos de machine learning como microsserviços independentes, que podem ser dinamicamente escalados conforme a demanda.
- Uso do Google Cloud Storage com o Delta Lake para armazenamento escalável e de alta performance dos dados em suas diferentes camadas de processamento.

### Resiliência e Tolerância a Falhas

- Implantação dos serviços em Kubernetes, tirando proveito de recursos como replicação e auto-healing para garantir a disponibilidade.
- Adoção de padrões como Circuit Breaker e Retry para evitar falhas em cascata e lidar com instabilidades temporárias.
- Utilização do Kafka para desacoplamento entre produtores e consumidores, evitando perda de mensagens em caso de indisponibilidade de serviços.
- Implementação de pipelines de dados idempotentes e tolerantes a falhas, garantindo a consistência dos dados mesmo em caso de reprocessamento.
- Armazenamento resiliente e com replicação geográfica no Google Cloud Storage. 

### Manutenibilidade e Evolucionariedade

- Forte coesão e baixo acoplamento entre os componentes da arquitetura, facilitando a evolução independente de cada parte.
- Uso extensivo de Infrastructure as Code e GitOps para gerenciar a configuração e implantação da infraestrutura de forma rastreável e reproduzível.  
- Adoção de estratégias de deployment como Canary Release e Blue-Green para permitir a entrega incremental de novas versões dos serviços com segurança.
- Monitoramento abrangente de logs, métricas e traces distribuídos para rapidamente detectar e depurar problemas em produção.
- Versionamento e controle do ciclo de vida dos modelos de ML com MLflow, facilitando a evolução e a governança.

## Conclusão

A arquitetura proposta foi concebida para atender aos desafios únicos de um sistema de detecção de fraudes em tempo real para transações Pix, considerando os altos volumes de dados, os requisitos estritos de latência e as constantes evoluções dos padrões de fraude. 

Ao adotar uma arquitetura orientada a eventos e microsserviços, em conjunto com tecnologias estado-da-arte para processamento de streams, armazenamento de dados com o Google Cloud Storage e o Delta Lake, e machine learning, o sistema será capaz de escalar eficientemente, se adaptar rapidamente a mudanças e fornecer insights acionáveis com baixíssima latência, contribuindo assim para um ecossistema Pix mais seguro e confiável para todos os envolvidos.
