# Ingestão de Dados - Detector de Fraudes Pix
## Visão Geral
Bem-vindo ao diretório de ingestão de dados do nosso sistema de detecção de fraudes Pix em tempo real! Este é o ponto de partida para o fluxo de dados, onde capturo dados brutos de transações Pix à medida que eles são gerados e os transmito de forma confiável e eficiente para as etapas subsequentes de processamento e análise.

A ingestão de dados é um componente crucial do pipeline, pois garante que tenhamos um fluxo constante e em tempo real de dados para trabalhar. Qualquer gargalo ou interrupção aqui pode propagar e afetar todo o sistema. Como tal, este módulo foi projetado com um foco inabalável em alta disponibilidade, taxa de transferência e baixa latência.
## Abordagem de Ingestão de Dados
Utilizo uma abordagem de ingestão de dados de duas vertentes:

1. **Apache Kafka**: O Apache Kafka serve como nosso backbone de ingestão de dados primário. Escolhemos o Kafka devido à sua capacidade comprovada de lidar com fluxos massivos de dados em tempo real com latência extremamente baixa. A arquitetura distribuída do Kafka também fornece resiliência inerente - se um nó falhar, os outros podem assumir a carga sem qualquer interrupção no fluxo de dados.

   Você pode explorar o código, as configurações e a documentação relacionados em [kafka/](kafka/).

2. **Apache Spark**: Também utilizo o Apache Spark para ingestão de dados. O Spark é uma ferramenta poderosa para processamento de dados distribuídos e seu modelo de micro-batching é particularmente adequado para ingerir grandes lotes de dados rapidamente. Utilizo o Spark para complementar o Kafka, lidando com picos de volume de dados ou fontes de dados que não são adequadas para streaming contínuo.

   Os detalhes da implementação do Spark para ingestão podem ser encontrados em [spark/](spark/).
## Fluxo de Trabalho de Ingestão
O fluxo de trabalho típico de ingestão envolve os seguintes passos:

1. **Aquisição**: Os dados brutos das transações Pix são capturados de várias fontes, como APIs de instituições financeiras, logs do sistema e streamings de dados.

2. **Enfileiramento**: Os dados capturados são imediatamente enfileirados no Kafka. O Kafka atua como um buffer, desacoplando a aquisição de dados do processamento e garantindo que nenhum dado seja perdido se houver um pico de volume ou uma interrupção a jusante.

3. **Lotes**: Para fontes de dados de alto volume que não requerem processamento de streaming contínuo, usO o Spark para ingerir os dados em micro-lotes. Isso permite processar grandes quantidades de dados de forma eficiente.

4. **Encaminhamento**: Uma vez ingeridos no sistema, os dados são encaminhados para as fases de processamento e armazenamento, onde são transformados, enriquecidos e preparados para análise.
## Monitoramento e Recuperação
Para garantir que o sistema de ingestão de dados esteja sempre operando em sua capacidade máxima, implementei monitoramento extensivo e mecanismos de recuperação automática:

- **Monitoramento de Desempenho**: Todos os componentes-chave, como produtores Kafka, consumidores e executores Spark, são continuamente monitorados para latência, taxa de transferência e utilização de recursos. Quaisquer desvios das métricas normais disparam alertas para investigação imediata.

- **Verificações de Integridade de Dados**: Realizo verificações regulares de integridade de dados nos dados ingeridos para identificar quaisquer corrupções, inconsistências ou lacunas nos dados. Quaisquer problemas detectados são automaticamente reportados e resolvidos.

- **Recuperação de Falhas**: Os sistemas Kafka e Spark são configurados para recuperação automática de falhas. Se um nó ou executor falhar, ele é automaticamente reiniciado e retoma de onde parou, garantindo processamento de dados contínuo e ininterrupto.
## Para Recrutadores e Revisores de Código
Como engenheira de machine learning, acredito firmemente que a base de qualquer pipeline de análise de dados robusto é um sistema de ingestão de dados bem arquitetado. Ao revisar este módulo, convido você a considerar:

1. **Escolha da Tecnologia**: Avaliei cuidadosamente as garantias de desempenho, escalabilidade e resistência fornecidas por Kafka e Spark? Estas escolhas estão bem alinhadas com os requisitos do sistema?

2. **Implementação**: O código aproveitou efetivamente os recursos de Kafka e Spark? Seguiu as melhores práticas para tópicos de design, gerenciamento de erros e eficiência?

3. **Monitoramento e Recuperação**: Existem sistemas abrangentes para monitorar o desempenho da ingestão e a integridade dos dados? Existem mecanismos para detectar e se recuperar automaticamente de falhas?

4. **Flexibilidade**: O sistema pode acomodar facilmente novas fontes de dados ou alterações nos formatos de dados? É modular e extensível?

Mais do que apenas um exercício técnico, acredito que este módulo de ingestão de dados demonstra minha capacidade de projetar e implementar sistemas de dados de missão crítica que podem suportar as demandas de negócios do mundo real. Estou ansiosa para aprofundar os detalhes técnicos e discutir como essa abordagem pode ser adaptada a diferentes cenários.

## Contato
Se você tiver alguma dúvida ou quiser discutir a arquitetura de ingestão de dados em mais detalhes, sinta-se à vontade para entrar em contato:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)

Estou sempre feliz em mergulhar nos detalhes técnicos e discutir potenciais melhorias ou adaptações para diferentes casos de uso. Obrigada pelo seu interesse neste projeto!
