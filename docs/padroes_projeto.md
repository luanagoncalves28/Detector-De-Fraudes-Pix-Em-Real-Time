# Padrões de Projeto - Pipeline Analítico de Detecção de Fraudes Pix

## Visão Geral

Este documento descreve os principais padrões de projeto de software e arquiteturais utilizados no desenvolvimento do Pipeline Analítico de Detecção de Fraudes Pix. A adoção desses padrões visa promover um sistema modular, escalável, resiliente e de fácil manutenção, seguindo as melhores práticas da engenharia de software.

## 1. Arquitetura Orientada a Eventos

### Padrão: Event-Driven Architecture (EDA)

- **Descrição**: A arquitetura orientada a eventos é um padrão arquitetural onde a produção, detecção, consumo e reação a eventos são as atividades centrais. Isso permite baixo acoplamento e alta escalabilidade.

- **Aplicação no Projeto**: A ingestão de transações Pix é feita através do Apache Kafka, que serve como um backbone orientado a eventos. Os componentes de processamento e ação são acionados por eventos, promovendo um fluxo de dados assíncrono e flexível.

- **Benefícios**: 
  - Desacoplamento entre produtores e consumidores de eventos
  - Escalabilidade independente de cada componente
  - Facilidade para adicionar novos consumidores de eventos
  - Resiliência, já que falhas em um consumidor não afetam os demais

## 2. Microsserviços

### Padrão: Microservices Architecture

- **Descrição**: A arquitetura de microsserviços é um estilo arquitetural onde um aplicativo é construído como uma coleção de serviços pequenos, autônomos e fracamente acoplados. Cada serviço implementa uma capacidade de negócio específica.

- **Aplicação no Projeto**: O pipeline é composto por vários microsserviços, cada um responsável por uma função específica, como validação de transações, detecção de anomalias, acionamento de ações, etc. Esses serviços se comunicam através de APIs bem definidas.

- **Benefícios**:
  - Modularidade e facilidade de manutenção
  - Escalabilidade granular de cada serviço conforme a demanda
  - Liberdade para usar a tecnologia mais adequada para cada serviço
  - Agilidade no desenvolvimento e deploy de novas funcionalidades

## 3. Processamento de Streams

### Padrão: Stream Processing

- **Descrição**: O processamento de streams é um paradigma de programação para processar dados em tempo real à medida que eles chegam, ao contrário do processamento em lote tradicional. É especialmente útil para cenários que exigem insights em tempo real e baixa latência.

- **Aplicação no Projeto**: O Spark Structured Streaming é usado para processar as transações Pix em tempo real conforme elas são ingeridas pelo Kafka. Isso permite a validação, enriquecimento e detecção de anomalias com latência mínima.

- **Benefícios**:
  - Processamento em tempo real com baixa latência
  - Capacidade de lidar com dados em movimento contínuo
  - Escalabilidade para altos volumes de dados
  - Facilitação de casos de uso como monitoramento e alerta em tempo real

## 4. Lambda Architecture

### Padrão: Lambda Architecture

- **Descrição**: A Arquitetura Lambda é um padrão de processamento de dados que busca balancear latência, throughput e tolerância a falhas combinando métodos de processamento em lote e em tempo real. Ela é composta por três camadas: batch, speed e serving.

- **Aplicação no Projeto**: Embora o foco principal seja o processamento em tempo real (camada speed), também é utilizado o processamento em lote (camada batch) para tarefas como treinamento de modelos e geração de visualizações. A camada serving é representada pelo Delta Lake.

- **Benefícios**:
  - Combina as vantagens do processamento em lote e em tempo real
  - Permite servir resultados com baixa latência e recalcular resultados quando necessário
  - Tolerância a falhas e capacidade de lidar com dados atrasados ou reprocessamento
  - Suporta uma ampla gama de casos de uso analíticos

## 5. Camadas de Dados (Arquitetura Medalhão)

### Padrão: Data Layering (Bronze, Silver, Gold)

- **Descrição**: A arquitetura medalhão é uma abordagem de design para lagos de dados que divide os dados em camadas com níveis crescentes de estrutura e qualidade. As camadas típicas são Bronze (dados brutos), Silver (dados refinados) e Gold (dados agregados/prontos para consumo).

