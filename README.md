# Detector de Fraudes em Tempo Real para Transações Pix

Bem-vindo ao meu projeto de detecção de fraudes em tempo real para o Pix, o sistema de pagamentos instantâneos do Banco Central do Brasil. Como engenheira de machine learning, desenvolvi este projeto para demonstrar minhas habilidades em construir pipelines de ML robustos, escaláveis e em conformidade com as melhores práticas de MLOps e DevOps.

## Visão Geral do Projeto

Este projeto implementa um sistema de ponta a ponta para detectar transações fraudulentas do Pix em tempo real. Ele combina técnicas avançadas de engenharia de dados e machine learning para analisar grandes volumes de dados de transações, identificar padrões suspeitos e sinalizar potenciais fraudes em questão de segundos.

## Destaques do Projeto

- Arquitetura de microserviços altamente escalável e resiliente
- Ingestão de dados em tempo real usando Apache Kafka e Spark Structured Streaming
- Processamento de dados distribuído com Apache Spark e Delta Lake
- Treinamento e implantação de modelos de ML usando Databricks e MLflow
- Monitoramento abrangente da infraestrutura, do pipeline e do modelo com Prometheus e Grafana
- Implantação e gerenciamento de contêineres com Google Kubernetes Engine (GKE)
- Práticas de CI/CD implementadas usando GitHub Actions

## Por que esta arquitetura?

A arquitetura deste projeto foi cuidadosamente projetada para lidar com os desafios únicos da detecção de fraudes em tempo real em um sistema de pagamentos de alto volume como o Pix. Alguns dos principais fatores que influenciaram minhas escolhas de arquitetura incluem:

- Escalabilidade: A capacidade de lidar com grandes picos de tráfego e escalar horizontalmente conforme necessário.
- Resiliência: Garantir que o sistema permaneça operacional e preserve a integridade dos dados mesmo em caso de falhas de componentes.
- Latência: Minimizar o tempo entre uma transação ocorrer e uma potencial fraude ser detectada e sinalizada.
- Manutenibilidade: Facilitar a depuração, o teste e a implantação de atualizações no sistema.

Escolhi tecnologias como Kafka, Spark e Kubernetes especificamente por sua capacidade comprovada de lidar com esses requisitos em sistemas de produção de grande escala.

## Navegando pelo Repositório

- `docs/`: Documentação detalhada sobre a arquitetura, os padrões de projeto e os ciclos de vida de MLOps e DevOps.
- `infraestrutura/`: Configurações de infraestrutura como código (IaC) usando Terraform e Kubernetes.
- `dados/`: Scripts e notebooks para ingestão, processamento e armazenamento de dados.
- `modelos/`: Notebooks e scripts para treinamento, avaliação e implantação de modelos de ML.
- `monitoramento/`: Configurações para monitoramento da infraestrutura, do pipeline e do modelo usando Prometheus e Grafana.
- `testes/`: Testes unitários e de integração para os componentes do sistema.
- `ci_cd/`: Configurações e workflows para integração contínua e implantação contínua (CI/CD) usando GitHub Actions.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo `LICENSE` para detalhes.

## Entre em Contato

Se você tiver alguma dúvida sobre este projeto ou quiser discutir oportunidades de trabalhar juntos, sinta-se à vontade para me contatar em lugonc.lga@gmail.com.

Estou sempre feliz em conversar sobre engenharia de machine learning, MLOps e como podemos usar dados para criar sistemas mais inteligentes e confiáveis. Espero que este projeto tenha lhe dado uma boa visão das minhas habilidades e paixão nesta área!

## Para Recrutadores Técnicos

Se você é um recrutador técnico ou um profissional de engenharia de machine learning revisando este projeto, sinta-se à vontade para explorar o código diretamente aqui no GitHub. Este repositório foi estruturado para facilitar a navegação e o entendimento da arquitetura do projeto, da qualidade do código, das convenções de nomenclatura e da documentação.

Algumas áreas de interesse particular podem incluir:

- A estrutura geral do projeto e a organização dos diretórios
- A qualidade e a clareza do código em si
- O uso de padrões de design e melhores práticas
- A abrangência e a qualidade da documentação
- A implementação de testes unitários e de integração

Espero que ao revisar este código, você possa ter um vislumbre das minhas habilidades e conhecimentos como Engenheira de Machine Learning. Se você tiver alguma dúvida ou quiser discutir qualquer aspecto do projeto em mais detalhes, não hesite em me contatar.

Além de revisar o código, também convido você a assistir aos vídeos que documentam o processo de desenvolvimento deste projeto. Estes vídeos estarão disponíveis no meu site de portfólio, no meu artigo no Medium e nas minhas postagens no LinkedIn. Eles fornecerão insights adicionais sobre meu processo de pensamento, minhas habilidades de resolução de problemas e minha abordagem geral para engenharia de machine learning.

Obrigada por dedicar seu tempo para revisar este projeto. Espero ter a oportunidade de discutir mais detalhadamente como minhas habilidades e experiência podem ser benéficas para sua equipe.
