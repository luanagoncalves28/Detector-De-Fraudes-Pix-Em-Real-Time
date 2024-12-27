# Testes - Detector de Fraudes Pix
## Visão Geral
Bem-vindo ao coração da qualidade e confiabilidade do meu projeto de detecção de fraudes em transações Pix! Este diretório contém todo o código, configurações e documentação relacionados à minha abordagem abrangente de testes.

Como engenheira de machine learning, eu entendo que testes robustos não são uma reflexão tardia, mas sim uma parte integral do processo de desenvolvimento. Em um sistema de alta responsabilidade como detecção de fraudes em tempo real, deixar bugs escaparem para a produção pode ter consequências severas. É por isso que eu investi pesadamente na criação de uma suíte de testes automatizados que verifica cada componente do meu sistema de forma minuciosa e contínua.

## Minha Filosofia de Testes
Minha abordagem de testes é multifacetada, cobrindo desde as menores unidades de código até a integração completa do sistema. Acredito que testes devem ser:

1. **Abrangentes**: Cada linha de código de produção deve ser exercitada por pelo menos um teste. Testes edge cases, situações de erro e fluxos de dados incomuns. 

2. **Automatizados**: Testes devem ser executados automaticamente como parte do pipeline de CI/CD. Isso garante que regressões sejam capturadas cedo e frequentemente.

3. **Rápidos**: A suíte de testes deve ser executada rapidamente para permitir iterações rápidas e feedback contínuo durante o desenvolvimento.

4. **Confiáveis**: Testes devem ser deterministas e isolados. Falhas de testes devem indicar claramente um problema no código, não inconsistências nos próprios testes.

5. **Legíveis**: Testes servem como documentação viva do sistema. Eles devem ser fáceis de ler e entender, mesmo para alguém novo no projeto.

## O que Eu Testo
Meus testes cobrem todos os aspectos do pipeline de detecção de fraudes:

1. **Funções de Ingestão de Dados**: Testo o processamento de payloads de diferentes formatos, tratamento de erros para dados malformados, e a integração com o Kafka.

2. **Transformações de Dados**: Verifico que as transformações aplicadas no Spark resultam nos schemas esperados e lidam com dados ausentes ou inválidos graciosamente.

3. **Funcionalidades do Modelo**: Testo a lógica do modelo em si, assegurando que ele classifica corretamente transações em cenários conhecidos e lida com entradas inesperadas de forma segura.

4. **Endpoints de API**: Verifico que os endpoints REST que servem o modelo retornam as respostas corretas, tratam erros de input, e atendem aos requisitos de desempenho.

5. **Integração de Componentes**: Executo testes de ponta a ponta que imitam transações Pix reais fluindo através de todo o sistema, validando que todos os componentes trabalham juntos sem problemas.

## Organização do Código de Testes
Organizei meu código de testes em dois subdiretórios principais:
 
- `unidade/`: Contém testes que verificam o comportamento de funções e classes individuais isoladamente. Esses testes são pequenos, rápidos e focados. Exemplos incluem testes para funções de transformação de dados e métodos de modelos.  

- `integracao/`: Contém testes que verificam como múltiplos componentes interagem juntos. Esses testes são maiores, mais lentos e focados em comportamentos de alto nível. Exemplos incluem testes para o pipeline de dados ponto a ponto e para os endpoints da API.

Cada subdiretório contém um arquivo `README.md` que explica os testes em mais detalhes.

## Para Recrutadores e Revisores
Como a engenheira de software responsável por este projeto crítico, eu tomo qualidade de código extremamente a sério. Minha suíte de testes abrangente reflete meu compromisso em entregar software em que se possa confiar.

Ao revisar o código e a documentação de testes neste diretório, sugiro considerar:

1. A estratégia de testes é abrangente, cobrindo uma variedade adequada de cenários normais e de erro em cada nível do sistema?

2. O código de teste é claro, legível e bem estruturado? Ele serve como documentação efetiva do comportamento esperado do sistema?

3. Os testes são devidamente parametrizados e isolados? Eles devem ser determinísticos e não depender de estados globais ou ordenação de execução.

4. Existe um bom equilíbrio entre testes de unidade e integração? Componentes de baixo nível são testados de forma isolada, enquanto comportamentos de alto nível são capturados em testes de integração?

5. Os testes são executados automaticamente como parte do pipeline de CI/CD? Existe uma definição clara de quais testes devem passar antes que mudanças sejam promovidas?

Estou extremamente orgulhosa do trabalho representado por esses testes e adoraria aprofundar as decisões técnicas e de qualidade por trás deles. Como uma engenheira de software com paixão implacável por excelência, estou sempre procurando maneiras de melhorar meus processos de teste e garantia de qualidade.

## Contato
Se você tiver alguma dúvida ou feedback, ou se quiser agendar um bate-papo para mergulhar mais fundo nesta abordagem de teste, não hesite em entrar em contato:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
