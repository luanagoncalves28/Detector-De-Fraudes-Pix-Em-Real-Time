# Pipeline de Dados - Detector de Fraudes Pix

## Visão Geral
Este diretório contém todo o pipeline de processamento de dados que desenvolvi para o sistema de detecção de fraudes em tempo real para transações Pix. O pipeline foi projetado para lidar com o imenso volume e velocidade de dados gerados pelas transações Pix, garantindo que as análises de fraude possam ser realizadas com a menor latência possível.

## Menu de Navegação
- [Ingestão de Dados](ingestao/README.md)
  - [Ingestão com Kafka](ingestao/kafka/README.md)
  - [Ingestão com Spark](ingestao/spark/README.md)
- [Processamento de Dados](processamento/README.md)  
  - [Processamento com PySpark e Databricks](processamento/pyspark/databricks/README.md)
  - [Processamento com Spark Structured Streaming](processamento/spark/structured_streaming/README.md)
- [Armazenamento de Dados](armazenamento/README.md)
  - [Camada Bronze](armazenamento/bronze/README.md)
  - [Camada Silver](armazenamento/silver/README.md)
  - [Camada Gold](armazenamento/gold/README.md)

## Importância do Pipeline de Dados
Em um sistema de detecção de fraudes em tempo real, a eficiência e robustez do pipeline de dados são absolutamente críticas. Cada segundo de latência pode significar a diferença entre bloquear uma transação fraudulenta ou permitir que ela ocorra. Portanto, cada componente deste pipeline foi cuidadosamente arquitetado para garantir:

1. **Ingestão de Dados em Tempo Real**: Capturar dados de transações Pix imediatamente à medida que ocorrem.

2. **Processamento Escalável**: Manipular picos de volume de transações sem degradação de performance. 

3. **Armazenamento Eficiente**: Armazenar dados de forma otimizada para análise rápida.

4. **Integração Perfeita**: Transmitir dados processados ​​diretamente para os modelos de detecção de fraude.

## Decisões Técnicas e Arquiteturais
### 1. Apache Kafka para Ingestão de Dados
Escolhi o Apache Kafka como a espinha dorsal para a ingestão de dados em tempo real devido a:

- Capacidade de lidar com altas taxas de transferência de dados com baixa latência
- Arquitetura distribuída e tolerante a falhas 
- Integração perfeita com o ecossistema de processamento de streaming

### 2. Apache Spark para Processamento 
O Apache Spark, especificamente com Structured Streaming, foi escolhido para o processamento de dados devido a:

- Capacidade de processar streams de dados em tempo real
- Integração nativa com o Kafka
- APIs de alto nível que permitem expressar transformações complexas de streaming

### 3. Delta Lake para Armazenamento
Para armazenar dados processados, estou usando o Delta Lake devido a:

- Transações ACID para consistência de dados
- Manipulação eficiente de grandes volumes de dados
- Integração perfeita com o Spark para acesso rápido aos dados

## Para Recrutadores e Revisores de Código
Ao revisar este pipeline de dados, convido você a considerar:

### 1. Escolha Apropriada de Tecnologias
- As tecnologias selecionadas são adequadas para os requisitos de performance e escalabilidade?
- As tecnologias se integram bem para criar um pipeline coeso?

### 2. Qualidade e Organização do Código
- O código é limpo, legível e bem documentado?
- As preocupações estão adequadamente separadas?
- As melhores práticas foram seguidas?

### 3. Tratamento de Erros e Resiliência
- O pipeline lida graciosamente com picos de dados e falhas parciais?  
- Existem mecanismos adequados para tratamento de erros e reinicializações?

### 4. Eficiência e Performance  
- O pipeline é otimizado para latência e taxa de transferência?
- Os recursos computacionais são usados ​​de forma eficiente?

### 5. Flexibilidade e Extensibilidade
- O pipeline pode acomodar facilmente novos tipos e fontes de dados?  
- Os componentes são fracamente acoplados e podem ser modificados independentemente?

Estou ansiosa para discutir essas e outras considerações em mais detalhes. O design e a implementação deste pipeline foram um esforço significativo, e acredito que ele demonstra não apenas minhas habilidades técnicas, mas também minha capacidade de arquitetar sistemas robustos e eficientes para lidar com desafios do mundo real.

## Contato
Se você tiver alguma dúvida ou quiser discutir este pipeline de dados em mais detalhes, sinta-se à vontade para entrar em contato:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/) 

Estou sempre feliz em aprofundar os detalhes técnicos e o raciocínio por trás da minha abordagem. Obrigado pelo seu tempo e consideração!
