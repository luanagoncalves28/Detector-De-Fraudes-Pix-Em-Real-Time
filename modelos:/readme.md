# Modelos de Machine Learning para Detecção de Fraudes Pix

## Visão Geral

Bem-vindo ao coração do meu projeto de detecção de fraudes Pix - os modelos de machine learning que eu desenvolvi! Este diretório contém todo o código, notebooks e artefatos relacionados ao meu trabalho no desenvolvimento, treinamento, avaliação e implantação dos modelos de detecção de fraude.

Como engenheira de machine learning, meu objetivo é criar modelos altamente precisos, eficientes e escaláveis que podem identificar transações Pix fraudulentas em tempo real. Isso envolve não apenas o design e treinamento dos modelos em si, mas também a criação de um pipeline completo de MLOps para gerenciar o ciclo de vida desses modelos.

## Minha Abordagem de MLOps 

MLOps (Machine Learning Operations) é um conjunto de práticas que visa unificar o desenvolvimento de modelos de machine learning (ML) e a operação de modelos de ML em produção. Eu implementei uma abordagem abrangente de MLOps para este projeto, que inclui:

1. **Versionamento de Dados e Modelos**: Eu rastreio e versiono todos os conjuntos de dados e versões de modelos usando o DVC (Data Version Control) e o MLflow. Isso garante total reprodutibilidade e facilita a depuração e o rollback se necessário.

2. **Pipeline Automatizado de ML**: Eu automatizei completamente nosso treinamento de modelos e processo de avaliação usando o Apache Airflow. Os jobs são disparados com base em agendamentos ou por eventos (por exemplo, chegada de novos dados).

3. **Monitoramento e Logging de Modelos**: Eu registro e rastreio todas as métricas relevantes (precisão, recall, F1-score etc.) para cada execução de modelo usando o MLflow. Além disso, eu continuamente monitoro a performance do modelo em produção para detecção de drift e degradação.

4. **CI/CD para Modelos**: Eu integrei os modelos ao nosso pipeline de CI/CD, permitindo teste, validação e implantação rápidos e automatizados de novas versões de modelos.

5. **Infraestrutura como Código**: Eu gerencio toda a infraestrutura necessária para treinamento, hospedagem e implantação de modelos através de código usando ferramentas como Terraform e Docker. Isso garante consistência e reduz erros humanos.

## Meu Fluxo de Trabalho do Modelo

Meu fluxo de trabalho de desenvolvimento de modelo consiste em várias etapas:

1. **Exploração e Preparação de Dados**: Eu exploro e preparo os dados brutos das camadas de armazenamento Bronze e Silver para treinamento do modelo. Isso inclui limpeza de dados, engenharia de recursos e transformações. Eu realizo essas operações usando notebooks interativos no Databricks.

2. **Treinamento do Modelo**: Eu treino os modelos usando o Spark MLlib no Databricks. Eu uso técnicas como cross-validation e hyperparameter tuning para otimizar a performance do modelo. Eu rastreio e registro todas as execuções de treinamento usando o MLflow.

3. **Avaliação do Modelo**: Eu avalio os modelos treinados em um conjunto de dados de retenção usando várias métricas. Eu uso visualizações como matrices de confusão e curvas ROC para entender a performance do modelo. Somente modelos que atingem meus limiares de performance são considerados para produção.

4. **Implantação do Modelo**: Eu empacoto os modelos selecionados usando o MLflow e os implanto em um ambiente de produção usando o Docker. Eu também configuro monitoramento e alerta da performance do modelo.

## Para Recrutadores e Revisores

Como a engenheira de machine learning liderando o desenvolvimento de modelos para este projeto de detecção de fraude Pix, estou extremamente orgulhosa da abordagem robusta, orientada a MLOps que projetei e implementei.

Ao revisar o código e os artefatos neste diretório, eu sugiro considerar o seguinte:

1. A abordagem de MLOps é abrangente e segue as melhores práticas da indústria?
2. O código para treinamento, avaliação e implantação de modelos está bem estruturado, modular e segue princípios de engenharia de software?
3. Os experimentos de modelo são devidamente rastreados, versionados e reproduzíveis?
4. Os pipelines de treinamento e implantação do modelo são robustos, eficientes e escaláveis?
5. As considerações de monitoramento e manutenção do modelo são levadas em conta?

## Contato

Se você tiver alguma dúvida ou feedback, ou se quiser agendar uma conversa para mergulhar mais fundo nesta arquitetura de aprendizado de máquina, não hesite em entrar em contato:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
