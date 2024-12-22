Ingestão de Dados com Apache Kafka
Visão Geral
Este diretório contém o código e as configurações para o componente de aquisição de dados baseado no Apache Kafka do pipeline de detecção de fraudes Pix. O Kafka atua como uma espinha dorsal para a captura em tempo real e o arquivo de dados de transações Pix, garantindo que nenhum dado seja perdido e que o processamento a jusante possa ocorrer de forma escalável e resiliente.
Por que Kafka?
O Apache Kafka é uma plataforma distribuída de streaming ideal para lidar com dados em tempo real, especialmente em alta escala. Suas principais características incluem:

Alto Throughput : O Kafka pode lidar com centenas de milhares de mensagens por segundo de várias fontes, tornando-o bem adequado para o grande volume de transações Pix.
Baixa Latência : As mensagens são enfileiradas em milissegundos, permitindo processamento quase em tempo real.
Escalabilidade Tolerante a Falhas : O Kafka pode escalar facilmente adicionando mais nós e é resiliente a falhas de nenhum indivíduo.
Durabilidade : As mensagens são persistentes no disco, proporcionando durabilidade e permitindo o consumo repetido.

Essas características tornam o Kafka uma escolha ideal para a fase de aquisição do nosso pipeline, onde a confiabilidade, a velocidade e a capacidade de lidar com cargas são primordiais.
Arquitetura do Sistema
Nossa implementação Kafka consiste nos seguintes componentes principais:

Tópicos : Teremos tópicos separados para diferentes categorias de eventos de transação Pix (por exemplo, pagamentos, coletas, estornos). Isso nos permite escalar e processar cada tipo de evento de forma independente.
Produtores : Temos produtores Kafka que capturam dados de transações de diversas fontes (APIs bancárias, logs do sistema, etc.) e os publicam nos detalhes detalhados. Os produtores são desenvolvidos em Python usando uma biblioteca kafka-python.
Consumidores : Os consumidores Kafka leem os eventos dos tópicos e os encaminham para as próximas etapas do pipeline (processamento em lote com Spark, armazenamento no Delta Lake, etc.). Também usamos uma biblioteca kafka-pythonpara nossos consumidores.

Aqui está uma visão geral de alto nível da arquitetura:
                                   ┌──────────────┐
                                   │              │
                           ┌──────▶│  Tópico Pix  │
                           │       │  Pagamentos  │
┌─────────────┐            │       │              │
│             │            │       └──────────────┘
│  Fontes de  │──┐         │
│  Dados Pix  │  │         │       ┌──────────────┐
│             │  │┌───────────────▶│              │
└─────────────┘  ││        │       │  Tópico Pix  │
                 ││  Kafka │       │ Recebimentos │
┌─────────────┐  │└───────────────▶│              │
│             │  │         │       └──────────────┘
│  Fontes de  │──┘         │
│  Dados Pix  │            │       ┌──────────────┐
│             │            │       │              │
└─────────────┘            └──────▶│  Tópico Pix  │
                                   │   Estornos   │
                                   │              │
                                   └──────────────┘

    Produtores                      Consumidores
Organização do Código
O código e as configurações neste diretório estão organizados da seguinte forma:

kafka_ingest.py: Este é o roteiro principal que inicializa os produtores e consumidores Kafka. Ele lê as configurações, cria as solicitações e orquestra o processo de aquisição.
kafka_config.yaml: Este arquivo contém todas as configurações para o nosso sistema Kafka, incluindo os detalhes do servidor bootstrap, os nomes dos tópicos, as configurações do produtor/consumidor, etc. Manter as configurações separadas do código torna fácil ajustar configurações sem modificar o código.
producers/: Este diretório contém o código para nossos vários produtores Kafka. Cada fonte de dados (por exemplo, API bancária, log do sistema) tem seu próprio produtor dedicado, permitindo tratamento especializado conforme necessário.
consumers/: Da mesma forma, este diretório contém o código para nossos consumidores Kafka. Cada destino downstream (por exemplo, Spark, Delta Lake) tem seu próprio consumidor, permitindo lógica de encaminhamento personalizado.

