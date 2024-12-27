# Monitoramento do Pipeline - Detector de Fraudes Pix
## Visão Geral
Este subdiretório contém as configurações e automações que desenvolvi para monitorar continuamente o desempenho e a integridade do meu pipeline de detecção de fraudes em tempo real. 

Como engenheira de machine learning, entendo que monitorar a saúde do meu pipeline é tão crucial quanto monitorar meus modelos em produção. Preciso ter visibilidade em tempo real de como cada componente está se saindo, desde a ingestão de dados até a entrega das previsões, para garantir que meu sistema esteja sempre operando com desempenho máximo.

## O que Estou Monitorando
Meu sistema de monitoramento do pipeline abrange todos os principais componentes da minha solução, incluindo:

1. **Ingestão de Dados**: Monitoro as taxas de ingestão do Kafka, latência e throughput para garantir que os dados estejam fluindo sem problemas. 

2. **Processamento de Dados**: Acompanho as métricas de processamento do Spark, como duração das tarefas, utilização de recursos e taxas de erro para identificar possíveis gargalos ou problemas.

3. **Armazenamento**: Verifico a integridade e a consistência dos dados armazenados no Delta Lake, monitorando métricas como o tamanho das tabelas, a distribuição dos dados e a latência das consultas.

4. **Treinamento e Inferência do Modelo**: Com o MLflow, monitoro as métricas dos experimentos, os parâmetros do modelo, as métricas de desempenho e os artefatos gerados durante o treinamento. Para os modelos implantados, rastreio a latência de inferência, o throughput e as taxas de erro.

## Como Eu Monitoro
Para habilitar esse monitoramento abrangente do pipeline, aproveitei um conjunto de ferramentas de código aberto líderes do setor:

1. **Prometheus**: Meu sistema principal de coleta de métricas. Ele agrega dados de séries temporais de métricas expostas por vários exportadores (por exemplo, JMX exporter para métricas do Spark, webhooks para métricas do Kafka, etc.).

2. **Grafana**: Utilizo o Grafana para visualizar as métricas coletadas pelo Prometheus. Criei painéis interativos que me dão uma visão em tempo real da integridade do pipeline, permitindo que eu identifique rapidamente quaisquer anomalias.  

3. **Alertmanager**: Configurei o Alertmanager para disparar alertas com base em regras predefinidas (por exemplo, latência de processamento > 5 min). Isso garante que eu seja proativamente notificada sobre potenciais problemas antes que eles impactem os usuários finais.

## Como Utilizar Este Diretório
Aqui está um rápido tour do que você encontrará neste diretório:

- `prometheus/`: Contém os arquivos de configuração para a implantação do Prometheus, incluindo as regras de alerta e os alvos de coleta (arquivos `prometheus.yml` e `alert.rules`).

- `grafana/`: Contém os arquivos de configuração e provisionamento do Grafana. O subdiretório `dashboards/` armazena as definições dos painéis pré-configurados.

## Para Recrutadores e Revisores
Como a engenheira de machine learning responsável por este pipeline, entendo que a confiabilidade e o desempenho da solução são tão importantes quanto a precisão dos modelos. 

Ao revisar as configurações e automações neste diretório, sugiro considerar:

1. A solução de monitoramento cobre de maneira abrangente os principais componentes do pipeline?

2. As escolhas das ferramentas (Prometheus, Grafana, etc.) são apropriadas e seguem as melhores práticas do setor?

3. Os painéis e alertas fornecem insights acionáveis sobre a integridade do pipeline? Eles são bem organizados e fáceis de entender?

4. As configurações de coleta de métricas e regras de alertas são abrangentes e capturam os principais indicadores de desempenho e de saúde?

Estou extremamente orgulhosa do sistema de monitoramento robusto e completo que projetei e implementei para este pipeline. Acredito que ele demonstra meu compromisso não apenas com a precisão do modelo, mas também com a confiabilidade e a eficiência do sistema como um todo.  

## Contato
Se você tiver alguma dúvida ou feedback, ou se quiser agendar uma conversa para mergulhar mais fundo nessa arquitetura de monitoramento, não hesite em entrar em contato:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
