# Monitoramento de Modelos - Detector de Fraudes Pix
## Visão Geral 

Bem-vindo ao centro de controle para o monitoramento dos meus modelos de detecção de fraude em produção! Este subdiretório contém todas as configurações e automações que desenvolvi para monitorar continuamente a performance e a integridade dos modelos que criei para identificar transações fraudulentas no Pix em tempo real.

Como engenheira de machine learning, entendo que o trabalho não termina quando um modelo é implantado. Na verdade, é nesse momento que o monitoramento vigilante se torna absolutamente crucial. Com milhões de transações Pix fluindo pelos meus modelos a cada dia, preciso ter visibilidade em tempo real de como eles estão se saindo para garantir que estejam sempre realizando detecções precisas.

## O que Estou Monitorando

Meu sistema de monitoramento de modelos se concentra em três aspectos principais:

1. **Distribuição dos Dados**: Monitoro como as características dos dados de entrada mudam ao longo do tempo. Mudanças significativas na distribuição podem indicar "data drift", o que pode degradar a performance do modelo se não for tratado. 

2. **Performance do Modelo**: Acompanho de perto métricas como precisão, recall, F1-score e AUC-ROC para cada modelo em produção. Uma queda nessas métricas pode sinalizar a necessidade de retreinamento.

3. **Comportamento do Modelo**: Analiso os padrões nas previsões do modelo para identificar anomalias. Por exemplo, um súbito aumento na taxa de transações sinalizadas como fraudulentas pode indicar um problema que requer investigação.

## Como Eu Monitoro

Para habilitar esse monitoramento abrangente do modelo, utilizo uma combinação de ferramentas de código aberto líderes da indústria:

1. **Prometheus**: Uso o Prometheus para coletar métricas dos endpoints de serviço do modelo. Isso inclui métricas de performance (latência, requests por segundo) e métricas de negócio (taxas de fraude).

2. **Grafana**: Crio painéis no Grafana para visualizar as métricas coletadas pelo Prometheus. Esses painéis me dão uma visão em tempo real da saúde de cada modelo, permitindo que eu identifique rapidamente qualquer comportamento anormal.

3. **Kafka**: Uso tópicos do Kafka para capturar todas as previsões feitas pelos modelos, juntamente com os dados de entrada correspondentes. Esses dados são essenciais para análises de data drift e investigações de anomalias.

4. **Python + Jupyter**: Tenho um conjunto de notebooks Jupyter que uso para análises detalhadas dos dados de previsão capturados do Kafka. Isso inclui scripts para calcular métricas de data drift, comparar distribuições de dados e investigar transações sinalizadas.

## Como Utilizar Este Diretório

Aqui está uma visão geral do que você encontrará neste diretório:

- `prometheus/`: Contém os arquivos de configuração para as regras de alerta do Prometheus e os endpoints de coleta de métricas.

- `grafana/`: Contém os arquivos de configuração e provisionamento do Grafana. O subdiretório `dashboards/` armazena as definições dos painéis pré-configurados para monitorar modelos.

- `notebooks/`: Contém os notebooks Jupyter que uso para análises detalhadas off-line dos dados de previsão. 

## Para Recrutadores e Revisores 

Como a engenheira de machine learning que projetou e implementou este sistema de monitoramento de modelos, estou extremamente orgulhosa de sua abrangência e robustez. 

Ao revisar as configurações e automações neste diretório, convido você a considerar:

1. A estratégia de monitoramento cobre de forma abrangente os principais aspectos de data drift, performance do modelo e comportamento anômalo?

2. As ferramentas escolhidas (Prometheus, Grafana, Kafka) são apropriadas e estão sendo usadas de acordo com as melhores práticas?

3. Os painéis e notebooks fornecem informações acionáveis sobre a saúde e performance dos modelos? Eles são bem organizados e fáceis de entender?

4. As configurações de coleta de métricas e regras de alerta capturam os principais indicadores de desempenho e integridade do modelo?

Estou muito orgulhosa do sistema robusto e completo que projetei e implementei para garantir que meus modelos de detecção de fraude permaneçam precisos, confiáveis e eficientes em produção. Acredito que isso demonstra meu profundo compromisso não apenas com a ciência de dados, mas também com a engenharia necessária para criar soluções de ML verdadeiramente impactantes.

## Contato

Se você tiver alguma dúvida ou feedback, ou se quiser agendar uma conversa para se aprofundar nesta arquitetura de monitoramento de modelos, não hesite em entrar em contato:

- Email: lugonc.lga@gmail.com  
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
