# **Documentação de Formatos e Estrutura de Dados no Projeto de Detecção de Fraudes no Pix**  

## **1. Introdução**  

Este projeto foi desenvolvido com o **máximo de realismo possível**, simulando **um cenário bancário real** para a **detecção de fraudes no Pix**, especificamente fraudes baseadas em **engenharia social**.  

Embora este seja um projeto **fictício**, os **formatos de dados utilizados** foram escolhidos **com base em como os bancos e instituições financeiras realmente tratam, processam e armazenam esses dados**. Isso garante que **o projeto tenha aplicabilidade prática**, tornando-o **mais próximo de um ambiente de produção real**.  

📌 **Objetivo desta documentação:**  
✅ Explicar quais **formatos de dados** são utilizados no projeto.  
✅ Justificar a escolha de cada formato com base **nas práticas reais do setor bancário**.  
✅ Detalhar como os dados são estruturados e **como cada formato se encaixa no fluxo de processamento**.  

---

## **2. Visão Geral dos Formatos de Dados Utilizados**  

Para garantir uma simulação realista, o projeto utiliza **múltiplos formatos de dados**, pois no mundo real **os bancos não trabalham apenas com JSON ou CSV**, mas sim com uma **variedade de formatos adequados a cada necessidade**.  

| **Tipo de Dado** | **Formato Utilizado** | **Motivo da Escolha** |
|------------------|------------------|--------------------|
| **Transações Pix** | **CSV, JSON** | CSV é usado para **grandes volumes de dados**, JSON para **integrações e APIs** |
| **Dados Comportamentais** | **JSON, XML** | JSON facilita **machine learning**, XML é padrão para **troca de informações bancárias** |
| **Dados Contextuais** | **JSON, XML** | JSON suporta **IA Generativa**, XML é usado para **auditoria regulatória** |
| **Dados de Contas Destinatárias** | **EDI, JSON** | EDI é padrão para **transações interbancárias**, JSON permite **análises avançadas** |

Abaixo, explico cada formato em mais detalhes e como ele está sendo aplicado no projeto.  

---

## **3. Explicação dos Formatos e Justificativa Técnica**  

### **3.1. CSV (Comma-Separated Values) - Registros de Transações Pix**
📌 **Onde está sendo usado?**  
- Utilizado para armazenar **grandes volumes de transações Pix**.  
- Simula como os bancos processam **arquivos de transações em lote**.  

📌 **Por que CSV?**  
✅ **Formatado para eficiência** → CSV é **leve e rápido**, ótimo para bancos processarem milhões de transações.  
✅ **Fácil manipulação** → Pode ser facilmente lido por **sistemas bancários, SQL e planilhas**.  

📜 **Exemplo de transação Pix em CSV:**  
```
id_transacao,valor,horario,chave_pix_destinatario,tipo_chave,banco_origem,banco_destino,canal_origem,status_transacao
TX123456789,8000.00,2025-01-15T22:45:00,emailfraudulento@xyz.com,Email,Banco X,Banco Y,App,Aprovada
```

---

### **3.2. JSON (JavaScript Object Notation) - Dados Estruturados e APIs**
📌 **Onde está sendo usado?**  
- Para **dados comportamentais do usuário**, que são **mais complexos e aninhados**.  
- Para **integração com modelos de machine learning e IA Generativa**.  
- Para **dados de contexto da transação**, como mensagens e chats analisados pela IA.  

📌 **Por que JSON?**  
✅ **Flexibilidade** → Permite armazenar **dados aninhados e complexos**.  
✅ **APIs e Machine Learning** → Suporte direto para **APIs e análise de dados**.  

📜 **Exemplo de JSON para análise de engenharia social:**  
```json
{
  "usuario_id": "123456",
  "historico_transacoes": [
    {"valor": 50.00, "destinatario": "contato_amigo@xyz.com"},
    {"valor": 100.00, "destinatario": "parente@xyz.com"}
  ],
  "localizacao": "São Paulo",
  "dispositivo_usado": "iPhone 12",
  "ip": "192.168.1.1",
  "mensagem_transacao": "urgente paga esse dinheiro por favor",
  "chat_usuario": "ele disse que vai fazer algo ruim se eu não pagar"
}
```

---

### **3.3. XML (Extensible Markup Language) - Troca de Dados Bancários**
📌 **Onde está sendo usado?**  
- Para **dados comportamentais do usuário** quando há necessidade de **integração bancária**.  
- Para **comunicação entre sistemas regulatórios**.  

📌 **Por que XML?**  
✅ **Padrão de interoperabilidade bancária** → Bancos trocam dados via XML para garantir **consistência**.  
✅ **Ideal para auditorias** → Estrutura organizada, **permite verificação regulatória**.  

📜 **Exemplo de XML para comportamento do usuário:**  
```xml
<usuario>
    <usuario_id>123456</usuario_id>
    <localizacao>São Paulo</localizacao>
    <dispositivo_usado>iPhone 12</dispositivo_usado>
    <ip>192.168.1.1</ip>
    <mensagem_transacao>urgente paga esse dinheiro por favor</mensagem_transacao>
</usuario>
```

---

### **3.4. EDI (Electronic Data Interchange) - Dados de Contas Destinatárias**
📌 **Onde está sendo usado?**  
- Para **dados de recebedores suspeitos** e **troca de informações entre bancos**.  

📌 **Por que EDI?**  
✅ **Formato bancário oficial** → Padrão para **transações interbancárias e compliance**.  
✅ **Segurança e compatibilidade** → Usado para garantir **comunicação confiável entre instituições**.  

📜 **Exemplo de EDI para análise de conta suspeita:**  
```
ISA*00* *00* *ZZ*SENDER BANK *ZZ*RECEIVER BANK *230115*2200*U*00401*000000001*0*T*>
GS*RA*SENDER BANK*RECEIVER BANK*20250115*2200*1*X*004010
ST*820*0001
BPR*I*8000.00*C*ACH*CTX*01*987654321*DA*123456789*XYZ BANK
N1*PR*EMAILFRAUDULENTO@XYZ.COM
REF*TX*TX123456789
SE*5*0001
GE*1*1
IEA*1*000000001
```

---

## **4. Conclusão**
📢 **Este projeto não apenas usa dados fictícios, mas faz isso de forma estruturada e alinhada ao mercado financeiro real**.  

🚀 **Principais diferenciais desta abordagem:**  
✔️ **Simulação realista dos formatos usados por bancos e reguladores**.  
✔️ **Facilidade de integração com sistemas de compliance e auditoria**.  
✔️ **Preparação para futura implementação em ambientes produtivos**.  

📌 **Com esta abordagem, o projeto está pronto para demonstrar seu valor real e facilitar a transição para um cenário de produção!** 🚀  
