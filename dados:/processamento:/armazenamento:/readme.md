# Armazenamento de Dados Processados

## Visão Geral

Bem-vindo ao meu sistema de armazenamento de dados processados! Este diretório contém a infraestrutura e pipelines que desenvolvi para armazenar, gerenciar e servir os dados resultantes dos meus jobs de processamento de lote e streaming.

Como engenheira de machine learning trabalhando em detecção de fraudes em tempo real, reconheço que ter uma camada de armazenamento robusta, performática e governada é tão crítico quanto os próprios pipelines de processamento. É aqui que os resultados dos meus modelos analíticos são materializados, tornando-se a base para insights acionáveis, treinamento de modelos e análises posteriores.

## Arquitetura de Armazenamento de Dados

Implementei uma Arquitetura Multi-Camadas (Multi-Tier Architecture) para o meu armazenamento de dados processados, também conhecida como Arquitetura de Medalhão (Bronze, Prata e Ouro):

1. **Camada Bronze**: Esta camada contém os dados brutos ou minimamente processados diretamente dos meus pipelines de ingestão. Os dados aqui estão na sua forma mais granular e não são tipicamente usados para análise direta. A camada Bronze funciona como um landing pad para todos os dados de entrada.

2. **Camada Prata**: Nesta camada, os dados brutos passaram por alguns processos de limpeza, transformação e enriquecimento. Os dados podem ser agregados a um nível mais amigável para análise e inconsistências ou duplicações teriam sido resolvidas. A camada Prata é adequada para a maioria das necessidades de análise e treinamento de modelo.

3. **Camada Ouro**: Esta camada contém dados altamente refinados, agregados e enriquecidos que são diretamente compatíveis com os requisitos de negócios. Os dados aqui podem ser resumidos a níveis mais altos (por exemplo, médias diárias, totais mensais) e geralmente seriam usados para relatórios e dashboards executivos.

## Tecnologia de Armazenamento: Delta Lake

Para implementar minha arquitetura Multi-Camadas, escolhi o Delta Lake como minha tecnologia de armazenamento primária. O Delta Lake é uma camada de armazenamento de código aberto construída sobre o data lake que fornece transações ACID, controle de versão de dados e outras funcionalidades de data warehousing.

Alguns dos motivos pelos quais escolhi o Delta Lake incluem:

1. **Integração Perfeita com Spark**: O Delta Lake trabalha perfeitamente com o Spark, que é a espinha dorsal dos meus pipelines de processamento. Posso ler e gravar para o Delta Lake usando APIs Spark familiares.

2. **Suporte ACID**: O Delta Lake fornece transações ACID completas, garantindo consistência de dados mesmo com múltiplos gravadores e em caso de falhas. Isto é crucial para um sistema de detecção de fraudes onde a precisão e a confiabilidade dos dados são primordiais.

3. **Controle de Versão de Dados e Viagem no Tempo**: Cada gravação para o Delta Lake cria uma nova versão do dado, permitindo rastrear facilmente mudanças e reverter para versões anteriores se necessário. Isto é útil para depuração, auditoria e reprodutibilidade.

4. **Desempenho e Escalabilidade**: O Delta Lake é otimizado para operações rápidas de leitura e gravação, mesmo em datasets muito grandes. Ele também escala perfeitamente com o Spark, permitindo processamento distribuído.

## Fluxos de Trabalho de Armazenamento de Dados

Meus dados fluem através das camadas de armazenamento da seguinte forma:

1. **Ingestão para Bronze**: Os dados brutos das transações Pix são inicialmente ingeridos na camada Bronze, seja a partir do pipeline de processamento em lote (a partir de fontes como Kafka) ou do pipeline de streaming (usando Spark Structured Streaming). Os dados são armazenados no formato bruto, particionados por timestamp de ingestão.

2. **Bronze para Prata**: Os jobs Spark leem os dados da camada Bronze, aplicam as lógicas de processamento e transformação necessárias e gravam os resultados na camada Prata. Estes jobs são acionados em intervalos regulares (por exemplo, a cada hora) para mover continuamente dados através do pipeline.

3. **Prata para Ouro**: Para dados necessários a nível agregado (por exemplo, para relatórios diários), os jobs Spark leem da camada Prata, realizam as agregações necessárias e gravam os resultados sumarizados na camada Ouro. Estes jobs podem rodar em intervalos mais longos (por exemplo, diariamente).

4. **Treinamento e Pontuação do Modelo**: Os jobs de treinamento de modelos de detecção de fraude leem dados da camada Prata para criar conjuntos de treinamento e teste. Os modelos treinados são então aplicados aos dados de streaming na camada Prata para pontuar transações em tempo quase real.

## Monitoramento e Governança de Dados

Para assegurar a saúde, performance e qualidade do meu armazenamento de dados, implementei monitoramento e governança de dados abrangentes:

1. **Validação de Qualidade de Dados**: Executo verificações de qualidade de dados regulares em cada camada para identificar quaisquer inconsistências, valores ausentes ou anomalias. Quaisquer problemas são relatados e tratados prontamente.

2. **Monitoramento de Performance**: Métricas chave como latência de leitura/gravação, throughput e utilização de armazenamento são continuamente rastreadas. Alertas são configurados para identificar e resolver estrangulamentos de desempenho.

3. **Lineage e Auditoria de Dados**: Aproveito os recursos de controle de versão e lineage do Delta Lake para manter um registro completo da jornada de cada dado através do pipeline. Isso é crucial para depuração, reprodutibilidade e conformidade regulatória.

4. **Controles de Segurança e Acesso**: Implementei controles de acesso granulares para assegurar que somente usuários e processos autorizados possam acessar os dados. Todos os dados são criptografados em repouso e em trânsito.

## Para Recrutadores e Revisores de Código

Como a engenheira de dados principal por trás deste armazenamento de dados processados, estou extremamente orgulhosa da arquitetura robusta, escalável e orientada à governança que projetei.

Ao revisar o código e a documentação neste diretório, sugiro avaliar os seguintes aspectos:

1. A escolha do Delta Lake e da arquitetura Multi-Camadas está bem fundamentada e alinhada com os requisitos do caso de uso de detecção de fraude em tempo real?

2. Os fluxos de trabalho de dados através das camadas de armazenamento são claros, eficientes e tolerantes a falhas? Existe uma separação clara de preocupações entre as camadas?

3. As considerações de desempenho, como particionamento, compactação e índices, são efetivamente aproveitadas para otimizar as operações de leitura e gravação?

4. As práticas de governança e qualidade de dados são abrangentes e robustas o suficiente para um caso de uso crítico como detecção de fraude?

5. A arquitetura geral é modular, extensível e capaz de escalar para acomodar o crescimento futuro dos dados e evolução dos requisitos de negócios?

## Contato

Se você tiver alguma dúvida ou feedback, ou se quiser agendar uma conversa para mergulhar mais fundo nesta arquitetura de armazenamento de dados, não hesite em entrar em contato:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
