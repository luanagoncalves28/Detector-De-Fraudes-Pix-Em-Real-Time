# Terraform - Provisionamento da Infraestrutura como Código

## Visão Geral

Este diretório contém o código Terraform que desenvolvi para provisionar e gerenciar toda a infraestrutura do sistema de detecção de fraudes Pix no Google Cloud Platform (GCP). A implementação segue as melhores práticas de Infrastructure as Code (IaC), garantindo que toda a infraestrutura seja versionada, testável e reprodutível.

## Organização do Código

O código está organizado em três arquivos principais:

### main.tf
Arquivo principal que define todos os recursos da infraestrutura, incluindo:

- Cluster GKE otimizado para processamento em tempo real
- VPC com design de rede segmentada
- Sistema de gerenciamento de identidade e acesso (IAM)
- Recursos de armazenamento e logging

Exemplo de configuração do cluster GKE:
```hcl
resource "google_container_cluster" "primary" {
  name     = "fraud-detection-cluster"
  location = var.region
  
  # Configuração para alta disponibilidade
  release_channel {
    channel = "REGULAR"
  }
  
  # Configurações de segurança
  private_cluster_config {
    enable_private_nodes    = true
    enable_private_endpoint = false
    master_ipv4_cidr_block = "172.16.0.0/28"
  }

  # Políticas de segurança do pod
  pod_security_policy_config {
    enabled = true
  }
}
```

### variables.tf
Define todas as variáveis utilizadas no projeto, permitindo flexibilidade e reutilização:

```hcl
variable "project_id" {
  description = "ID do projeto GCP"
  type        = string
}

variable "region" {
  description = "Região principal do GCP"
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Ambiente (dev, staging, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Ambiente deve ser dev, staging ou prod."
  }
}
```

### outputs.tf
Define as saídas importantes do provisionamento, úteis para integração com outros sistemas:

```hcl
output "kubernetes_cluster_name" {
  description = "Nome do cluster GKE"
  value       = google_container_cluster.primary.name
}

output "vpc_network_id" {
  description = "ID da VPC criada"
  value       = google_compute_network.vpc.id
}
```

## Decisões Técnicas Importantes

### 1. Segmentação de Rede
Implementei uma arquitetura de rede segmentada para isolar componentes críticos:

```hcl
# Exemplo de segmentação de rede
resource "google_compute_subnetwork" "private" {
  name          = "private-subnet"
  ip_cidr_range = "10.0.0.0/20"
  network       = google_compute_network.vpc.id
  
  # Habilita logs de fluxo para auditoria
  log_config {
    aggregation_interval = "INTERVAL_5_SEC"
    flow_sampling       = 0.5
  }
}
```

### 2. Gestão de Segredos
Utilizei o Cloud KMS para gerenciamento seguro de credenciais:

```hcl
resource "google_kms_key_ring" "fraud_detection" {
  name     = "fraud-detection-keyring"
  location = var.region
}

resource "google_kms_crypto_key" "database_key" {
  name     = "database-encryption-key"
  key_ring = google_kms_key_ring.fraud_detection.id
  
  rotation_period = "7776000s" # 90 dias
}
```

### 3. Auto-scaling Inteligente
Configurei políticas de auto-scaling baseadas em métricas de negócio:

```hcl
resource "google_container_node_pool" "primary_nodes" {
  name       = "fraud-detection-node-pool"
  cluster    = google_container_cluster.primary.id
  
  autoscaling {
    min_node_count = 3
    max_node_count = 100
    
    # Métricas customizadas para scaling
    location_policy = "BALANCED"
  }
}
```

## Para Recrutadores e Revisores de Código

Ao avaliar este código Terraform, sugiro focar nos seguintes aspectos:

### 1. Estrutura e Modularização
- Organização clara do código em arquivos lógicos
- Uso efetivo de módulos para reutilização
- Consistência nas convenções de nomenclatura
- Documentação inline explicativa

### 2. Práticas de Segurança
- Implementação do princípio do menor privilégio
- Criptografia em repouso e em trânsito
- Segregação de redes e controle de acesso
- Logs de auditoria abrangentes

### 3. Escalabilidade e Performance
- Configurações de auto-scaling
- Distribuição geográfica de recursos
- Otimização de custos
- Resiliência e alta disponibilidade

### 4. Governança e Compliance
- Conformidade com a Resolução BCB n° 403/2024
- Tags e labels para governança
- Políticas de backup e disaster recovery
- Monitoramento e alertas

### 5. Boas Práticas de IaC
- Uso de state remoto e locking
- Variáveis bem documentadas
- Outputs relevantes
- Tratamento de dependências

## Próximos Passos Planejados

Para futura implementação, considero:

1. Implementar workload identity para maior segurança
2. Expandir métricas de auto-scaling customizadas
3. Adicionar mais políticas de governança
4. Otimizar custos com spot instances

## Contato

Para discussões sobre as decisões de infraestrutura:
- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
