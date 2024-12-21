# Infraestrutura como Código - Detector de Fraudes Pix

Bem-vindo à documentação da infraestrutura do projeto "Detector de Fraudes Pix em Tempo Real". Este diretório contém todos os recursos que desenvolvi para provisionar e gerenciar a infraestrutura do sistema de forma automatizada e segura, garantindo total conformidade com os requisitos da Resolução BCB n° 403/2024.

## Visão Geral da Infraestrutura

Projetei esta infraestrutura para atender aos rigorosos requisitos de segurança, escalabilidade e resiliência estabelecidos pelo Banco Central do Brasil. Optei por uma abordagem de infraestrutura como código (IaC) com Terraform e configurações Kubernetes, garantindo um provisionamento consistente e reprodutível em todos os ambientes.

### Componentes Principais

1. **Google Kubernetes Engine (GKE)**
   - Cluster gerenciado para orquestração de contêineres
   - Configuração de auto-scaling para lidar com picos de transações
   - Network policies para isolamento de tráfego
   - Segregação de workloads por namespaces

2. **Redes e Segurança**
   - VPC dedicada com subnets segregadas por ambiente
   - Firewall rules para controle granular de tráfego
   - Cloud IAM para gerenciamento de identidade e acesso
   - Cloud KMS para gerenciamento de chaves criptográficas

3. **Armazenamento e Dados**
   - Cloud Storage para armazenamento de dados não estruturados
   - Managed Disks para volumes persistentes
   - Sistema de backup automatizado

4. **Monitoramento e Observabilidade**
   - Stack Prometheus/Grafana para métricas
   - Cloud Logging para centralização de logs
   - Cloud Monitoring para alertas e dashboards

## Estrutura do Diretório

```
infraestrutura/
├── terraform/              # Código IaC para provisionamento
│   ├── main.tf            # Configurações principais
│   ├── variables.tf       # Variáveis do projeto
│   └── outputs.tf         # Outputs do provisionamento
├── kubernetes/            # Manifestos Kubernetes
│   ├── namespaces/       # Definições de namespaces
│   ├── deployments/      # Configurações de deployments
│   └── services/         # Definições de serviços
└── gke/                  # Configurações específicas do GKE
    ├── cluster.yaml      # Configuração do cluster
    └── policies/         # Políticas de segurança
```

## Para Recrutadores e Revisores de Código

Se você é um recrutador técnico, engenheiro sênior ou especialista em machine learning revisando este projeto, esta seção destaca os principais aspectos da infraestrutura para avaliação:

### 1. Arquitetura e Design
- Implementação de arquitetura em camadas com clara separação de responsabilidades
- Uso de microserviços para garantir escalabilidade e manutenibilidade
- Design robusto de redes e segurança alinhado com requisitos regulatórios

### 2. Conformidade Regulatória
- Implementação completa dos requisitos da Resolução BCB n° 403/2024
- Controles de segurança em múltiplas camadas
- Tratamento adequado de dados sensíveis

### 3. Infraestrutura como Código
- Código Terraform limpo e modular
- Uso de variáveis e módulos para reusabilidade
- Documentação clara das configurações
- Práticas de segurança em IaC

### 4. Kubernetes e Containerização
- Configurações otimizadas de cluster
- Políticas de segurança bem definidas
- Estratégias eficientes de deployment
- Configuração adequada de recursos

### 5. Monitoramento e Observabilidade
- Métricas abrangentes de sistema
- Dashboards informativos
- Sistema robusto de logging
- Alertas bem configurados

### 6. Segurança
- Implementação do princípio do menor privilégio
- Segregação adequada de ambientes
- Gestão segura de segredos
- Proteção de endpoints e comunicações

## Contato

Para discussões técnicas sobre a infraestrutura:
- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](../LICENSE) para detalhes.
