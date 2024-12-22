# Processamento de Dados em Lote com PySpark no Databricks

## Visão Geral

Bem-vindo ao coração do meu pipeline de processamento de dados em lote! Este diretório contém todo o código PySpark e as configurações necessárias para executar jobs de processamento em lote no ambiente Databricks.

Como mencionado no README do diretório pai, o processamento em lote desempenha um papel crucial no meu sistema de detecção de fraudes, permitindo análises aprofundadas de dados históricos, treinamento de modelos e geração de recursos. E o Databricks é a minha plataforma de escolha para executar esses jobs intensivos de dados.

## Por que Databricks?

Escolhi o Databricks como meu ambiente de processamento em lote por várias razões:

1. **Gerenciamento de Cluster Simplificado**: O Databricks abstrai a complexidade do gerenciamento de um cluster Spark, permitindo que eu me concentre na escrita do meu código de processamento em vez de me preocupar com a configuração e manutenção da infraestrutura.

2. **Colaboração e Compartilhamento**: Com notebooks Databricks, posso facilmente colaborar com outros membros da equipe, compartilhar minhas análises e resultados, e criar uma documentação clara dos meus workflows de processamento.

3. **Integração com Serviços de Nuvem**: O Databricks se integra perfeitamente com uma variedade de serviços de nuvem (no meu caso, estou usando o Google Cloud Platform), tornando mais fácil ler e gravar dados de e para fontes externas.

4. **Desempenho e Otimização**: O Databricks adiciona várias otimizações sobre o Spark "vanilla", incluindo um otimizador de consulta, indexação automática e um formato de armazenamento colunar (Delta Lake) para melhorar o desempenho dos meus jobs.

## Meus Jobs PySpark

Eu tenho dois scripts PySpark principais neste diretório:

1. **processamento.py**: Este script contém a lógica principal do meu workflow de processamento em lote. Ele lê dados brutos de transações Pix, realiza uma série de transformações e análises, e gera recursos para meus modelos de detecção de fraude. As principais etapas incluem:

   - Filtragem de transações por período de tempo relevante
   - Junção com dados de referência (por exemplo, informações do cliente)
   - Agregações para criar recursos no nível do cliente (por exemplo, contagens de transações, valores médios)
   - Codificação de variáveis categóricas
   - Escrita dos recursos gerados no Delta Lake para consumo posterior

2. **processamento_config.yaml**: Este arquivo contém todas as configurações para o meu job de processamento, incluindo:

   - Caminhos para dados de entrada e saída
   - Parâmetros para as várias etapas de transformação
   - Configurações do Spark (por exemplo, número de partições, tamanho do executor)

   Manter essas configurações separadas do código principal torna mais fácil ajustar e reutilizar o job para diferentes períodos de tempo ou conjuntos de dados.

## Fluxo de Trabalho do Databricks

Meu fluxo de trabalho típico no Databricks envolve os seguintes passos:

1. **Desenvolvimento do Notebook**: Começo explorando os dados e prototipando minha lógica de processamento em um notebook interativo do Databricks. Isto me permite iterar rapidamente, visualizar os resultados e depurar quaisquer problemas.

2. **Refatoração em Script Python**: Uma vez que tenha acertado a lógica no notebook, refatoro-o em um script Python independente (`processamento.py`). Isto torna mais fácil reutilizar o código e integrá-lo com outras partes do meu pipeline.

3. **Configuração do Job**: Crio um arquivo de configuração (`processamento_config.yaml`) para especificar todos os parâmetros e caminhos de entrada/saída para o meu job. Isto me permite facilmente reutilizar o mesmo script para diferentes execuções.

4. **Agendamento e Execução**: Uso a interface de Jobs do Databricks para agendar a execução regular do meu script de processamento (por exemplo, diariamente ou semanalmente). O Databricks cuida de provisionar um cluster, executar o código e desligar os recursos quando o job é finalizado.

5. **Monitoramento e Depuração**: Monitoro o progresso e o desempenho do meu job usando os dashboards do Databricks. Se ocorrerem erros, uso os logs e mensagens de erro para depurar e refinar o meu código.

## Para Recrutadores e Revisores de Código

Como engenheira de machine learning trabalhando independentemente neste projeto, tive que tomar muitas decisões de design e arquitetura sozinha. Ao revisar este código, convido você a considerar:

1. **Estrutura e Clareza do Código**: O código está organizado de uma forma lógica e fácil de seguir? Ele segue as melhores práticas e convenções do PySpark? A intenção por trás de cada etapa de transformação é clara?

2. **Desempenho e Otimização**: O código faz bom uso das capacidades de processamento distribuído do Spark? Existem oportunidades para melhorar o desempenho através de uma melhor partição, cache ou técnicas de otimização de PySpark?

3. **Robustez e Tratamento de Erros**: Como o código lida com dados malformados ou ausentes? Existem verificações de erro adequadas e mecanismos de tratamento em vigor?

4. **Qualidade da Configuração**: A separação do código principal e das configurações do job é feita de maneira eficaz? As configurações são abrangentes e fáceis de entender?

5. **Potencial de Reutilização**: O código é modular e pode ser facilmente adaptado para outros casos de uso de processamento em lote? Há potencial para abstrai-lo em uma biblioteca PySpark reutilizável?

Estou extremamente orgulhosa do sistema robusto e eficiente que construí, e adoraria aprofundar as decisões técnicas por trás dele. Seu feedback e insights seriam imensamente valiosos para me ajudar a crescer como engenheira de dados.

## Contato

Se você tiver alguma dúvida ou quiser agendar uma conversa mais aprofundada, sinta-se à vontade para entrar em contato:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
