# DetectorDeFraudesPixEmTempoReal


## 📝 Descrição

Sistema de detecção de fraudes em tempo real para transações PIX utilizando Machine Learning e processamento distribuído.


## 🎯 Objetivo

Criar uma solução robusta e escalável que utilize técnicas avançadas de Engenharia de Dados e Machine Learning para identificar e prevenir atividades fraudulentas, garantindo a segurança e a integridade do sistema Pix.



## 🏗️ Arquitetura do Sistema

O pipeline é construído utilizando tecnologias de ponta:

1. Databricks: Ambiente unificado de processamento e análise
2. Apache Spark: Processamento distribuído de dados
3. Delta Lake: Armazenamento confiável de dados
4. MLflow: Gerenciamento do ciclo de vida ML
5. Prometheus & Grafana: Monitoramento e visualização


📚 Para mais detalhes, consulte a documentação de arquitetura



## 🚀 Configuração do Ambiente

1. Pré-requisitos:
- Databricks
- Conta ativa (Azure Databricks, AWS ou Community Edition)
- Apache Kafka
- Cluster externo configurado
- Opções: auto-hospedado, Confluent Cloud ou Amazon MSK
- Docker
- Instalação local para Prometheus e Grafana


## 💻 Executando o Pipeline
Configuração Inicial

` #Clone o repositório`
` git clone https://github.com/seu-usuario/DetectorDeFraudesPixEmTempoReal
cd DetectorDeFraudesPixEmTempoReal`

` #Inicie os serviços de monitoramento`
`docker-compose up -d`


## Execução dos Notebooks
1. Ingestão: (ingestao/notebook_ingestao.py)
2. Processamento: (processamento/notebook_processamento.py)
3. Machine Learning: (machine_learning/notebook_modelo.py)


## 📁 Estrutura do Repositório

DetectorDeFraudesPixEmTempoReal/

├── docs/ # Documentação completa

├── ingestao/ # Pipeline de ingestão Kafka

├── processamento/ # Processamento Spark

├── machine_learning/ # Modelos e MLflow

├── monitoramento/ # Configs Prometheus/Grafana

└── testes/ # Testes unitários/integração



## 🤝 Contribuindo
Fork o projeto
Crie sua Feature Branch (git checkout -b feature/AmazingFeature)
Commit suas mudanças (git commit -m 'Add: nova funcionalidade')
Push para a Branch (git push origin feature/AmazingFeature)
Abra um Pull Request



##📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.



## 📧 Contato

Luana Gonçalves - (lugonc.lga@gmail.com)

Link do Projeto: (https://github.com/seu-usuario/DetectorDeFraudesPixEmTempoReal)

⭐️ Se este projeto te ajudou, considere dar uma estrela!

Gostaria que eu explicasse ou detalhasse alguma parte do markdown?
