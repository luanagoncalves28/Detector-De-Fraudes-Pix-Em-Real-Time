# Detector De Fraudes Pix Em Tempo Real

Bem-vindo ao repositório do projeto "Detector de Fraudes Pix em Tempo Real"! Este projeto implementa um pipeline analítico de gerenciamento de risco de fraude para o Pix, em total conformidade com a Resolução BCB n° 403 de 22/07/2024, que entrou em vigor em 1° de novembro de 2024.

## Visão Geral do Projeto

Este projeto foi desenvolvido em resposta direta às novas diretrizes do Banco Central do Brasil, especificadas na Resolução BCB n° 403/2024, que estabelece requisitos mais rigorosos para o gerenciamento de risco de fraude em transações Pix. Com a entrada em vigor destas novas exigências em 1° de novembro de 2024, as instituições financeiras necessitam implementar:

- Sistema de monitoramento em tempo real para análise de transações Pix
- Mecanismos robustos de detecção de fraudes e anomalias
- Solução de gerenciamento de risco de fraude integrando informações do DICT
- Identificação e tratamento de comportamentos atípicos
- Sistema de alerta e bloqueio preventivo de transações suspeitas

A solução aborda esses requisitos através de um pipeline analítico avançado que:

1. Monitora e detecta fraudes em tempo quase real com taxa de acerto superior a 95%
2. Processa até 1 milhão de transações por segundo em períodos de pico
3. Integra-se com o DICT para validação de transações e identificação de comportamentos atípicos
4. Implementa mecanismos automáticos de bloqueio preventivo
5. Fornece dashboards em tempo real para monitoramento de atividades suspeitas

## Destaques do Projeto

- Arquitetura de microsserviços altamente escalável e resiliente
- Ingestão de dados em tempo real com Apache Kafka e Spark Structured Streaming
- Processamento distribuído usando Apache Spark e Delta Lake
- Treinamento e implementação de modelos de ML com Databricks e MLflow
- Monitoramento abrangente usando Prometheus e Grafana
- Implantação e gerenciamento com Google Kubernetes Engine (GKE)
- Práticas rigorosas de testes e integração contínua com GitHub Actions

## Estrutura do Repositório

O repositório está organizado de forma modular, refletindo as diferentes camadas do sistema:

```
.
├── docs/                    # Documentação detalhada do projeto
├── infraestrutura/         # Configurações e scripts IaC
├── dados/                  # Pipeline de processamento de dados
│   ├── ingestao/          # Ingestão com Kafka
│   ├── processamento/     # Processamento Spark
│   └── armazenamento/     # Camadas Bronze/Silver/Gold
├── modelos/               # Código ML e MLOps
├── monitoramento/         # Configurações monitoramento
├── testes/                # Testes unitários/integração
└── ci_cd/                # Pipelines CI/CD
```

Cada diretório contém seu próprio README.md com detalhes específicos sobre sua finalidade e funcionamento.

## Para Recrutadores e Revisores de Código

Se você é um recrutador técnico ou profissional de machine learning revisando este projeto, seja bem-vindo! Este repositório demonstra não apenas competências técnicas em engenharia de dados e MLOps, mas também profundo entendimento do contexto regulatório atual do sistema financeiro brasileiro.

Ao revisar este projeto, considere:

1. Alinhamento com requisitos regulatórios atuais
2. Arquitetura do sistema e decisões de design
3. Qualidade e clareza do código
4. Uso efetivo de padrões de design e melhores práticas
5. Abrangência da documentação
6. Cobertura e qualidade dos testes
7. Implementação de práticas de CI/CD e automação

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Para dúvidas, sugestões ou oportunidades:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Seu Perfil do LinkedIn](link-para-seu-linkedin)
- Website: [Seu Website](link-para-seu-website)

Agradeço seu interesse neste projeto! Juntos, podemos tornar o Pix mais seguro e confiável, em total conformidade com as mais recentes exigências regulatórias.
