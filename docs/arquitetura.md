# Arquitetura do Sistema de Detecção de Fraudes Pix com MLOps

## 1. Visão Geral

A arquitetura deste sistema de detecção de fraudes em transações Pix foi meticulosamente projetada visando alta escalabilidade, resiliência e baixo acoplamento. Ela é capaz de processar um altíssimo volume de transações em tempo real, atendendo aos rigorosos requisitos de performance e confiabilidade exigidos pelo domínio de pagamentos instantâneos. 

A solução adota uma abordagem de arquitetura orientada a serviços e baseada em eventos, onde os componentes são organizados em camadas com responsabilidades bem definidas e se comunicam através de um barramento de eventos central (Apache Kafka). Essa arquitetura desacoplada permite que cada serviço evolua independentemente e que o sistema como um todo seja facilmente escalado horizontalmente.

## 2. Diagrama de Arquitetura

![image](https://github.com/user-attachments/assets/63c44086-a2e3-4317-8715-ab017d890976)

O diagrama acima apresenta uma visão geral de alto nível dos principais componentes da arquitetura:

- **Camada de Ingestão de Dados**: Responsável por consumir os dados de transações Pix de múltiplas fontes (APIs de instituições financeiras, arquivos batch), aplicar validações e publicar as transações brutas em tópicos Kafka para processamento posterior.

- **Camada de Processamento de Stream**: Consome as transações dos tópicos Kafka, enriquece os dados, aplica as regras de detecção de fraude em tempo real usando modelos de ML servidos como microsserviços, e publica as transações classificadas em novos tópicos.

- **Camada de Armazenamento (Data Lakehouse)**: Persiste os dados processados no Google Cloud Storage usando Delta Lake, seguindo a arquitetura medallion (Bronze, Silver, Gold) para análises exploratórias, treinamento de modelos e consultas.
  
- **Camada de Serviços**: Expõe APIs REST para consulta dos resultados da análise de fraude em tempo real e integração com sistemas de ação (bloqueio de transações, alertas).

- **Camada de Machine Learning (MLOps)**: Orquestra o treinamento contínuo dos modelos a partir dos dados históricos no Delta Lake, servindo-os via endpoints para inferência em tempo real no processamento de stream.

## 3. Principais Componentes e Tecnologias

### 3.1. Apache Kafka

O Apache Kafka atua como a espinha dorsal da arquitetura orientada a eventos. Ele é responsável pela ingestão de dados de transações Pix em tempo real, garantindo baixa latência e alta vazão. As transações são publicadas em tópicos Kafka específicos, criando um buffer para processamento posterior.

### 3.2. Apache Spark (Structured Streaming)

O processamento de stream é realizado utilizando o Apache Spark com a API Structured Streaming. Ele consome as transações brutas dos tópicos Kafka, realiza o enriquecimento com dados de referência e aplica as regras de detecção de fraude em tempo real através da invocação dos modelos de ML. As transações processadas são então publicadas em novos tópicos para consumo por outras partes do sistema.

### 3.3. Google Cloud Storage + Delta Lake

Os dados processados são armazenados no Google Cloud Storage utilizando o formato Delta Lake. A arquitetura Medallion é aplicada para organizar os dados em camadas:

- Bronze: Dados brutos ingeridos dos tópicos Kafka.
- Silver: Dados limpos, conformados e enriquecidos.  
- Gold: Dados agregados e sumarizados, prontos para consumo por processos analíticos e de ML.

O Delta Lake traz benefícios como transações ACID, controle de versão e time-travel, cruciais para casos de uso de ML.

### 3.4. MLflow

O MLflow é utilizado para gerenciar todo o ciclo de vida dos modelos de ML na camada de MLOps. Ele controla os experimentos, versionamento de modelos, registro de modelos no Model Registry para promoção a produção, e implantação dos modelos como endpoints servidos.

### 3.5. Tecnologias Adicionais

- **Google Kubernetes Engine (GKE)**: Orquestração de contêineres para implantação e escala dos microsserviços.
- **Terraform**: Provisionamento da infraestrutura como código.
- **Prometheus & Grafana**: Monitoramento do pipeline end-to-end e visualização de métricas.
- **Databricks**: Ambiente para Engenharia de dados e treinamento distribuído de modelos.

## 4. Padrões Arquiteturais e Boas Práticas

A arquitetura incorpora diversos padrões e boas práticas para garantir escalabilidade, resiliência e flexibilidade:

- **Arquitetura Orientada a Serviços (SOA)**: Os componentes são desenvolvidos como serviços independentes com APIs bem definidas.

- **Arquitetura baseada em Eventos**: A comunicação entre os serviços é feita predominantemente através de eventos publicados nos tópicos Kafka.

- **Segregação Comando-Consulta (CQRS)**: As operações de escrita (processamento) são separadas das de leitura (servir resultados).

- **Orquestração de Contêineres**: Todos os componentes são implantados como contêineres no Kubernetes, permitindo escala, resiliência e portabilidade.

- **Pipeline de CI/CD**: Processos automatizados de build, teste e implantação usando metodologias IaC.

- **Observabilidade**: Monitoramento centralizado de logs, métricas e traces incorporado em todas as camadas.

- **MLOps**: Adoção de práticas de MLOps para entregar modelos de ML em produção de forma contínua e automatizada.

## 5. Fluxos de Dados Principais

1. Transações Pix brutas são ingeridas pela **Camada de Ingestão** e publicadas em tópicos Kafka.

2. A **Camada de Processamento de Stream** consome as transações brutas, enriquece, aplica regras de fraude e publica transações classificadas em tópicos refinados.

3. A **Camada de Armazenamento** persiste as transações nas camadas Bronze, Silver e Gold do Data Lakehouse.

4. A **Camada de Serviços** consulta os dados processados para servir resultados através de APIs REST.

5. A **Camada MLOps** treina e atualiza continuamente os modelos de ML com os dados do Data Lakehouse e os disponibiliza para inferência online.

## 6. Considerações de Escalabilidade e Desempenho

Cada camada da arquitetura foi projetada com escalabilidade e desempenho em mente:

- A ingestão via Kafka permite processar altos volumes com baixa latência.
- O processamento de stream com Spark permite escalar horizontalmente workers conforme a carga.
- O armazenamento no Delta Lake no GCS oferece alta performance de leitura/escrita e escalabilidade.
- Os serviços são implantados no GKE, permitindo escala elástica via Horizontal Pod Autoscaler (HPA).
- O treinamento distribuído no Databricks permite reduzir o tempo de experiências de ML.

## 7. Considerações de Resiliência e Tolerância a Falhas

A arquitetura incorpora várias estratégias para garantir resiliência e tolerância a falhas:

- Kafka provê armazenamento resiliente das mensagens e permite reprocessamento em caso de falhas.
- O Spark Structured Streaming conta com checkpointing para recuperar o estado em caso de reinicializações.
- O Delta Lake suporta transações ACID, garantindo consistência dos dados.
- Os microsserviços implantados no GKE se beneficiam dos mecanismos de self-healing e replicação do Kubernetes.
- Os processos de ML têm versionamento de artefatos no MLflow, permitindo rollback em caso de problemas.

## 8. Evolução e Extensibilidade

A arquitetura foi concebida para ser flexível e extensível:

- Novos modelos de ML e regras de fraude podem ser facilmente incorporados e evoluídos independentemente.
- Serviços adicionais de enriquecimento e processamento podem ser adicionados sem impactar os existentes.
- A arquitetura medallion no Delta Lake permite que novos casos de uso analíticos sejam construídos sobre os dados existentes.
- O uso de Kafka permite ingerir dados de novas fontes sem alterações disruptivas na arquitetura.

## 9. Compliance e Segurança

A segurança e conformidade com regulamentações são aspectos fundamentais dessa arquitetura:

- Todas as transferências de dados ocorrem sobre canais encriptados (ex: SSL).
- Os microsserviços implantados no GKE seguem o princípio de least-privilege e contam com autenticação mútua (mTLS).
- O acesso aos dados no Data Lakehouse é rigorosamente controlado por IAM e políticas finas de acesso.
- Todos os dados sensíveis (PII) são criptografados em repouso e em trânsito.
- Os modelos de ML são constantemente monitorados quanto a fairness e drift.
- Os processos e fluxos de dados estão em conformidade com regulamentações como a LGPD.

## 10. Conjuntos de Dados Simulados

Como este é um projeto fictício com o intuito de demonstrar conhecimentos, habilidades e expertise em Engenharia de Machine Learning, serão criados conjuntos de dados sintéticos para simular um ambiente realista de transações Pix. Esses dados atuarão como a base para o pipeline de detecção de fraudes, permitindo testar e validar as estratégias empregadas, ao mesmo tempo em que mantém o projeto dentro dos limites da camada gratuita do Google Cloud Platform.

Os principais datasets a serem gerados incluem:

1. **Transações Pix (`transacoes_pix.csv`)**: 
   - Descrição: Simula transações Pix, incluindo transferências legítimas e potencialmente fraudulentas.
   - Campos chave: `id_transacao`, `timestamp`, `valor`, `chave_pix_origem`, `chave_pix_destino`, `tipo_transacao`, `status`.
   - Volume: 50.000 registros, sendo 0,5% (250) simulando transações suspeitas.

2. **Cadastro de Chaves Pix (`chaves_pix.csv`)**: 
   - Descrição: Representa o registro de chaves Pix no DICT (Diretório de Identificadores de Contas Transacionais).
   - Campos: `chave_pix`, `tipo_chave`, `cpf_cnpj`, `nome_titular`, `data_cadastro`, `status`.
   - Volume: 25.000 registros únicos.
   
3. **Dados de Usuários (`usuarios.csv`)**: 
   - Descrição: Contém informações básicas dos usuários do sistema Pix, como dados demográficos e de contato.
   - Campos: `id_usuario`, `cpf_cnpj`, `nome`, `email`, `telefone`, `data_cadastro`, `status`.
   - Volume: 20.000 registros únicos.

4. **Dispositivos Registrados (`dispositivos.csv`)**:
   - Descrição: Armazena os dispositivos registrados pelos usuários para realizar transações.
   - Campos: `id_dispositivo`, `id_usuario`, `tipo_dispositivo`, `data_registro`, `status`. 
   - Volume: 30.000 registros, com alguns usuários tendo múltiplos dispositivos.

5. **Histórico de Fraudes (`fraudes.csv`)**: 
   - Descrição: Registra casos confirmados de fraude que podem ser usados para treinar modelos de detecção.
   - Campos: `id_fraude`, `id_transacao`, `tipo_fraude`, `data_deteccao`, `valor_fraude`, `status`.
   - Volume: 1.000 registros.

6. **Limites de Transações (`limites_transacoes.csv`)**: 
   - Descrição: Armazena os limites de transação configurados para cada usuário/conta.
   - Campos: `id_usuario`, `limite_diario`, `limite_por_transacao`, `data_atualizacao`.
   - Volume: 20.000 registros, um para cada usuário.

7. **Log de Autenticação (`log_autenticacao.csv`)**: 
   - Descrição: Registra as tentativas de autenticação dos usuários.
   - Campos: `id_log`, `id_usuario`, `timestamp`, `tipo_autenticacao`, `status`, `id_dispositivo`.
   - Volume: 100.000 registros.

Esses datasets serão gerados utilizando scripts Python que garantem consistência entre os dados e incorporam padrões realistas, como sazonalidade de transações, distribuições não uniformes de valores e correlações entre tipos de usuários e comportamentos transacionais. 

Anomalias sutis, como sequências atípicas de transações ou atividades suspeitas originadas de contas recém-criadas, serão cuidadosamente inseridas para simular tentativas de fraude.

O volume de dados será dimensionado para permitir testes abrangentes das capacidades de detecção de fraude do pipeline, sem exceder as cotas gratuitas do GCP. Técnicas como compressão, particionamento, otimização de esquema e amostragem estratificada serão aplicadas para maximizar a utilização dos recursos computacionais disponíveis.

Embora os dados sejam fictícios, eles serão modelados para espelhar de perto as características e desafios de dados reais de transações Pix, possibilitando uma demonstração realista da eficácia da solução proposta. Documentação detalhada sobre a geração dos dados e sobre como o sistema poderia escalar para volumes de produção também será fornecida.

## 11. Conclusão

Essa arquitetura de referência representa o estado da arte em construção de pipelines analíticos de ML escaláveis e resilientes para detecção de fraudes em tempo real no domínio financeiro. Através de uma combinação meticulosa de tecnologias de ponta, padrões arquiteturais robustos e boas práticas estabelecidas de Engenharia de Dados e MLOps, ela atende aos rigorosos requisitos de desempenho, confiabilidade e conformidade regulatória, ao mesmo tempo em que permite evolução contínua e extensibilidade para acomodar futuros casos de uso.

Ao passo que incorpora datasets simulados realistas e técnicas sofisticadas de geração de dados, essa proposta oferece uma demonstração completa e convincente das habilidades de Engenharia de ML necessárias para abordar os desafios complexos da detecção de fraudes Pix no mundo real. Da modelagem de dados ao design de arquitetura e implementação, cada aspecto deste projeto fictício foi pensado para espelhar de perto um cenário real e mostrar a expertise necessária para conduzir iniciativas de ML sofisticadas do início ao fim.

Embora seja uma prova de conceito, esta solução não deixa de incorporar as melhores práticas e considerações de um sistema de produção. Cada decisão de design foi tomada com escalabilidade, resiliência, eficiência e segurança em mente.
Da aquisição de dados através de Kafka até o armazenamento no Delta Lake, do processamento de streams com Spark até o serviço de modelos com MLflow e Kubernetes, cada componente foi escolhido e arquitetado para operar com excelência sob as demandas de um ambiente de produção real.

Além disso, a atenção meticulosa dada à geração de conjuntos de dados sintéticos demonstra uma compreensão profunda dos padrões e anomalias presentes em dados reais de transações financeiras. Esse conhecimento de domínio, combinado com as habilidades técnicas demonstradas na engenharia da solução, oferece um testemunho convincente da capacidade de projetar e implementar sistemas de ML de ponta a ponta na indústria.

Em suma, esta proposta de arquitetura, juntamente com o plano detalhado de simulação de dados, não apenas demonstra um conjunto abrangente de competências técnicas, mas também a modernidade, visão estratégica e conhecimento de domínio necessário para iniciativas lideradas de ML sofisticadas e de alto impacto em um ambiente empresarial dinâmico e desafiador como o de serviços financeiros.
Com uma solução tão bem concebida e articulada, não tenho dúvidas de que esse projeto fictício servirá como uma demonstração poderosa das minhas habilidades e expertise, me posicionando como uma forte candidata para funções de liderança em Engenharia de Machine learning.