Decisões de Design e Raciocínio
Algumas das principais decisões de design tomadas na implementação do nosso sistema Kafka incluem:

Tópicos separados por categoria de evento : Ao invés de ter um único tópico para todas as transações Pix, optamos por ter tópicos separados por categoria de evento (pagamentos, recebimentos, estornos). Isso nos dá mais flexibilidade para escalar e processar cada tipo de evento de forma independente com base em seus padrões únicos de volume e velocidade.
Produtores e Consumidores Dedicados : Cada fonte de dados tem seu próprio produtor dedicado e cada destino downstream tem seu próprio consumidor dedicado. Isso permite um tratamento mais personalizado em cada ponta do pipeline Kafka. Por exemplo, diferentes fontes de dados podem exigir diferentes formatos de serialização, enquanto diferentes destinos downstream podem exigir diferentes lógicas de lote ou encaminhamento.
Configurações Externas : Todas as configurações do Kafka são mantidas em um arquivo YAML externo em vez de codificado no script. Isso torna muito mais fácil ajustar configurações sem modificar o código, e também facilita ter diferentes configurações para ambientes diferentes (por exemplo, dev, staging, prod).

Monitoramento e Métricas de Desempenho
Para garantir que nosso sistema Kafka esteja sempre operando com desempenho máximo, implementamos um monitoramento extensivo, incluindo:

Métricas do Kafka : Rastreamos todas as métricas chave do Kafka, como taxas de consumo, latência de ponta a ponta, offset lag, etc. Essas métricas são enviadas ao nosso sistema de monitoramento (Prometheus) e visualizadas em dashboards Grafana.
Logs de Aplicativos : Todos os nossos produtores e consumidores geram logs extensivos que nos permitem rastrear o progresso de cada mensagem através do sistema. Usamos a pilha ELK (Elasticsearch, Logstash, Kibana) para agregar e visualizar esses logs.
Alertas : Temos alertas configurados para acionar qualquer métrica do Kafka ou do aplicativo sair dos acontecimentos normais. Isso nos permite identificar e resolver proativamente quaisquer problemas antes que eles se tornem críticos.

Para mais detalhes sobre nossa configuração de monitoramento, consultemonitoramento / .
Para Recrutadores e Revisores de Código
Como a única engenheira trabalhando neste projeto, eu tive que tomar muitas decisões de design e implementação de forma independente. Ao revisar este código, você deve considerar:

Adequação do Kafka : O Kafka é a escolha correta para este caso de uso de aquisição de dados de alta velocidade? As garantias de desempenho, durabilidade e escalabilidade do Kafka estão sendo totalmente aproveitadas?
Organização do Código : O código é modular, legível e segue as melhores práticas? Quais são as preocupações específicas separadas (por exemplo, produtores vs consumidores, código vs configuração)?
Resiliência e Tratamento de Erros : Como o sistema lida com falhas (por exemplo, indisponibilidade do servidor Kafka, mensagens malformadas)? Existem mecanismos adequados para novas tentativas e filas de mensagens mortas?
Desempenho e Otimização : O código faz uso eficiente dos recursos? Há oportunidades para otimização de latência ou rendimento (por exemplo, ajuste de tamanho de lote, atualizações)?
Extensibilidade : Quão fácil é adicionar novos produtores ou consumidores? O sistema pode acomodar novos tipos de eventos ou alterações nos formatos de dados?

Acredito que este sistema Kafka demonstra minha capacidade de projetar, construir e operar pipelines de dados críticos que podem lidar com as demandas implacáveis ​​do mundo real. Estou ansioso para discutir as compensações arquitetônicas, mergulhar nos detalhes da implementação e explorar como esse sistema pode ser aprimorado.
Contato
Se você tiver alguma dúvida ou quiser discutir este sistema Kafka em mais detalhes, sinta-se à vontade para entrar em contato:

E-mail: lugonc.lga@gmail.com
LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)

agradeço a oportunidade de apresentar meu trabalho!
