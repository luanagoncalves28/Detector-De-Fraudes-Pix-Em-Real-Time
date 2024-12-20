# DetectorDeFraudesPixEmTempoReal

Este repositório contém um projeto completo de pipeline de Machine Learning desenvolvido para detectar fraudes em tempo real nas transações do Pix, o sistema de pagamentos instantâneos do Banco Central do Brasil. O objetivo é criar uma solução robusta e escalável que utilize técnicas avançadas de Engenharia de Dados e Machine Learning para identificar e prevenir atividades fraudulentas, garantindo a segurança e a integridade do sistema Pix.

## Arquitetura do Sistema

O pipeline é construído na plataforma Databricks, aproveitando o Apache Spark para processamento distribuído e o Apache Kafka para absorção de dados em tempo real. Os componentes principais incluem:

- Databricks para um ambiente unificado de processamento e análise de dados
- Apache Spark para processamento distribuído de dados
- Delta Lake para armazenamento confiável de dados
- MLflow para gerenciamento do ciclo de vida do modelo de machine learning
- Prometheus e Grafana para monitoramento e visualização

Para mais detalhes, consulte a documentação de arquitetura em docs/arquitetura.md.

## Configuração do Ambiente

Para configurar o ambiente de desenvolvimento, você precisa:

1. Uma conta no Databricks (Azure Databricks, Databricks on AWS, ou Databricks Community Edition)
2. Um cluster Kafka externo (auto-hospedado ou um serviço gerenciado como Confluent Cloud ou Amazon MSK)
3. Docker para executar Prometheus e Grafana localmente

As dependências do Python serão gerenciadas dentro do seu ambiente Databricks. Para instruções sobre como configurar cada componente, consulte a documentação em docs/.

## Executando o Pipeline

O pipeline pode ser executado no Databricks para processamento de dados em grande escala.

1. Crie um cluster Databricks e anexe este repositório a ele.
2. Inicie os serviços Prometheus e Grafana usando Docker Compose:
```bash
docker-compose up -d
```
3. Execute o notebook de ingestão de dados `ingestao/notebook_ingestao.py` para começar a inserir dados do seu cluster Kafka.
4. Execute o notebook de processamento `processamento/notebook_processamento.py` para processar os dados usando Spark.
5. Treine e implante o modelo de machine learning executando o notebook `machine_learning/notebook_modelo.py`.

Para mais detalhes sobre implantação e monitoramento, consulte a documentação em docs/uso_operacional.md.

## Estrutura do Repositório

* `docs/`: Documentação do projeto, incluindo arquitetura, padrões de projeto e guias operacionais.
* `ingestao/`: Notebook e configurações para ingestão de dados usando Kafka.
* `processamento/`: Notebook para processamento de dados usando Spark e Delta Lake.
* `machine_learning/`: Notebook para treinamento e implantação de modelos usando MLflow.
* `monitoramento/`: Configurações para monitoramento usando Prometheus e Grafana.
* `testes/`: Testes unitários e de integração.

## Contribuindo

Contribuições são bem-vindas! Por favor, abra uma questão para discutir mudanças importantes antes de submeter uma solicitação pull. Certifique-se de atualizar os testes em conformidade com a proteção.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo `LICENSE` para detalhes.

## Contato

Em caso de qualquer questão ou preocupação, por favor abra uma edição neste repositório ou entre em contato com o mantenedor do projeto em lugonc.lga@gmail.com.