- **Aplicação no Projeto**: O Delta Lake é usado para implementar a arquitetura medalhão. As transações brutas são armazenadas na camada Bronze, validadas e enriquecidas na camada Silver, e agregadas para consumo na camada Gold.

- **Benefícios**:
  - Separação clara de preocupações em cada etapa do pipeline de dados
  - Possibilidade de reprocessar e corrigir dados em cada camada
  - Facilidade para diferentes consumidores acessarem os dados no nível de refinamento necessário
  - Governança e rastreabilidade de dados aprimoradas

## 6. Micropadrões de Streaming

### Padrão: Micropatterns for Streaming (Filtering, Joining, Aggregating, Branching, Windowing)

- **Descrição**: O processamento de streams envolve vários cenários comuns que podem ser encapsulados em micropadrões tais como filtrar dados, juntar streams, agregar em janelas de tempo, ramificar fluxos, etc. Esses micropadrões fornecem blocos de construção reutilizáveis.

- **Aplicação no Projeto**: Vários micropadrões de streaming são usados no processamento com Spark Structured Streaming, como:
  - Filtrar transações inválidas
  - Unir transações com dados de perfil do cliente
  - Agregar métricas em janelas horárias para detecção de anomalias
  - Ramificar transações suspeitas para fluxos de alerta e bloqueio

- **Benefícios**:
  - Reutilização de lógicas comuns de processamento de streams
  - Expressividade e legibilidade do código
  - Guia para implementação das operações mais frequentes
  - Base para construir pipelines de streaming complexos

## 7. Arquitetura Federada de Machine Learning

### Padrão: Federated Machine Learning Architecture

- **Descrição**: Em uma arquitetura federada de machine learning, os modelos são treinados de forma descentralizada em nós locais (por exemplo, instituições financeiras) e depois agregados em um modelo global. Isso permite o aprendizado colaborativo preservando a privacidade dos dados.

- **Aplicação no Projeto**: Embora não implementado diretamente neste projeto individual, a arquitetura é projetada para permitir o aprendizado federado no futuro. Cada instituição poderia treinar modelos localmente em seus próprios dados de fraude e contribuir para um modelo global mais robusto.

- **Benefícios**:
  - Permite o aprendizado com dados distribuídos mantendo a privacidade
  - Modelos mais robustos treinados em uma ampla gama de padrões de fraude
  - Reduz a necessidade de compartilhar dados sensíveis
  - Alinhado com regulamentações de proteção de dados como LGPD

## 8. Observabilidade e Monitoramento

### Padrão: Observability and Monitoring

- **Descrição**: Observabilidade é a capacidade de compreender o estado interno de um sistema com base em suas saídas externas. Isso geralmente envolve a coleta abrangente de métricas, logs e traces. O monitoramento é o processo de acompanhar essas informações para garantir a saúde e a performance do sistema.

- **Aplicação no Projeto**: Prometheus é usado para coletar métricas de todos os componentes do sistema, enquanto Grafana fornece dashboards para monitorar a saúde do pipeline e as principais métricas de negócio. O Alertmanager notifica as equipes sobre anomalias.

- **Benefícios**:
  - Visibilidade em tempo real do comportamento do sistema
  - Detecção proativa de problemas antes que afetem os usuários
  - Capacidade de depurar e rastrear a causa raiz de incidentes
  - Base para análise de performance e otimização contínua
  - Conformidade com requisitos de auditoria e regulação

## Conclusão

A aplicação desses padrões de projeto no Pipeline Analítico de Detecção de Fraudes Pix visa criar um sistema robusto, escalável e sustentável. A combinação de padrões de arquitetura como EDA e microsserviços promove baixo acoplamento e alta coesão, enquanto padrões de processamento de dados como Lambda e stream processing equilibram latência e throughput.

A adoção da arquitetura medalhão com o Delta Lake garante a governança e a qualidade dos dados em cada estágio, e a observabilidade fornecida por Prometheus e Grafana permite monitoramento e resposta proativa a problemas.

Embora nem todos os padrões (como federated learning) sejam implementados diretamente neste projeto individual, a arquitetura é projetada com extensibilidade em mente, permitindo a evolução contínua do sistema à medida que os requisitos de negócios e regulatórios mudam.

Esses padrões e princípios arquitetônicos, aplicados de forma holística, criam um sistema analítico de detecção de fraudes de última geração, capaz de lidar com os desafios únicos e em constante mudança do domínio de pagamentos instantâneos.
