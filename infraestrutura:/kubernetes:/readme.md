# Kubernetes - Orquestração de Contêineres para Detecção de Fraudes Pix

## Visão Geral

Neste diretório, implementei as configurações Kubernetes necessárias para orquestrar os microserviços do sistema de detecção de fraudes Pix. O Kubernetes atua como a camada crítica de orquestração, garantindo a alta disponibilidade, escalabilidade e resiliência necessárias para processar até 1 milhão de transações por segundo, conforme exigido pelos requisitos do projeto.

## Arquitetura dos Microserviços

Desenvolvi uma arquitetura de microserviços distribuída onde cada componente é responsável por uma função específica do pipeline de detecção de fraudes:

### 1. Ingestão de Dados
```yaml
# Exemplo de configuração do serviço de ingestão
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kafka-ingestor
  labels:
    app: fraud-detection
    component: ingestor
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fraud-detection
  template:
    spec:
      containers:
      - name: kafka-consumer
        image: fraud-detection/kafka-consumer:latest
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "1000m"
```

### 2. Processamento em Tempo Real
```yaml
# Configuração do serviço de análise em tempo real
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: fraud-analyzer
spec:
  serviceName: "fraud-analyzer"
  replicas: 5
  template:
    spec:
      containers:
      - name: spark-processor
        image: fraud-detection/spark-processor:latest
        env:
        - name: SPARK_MASTER_URL
          valueFrom:
            configMapKeyRef:
              name: spark-config
              key: master-url
```

## Organização do Diretório

```
kubernetes/
├── namespaces/           # Definições de isolamento lógico
│   ├── production.yaml   # Ambiente de produção
│   └── staging.yaml      # Ambiente de homologação
├── deployments/          # Configurações de aplicações
│   ├── ingestor.yaml     # Serviço de ingestão
│   ├── processor.yaml    # Processamento em tempo real
│   └── api.yaml          # API de serviços
└── services/            # Definições de conectividade
    ├── internal.yaml    # Serviços internos
    └── external.yaml    # Endpoints externos
```

## Implementações de Segurança

Implementei várias camadas de segurança seguindo as exigências da Resolução BCB n° 403/2024:

### 1. Network Policies
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: restrict-internal-traffic
spec:
  podSelector:
    matchLabels:
      app: fraud-detection
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: fraud-detection
    ports:
    - protocol: TCP
      port: 8080
```

### 2. Pod Security Policies
```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
    - ALL
  volumes:
    - 'configMap'
    - 'emptyDir'
    - 'secret'
  runAsUser:
    rule: 'MustRunAsNonRoot'
```

## Gerenciamento de Recursos

Implementei configurações cuidadosas de recursos para garantir performance e custo-benefício:

### 1. Autoscaling Horizontal
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: fraud-detector-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: fraud-detector
  minReplicas: 3
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

## Para Recrutadores e Revisores de Código

Ao avaliar as configurações Kubernetes deste projeto, sugiro focar nos seguintes aspectos:

### 1. Arquitetura e Design
- Separação clara de responsabilidades entre serviços
- Configurações de recursos otimizadas
- Estratégias de deployment e rollback
- Gerenciamento de estado e persistência

### 2. Segurança e Compliance
- Implementação de Network Policies
- Configurações de Pod Security
- Gerenciamento de segredos
- Isolamento de namespaces

### 3. Performance e Escalabilidade
- Configurações de auto-scaling
- Alocação de recursos
- Estratégias de resiliência
- Balanceamento de carga

### 4. Observabilidade
- Configuração de health checks
- Estratégias de logging
- Métricas de performance
- Traces distribuídos

### 5. Manutenibilidade
- Organização dos manifestos
- Padrões de nomenclatura
- Documentação inline
- Modularização das configurações

## Destaques Técnicos

1. **Alta Disponibilidade**
   - Replicação de serviços críticos
   - Distribuição geográfica
   - Recuperação automática de falhas

2. **Segurança em Camadas**
   - Network Policies restritivas
   - Pod Security Policies
   - Service Accounts com menor privilégio

3. **Performance Otimizada**
   - Resource limits adequados
   - Auto-scaling baseado em métricas
   - Afinidade de pod para latência

## Contato

Para discussões técnicas sobre as configurações Kubernetes:
- Email: lugonc.lga@gmail.com
- LinkedIn: [Meu Perfil](https://www.linkedin.com/in/luanagoncalves05/)
