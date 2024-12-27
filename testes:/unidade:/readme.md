# Testes de Unidade - Detector de Fraudes Pix
## Visão Geral
Bem-vindo ao núcleo da minha abordagem de testes para o projeto Detector de Fraudes Pix! Este subdiretório contém todos os testes de unidade que desenvolvi para garantir que cada componente individual do meu sistema funcione perfeitamente de forma isolada.

Como engenheira de software, acredito firmemente que testes de unidade são a base de qualquer suite de testes robusta. Ao testar minuciosamente as menores unidades de código, posso ter confiança de que cada bloco de construção do meu sistema é sólido e se comporta como esperado. Isso não apenas torna mais fácil identificar e corrigir bugs, mas também facilita a manutenção e expansão do sistema ao longo do tempo.

## O que é um Teste de Unidade?
Um teste de unidade é um pedaço de código que invoca uma unidade de trabalho no sistema (como um método, função, ou classe), e então verifica se a saída dessa unidade é conforme o esperado. O objetivo é validar que cada unidade de software performa como projetado, independente de outras partes do sistema.  

Testes de unidade geralmente têm as seguintes características:

1. **Isolados**: Testes de unidade não devem depender ou interagir com código externo à unidade sendo testada. Isso é frequentemente alcançado através do uso de mocks, stubs, e outras técnicas de teste.

2. **Rápidos**: Testes de unidade devem executar muito rapidamente, geralmente em questão de milissegundos. Isso permite que sejam executados frequentemente sem desacelerar o processo de desenvolvimento.

3. **Repetíveis**: Testes de unidade devem ser determinísticos - ou seja, dado o mesmo input, eles sempre produzem o mesmo resultado. Isso garante que falhas nos testes indiquem de forma confiável problemas no código.

4. **Auto-verificáveis**: Testes de unidade devem ser capazes de detectar automaticamente se passaram ou falharam sem necessidade de inspeção manual.

## O que Estou Testando
Meus testes de unidade cobrem todas as peças críticas do meu pipeline de detecção de fraudes, incluindo:

1. **Funções de Ingestão de Dados**: Testo a lógica para processar diferentes formatos de payload, parsear campos chave, e manipular erros. Exemplos incluem testes para funções que consomem do Kafka.

2. **Transformações de Dados**: Verifico que minhas funções PySpark e SQL geram os schemas e agregações corretas. Testo cenários com dados ausentes ou mal formatados para garantir manipulação graciosa de erros.

3. **Lógica do Modelo**: Testo os métodos centrais dos meus modelos de detecção de fraude, assegurando que eles classificam transações corretamente e geram scores de confiança razoáveis. Também testo como os modelos lidam com entradas inesperadas ou mal formadas.

4. **Funções Auxiliares**: Qualquer função auxiliar usada em todo o pipeline, como formatadores de data, geradores de ID, ou validadores de schema, também é minuciosamente testada.

## Como Escrevo Testes de Unidade
Uso o framework de testes `pytest` para escrever e executar meus testes de unidade em Python. Pytest oferece uma sintaxe simples e expressiva para estruturar testes e fazer asserções.

Um teste de unidade típico no meu sistema se parece com isso:

```python
def test_transform_transaction_data():
    # Definir dados de teste
    raw_data = {
        'transaction_id': 't1234',
        'amount': '100.00',
        'timestamp': '2022-01-01T10:00:00'
    }
    
    # Chamar a função sendo testada
    transformed_data = transform_transaction_data(raw_data)
    
    # Verificar que a saída é conforme o esperado  
    assert transformed_data == {
        'transaction_id': 't1234', 
        'amount': 100.0,
        'timestamp': datetime(2022, 1, 1, 10, 0, 0)
    }
```

Neste exemplo, estou testando uma função `transform_transaction_data` que é responsável por converter dados de transação brutos (como strings) em tipos apropriados para análise posterior. 

O teste segue um padrão comum:

1. Primeiro, defino alguns dados de entrada de teste que imitam o formato dos dados brutos.

2. Em seguida, chamo a função `transform_transaction_data` com esses dados de teste.

3. Finalmente, uso uma asserção para verificar que a saída transformada corresponde ao que eu esperava. Se a asserção falhar, o teste falha, indicando um potencial bug na função.

Sigo este mesmo padrão básico para todos os meus testes de unidade, adaptando os dados de entrada e as verificações conforme necessário para cada unidade de código sendo testada.

## Executando os Testes
Todos os testes de unidade podem ser executados utilizando o comando `pytest` na raiz do diretório de testes. Isso executará todos os testes de unidade e reportará quaisquer falhas.

Também configurei os testes de unidade para serem executados automaticamente como parte do meu pipeline de CI/CD. Sempre que mudanças de código são feitas, todos os testes de unidade são executados, e falhas de teste bloqueiam o deploy das mudanças. Isso ajuda a pegar regressões cedo e assegurar que problemas não cheguem à produção.  

## Para Recrutadores e Revisores
Como a engenheira de software por trás deste crítico sistema de detecção de fraudes, investi uma quantidade significativa de tempo e esforço na criação de testes de unidade abrangentes. Acredito que eles demonstram meu compromisso com a entrega de código de alta qualidade e manutenível.

Ao revisar os testes de unidade neste diretório, sugiro considerar o seguinte:

1. Os testes cobrem adequadamente os principais caminhos e casos extremos para cada unidade?

2. Os testes são legíveis e claramente documentam o comportamento esperado de cada unidade?

3. Os testes seguem as melhores práticas, como ser isolado, rápido e determinístico?

4. Os testes capturam efetivamente possíveis erros e manipulam cenários imprevistos?

5. Há uma alta taxa de cobertura de testes? A maioria, se não todas as unidades que podem ser testadas, possuem testes correspondentes?

Estou extremamente orgulhosa da suite de testes de unidade que desenvolvi e adoraria mergulhar mais profundamente nas decisões técnicas por trás dela. Acredito que ela demonstra não apenas minhas habilidades técnicas, mas também meu compromisso em criar software que seja robusto, confiável e fácil de evoluir ao longo do tempo.

## Contato 
Se você tiver alguma dúvida ou feedback, ou se quiser agendar uma conversa para mergulhar mais profundamente nessa abordagem de testes de unidade, não hesite em entrar em contato:

- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
