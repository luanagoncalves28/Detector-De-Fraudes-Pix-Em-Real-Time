## Monitoramento de Infraestrutura

### Visão Geral

Bem-vindo ao centro de controle para o monitoramento da infraestrutura do meu pipeline de detecção de fraudes Pix! Este subdiretório contém todas as configurações e automações que desenvolvi para monitorar continuamente a saúde e o desempenho dos componentes de infraestrutura que sustentam minha solução.

Como engenheira de machine learning, entendo que a infraestrutura é a espinha dorsal de qualquer sistema de produção. Não importa quão sofisticados sejam meus modelos, eles só podem agregar valor de negócio se a infraestrutura subjacente for robusta, escalável e altamente disponível. É por isso que coloco grande ênfase no monitoramento proativo da infraestrutura.

### O que Estou Monitorando

Meu sistema de monitoramento de infraestrutura abrange todos os principais componentes do meu pipeline, incluindo:

1. **Servidores**: Acompanho de perto métricas como utilização de CPU, memória, espaço em disco e largura de banda de rede para todos os servidores que executam meus serviços. Isso me ajuda a identificar estrangulamentos e escalar proativamente.

2. **Banco de Dados**: Monitoro a saúde e o desempenho dos meus bancos de dados, rastreando métricas como conexões abertas, latência de consulta, taxa de hits de cache e crescimento do armazenamento. Isso é crucial para garantir tempos de resposta rápidos para minhas APIs.

3. **Kubernetes Clusters**: Como opero meus serviços em contêineres orquestrados pelo Kubernetes, monitoro de perto métricas a nível de cluster, como contagens de pods, uso de recursos por namespace, e saúde de nós.  

4. **Filas de Mensagens**: Acompanho o comprimento da fila, idade das mensagens, e taxas de entrada/saída para minhas filas Kafka e RabbitMQ para garantir um processamento suave de dados.

5. **Gateways de API**: Monitoro as taxas de solicitação, latências e códigos de status HTTP nos meus gateways de API para rapidamente detectar interrupções ou degradação da performance.

### Como Eu Monitoro

Para habilitar esse monitoramento de infraestrutura abrangente, aproveitei uma pilha de ferramentas de código aberto líder da indústria:

1. **Prometheus**: Prometheus é meu sistema principal de coleta de métricas. Ele reúne dados de séries temporais de métricas expostas por vários exportadores (por exemplo, node_exporter para métricas de servidor, mysqld_exporter para métricas de banco de dados, etc.).

2. **Grafana**: Eu uso Grafana para visualizar as métricas coletadas pelo Prometheus. Criei painéis interativos que me dão uma visão em tempo real da saúde do meu sistema, permitindo que eu identifique rapidamente quaisquer anomalias.

3. **Alertmanager**: Configurei o Alertmanager para acionar alertas com base em regras predefinidas (por exemplo, uso de CPU > 90% por 5 minutos). Isso garante que eu seja proativamente notificado sobre potenciais problemas antes que eles impactem os usuários finais.

4. **Loki**: Para agregação e consulta de logs, uso Loki. Ele integra-se perfeitamente com o Grafana, permitindo que eu correlacione spikes em métricas com entradas de log relevantes para depuração mais rápida.

### Como Usar Este Diretório

Aqui está um rápido tour do que você encontrará neste diretório:

- `prometheus`: Contém os arquivos de configuração para a implantação do Prometheus, incluindo regras de alerta.

- `grafana`: Contém definições de dashboard do Grafana e templates de painel pré-configurados.

- `exporters`: Contém as configurações para os vários exportadores de métricas em execução em diferentes componentes do sistema.

- `alertmanager`: Contém os arquivos de configuração do Alertmanager, incluindo canais de notificação e roteamento de alertas.

- `scripts`: Contém vários scripts de automação para implantar e gerenciar a pilha de monitoramento.

### Para Recrutadores e Revisores

Como a única engenheira de machine learning trabalhando neste projeto, a responsabilidade de garantir a confiabilidade e a performance da infraestrutura caiu sobre mim. Isso exigiu que eu me aprofundasse em DevOps e SRE princípios e práticas.

Ao revisar as configurações e automações neste diretório, sugiro considerar:

1. A solução de monitoramento é abrangente em sua cobertura dos principais componentes da infraestrutura?

2. As escolhas das ferramentas (Prometheus, Grafana, etc.) são apropriadas e seguem as melhores práticas da indústria?  

3. Os painéis e alertas fornecem insights acionáveis sobre a saúde do sistema? Eles são bem organizados e fáceis de entender?

4. As automações de implantação e gerenciamento são robustas, bem documentadas e fáceis de manter?

5. A solução de monitoramento é ela própria altamente disponível e resiliente a falhas?

Estou extremamente orgulhosa do sistema de monitoramento abrangente e eficiente que projetei e implantei. Acredito que ele demonstra não apenas minhas habilidades técnicas, mas também meu compromisso inabalável em garantir a confiabilidade e o desempenho dos sistemas que construo.

### Contato

Se você tiver alguma dúvida ou feedback, ou se quiser agendar uma conversa para mergulhar mais fundo nesta arquitetura de monitoramento, não hesite em entrar em contato:

- Email: lugonc.lga@gmail.com

- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
