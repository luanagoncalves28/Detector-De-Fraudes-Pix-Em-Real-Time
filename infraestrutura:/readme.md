# Infraestrutura como Código - Detector de Fraudes Pix

## Contextualização

Este diretório contém a infraestrutura completa que desenvolvi para suportar o sistema de detecção de fraudes em transações Pix. Em um sistema que precisa processar até 1 milhão de transações por segundo e detectar fraudes em tempo quase real, a infraestrutura é um componente crítico que determina o sucesso do projeto. Aqui você encontrará todo o código de infraestrutura como código (IaC) e configurações necessárias para garantir a conformidade com a Resolução BCB n° 403/2024.

## Importância da Infraestrutura no Projeto

A infraestrutura deste projeto foi projetada para atender três requisitos críticos:

1. **Alta Performance**: O sistema precisa analisar transações Pix em tempo quase real, exigindo uma infraestrutura que garanta baixa latência e alto throughput.

2. **Escalabilidade**: Com volumes de transações variando significativamente ao longo do dia, a infraestrutura deve escalar automaticamente para manter a performance sem desperdiçar recursos.

3. **Segurança**: Como parte do sistema financeiro, a infraestrutura implementa múltiplas camadas de segurança para proteger dados sensíveis e prevenir acessos não autorizados.

## Decisões Técnicas e Arquiteturais

### 1. Google Kubernetes Engine (GKE)
Escolhi o GKE como plataforma principal por três razões fundamentais:
- Orquestração robusta de contêineres com auto-scaling granular
- Integração nativa com serviços de segurança do Google Cloud
- Facilidade de implementar políticas de isolamento e segurança

Configurações implementadas:
```yaml
# Exemplo de configuração de auto-scaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: fraud-detection-hpa
spec:
  minReplicas: 3
  maxReplicas: 100
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### 2. Redes e Segurança
Arquitetei a infraestrutura de rede seguindo o princípio de defesa em profundidade:

- VPC dedicada com subnets segregadas:
  - Subnet para serviços públicos (APIs)
  - Subnet privada para processamento
  - Subnet isolada para dados sensíveis

- Implementação de segurança em camadas:
  ```hcl
  # Exemplo de configuração Terraform para segurança em camadas
  resource "google_compute_firewall" "internal" {
    name    = "internal-traffic"
    network = google_compute_network.vpc.name
    
    allow {
      protocol = "tcp"
      ports    = ["8080", "9090"]
    }
    
    source_ranges = ["10.0.0.0/8"]
    target_tags   = ["internal"]
  }
  ```

### 3. Sistema de Monitoramento
Implementei uma stack de monitoramento completa para garantir visibilidade total do sistema:

- Prometheus: Coleta de métricas em tempo real
- Grafana: Dashboards customizados para diferentes perfis
- AlertManager: Sistema de alertas inteligentes

## Estrutura do Diretório

```
infraestrutura/
├── terraform/              # IaC para provisionamento
│   ├── main.tf            # Configurações principais
│   ├── variables.tf       # Variáveis do projeto
│   └── outputs.tf         # Outputs do provisionamento
├── kubernetes/            # Configurações Kubernetes
│   ├── namespaces/       # Definição de ambientes
│   ├── deployments/      # Configurações de apps
│   └── services/         # Definições de serviços
└── gke/                  # Configs específicas GKE
    ├── cluster.yaml      # Configuração do cluster
    └── policies/         # Políticas de segurança
```

## Para Recrutadores e Revisores de Código

Esta seção foi estruturada para facilitar a avaliação técnica do projeto, destacando aspectos específicos que demonstram minhas habilidades em infraestrutura, segurança e conformidade regulatória.

### 1. Estrutura e Organização do Código
Ao revisar a estrutura, observe:

- Separação clara entre camadas de infraestrutura
- Modularização do código Terraform
- Organização hierárquica dos manifestos Kubernetes
- Consistência nas convenções de nomenclatura

Exemplo de boa modularização:
```hcl
# terraform/modules/networking/main.tf
module "vpc" {
  source = "./modules/networking"
  
  project_id    = var.project_id
  network_name  = "fraud-detection-vpc"
  subnet_config = local.subnet_configuration
}
```

### 2. Segurança e Conformidade
Pontos críticos para avaliação:

- Implementação de controles de acesso RBAC
- Configurações de network policies
- Gestão de segredos com Google KMS
- Logs de auditoria e compliance

### 3. Performance e Escalabilidade
Aspectos a serem avaliados:

- Configurações de auto-scaling
- Otimização de recursos
- Estratégias de cache e performance
- Gerenciamento de carga

### 4. Monitoramento e Observabilidade
Verifique a implementação de:

- Métricas de negócio customizadas
- Dashboards operacionais
- Sistema de alertas
- Rastreamento de transações

### 5. Infrastructure as Code
Analise a qualidade do código IaC:

- Uso de variáveis e locals
- Modularização efetiva
- Tratamento de estados
- Gestão de dependências

## Contato

Para discussões técnicas sobre a infraestrutura:
- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](../LICENSE) para detalhes.
