# Google Kubernetes Engine (GKE) - Configurações e Deployments
## Visão Geral
Este diretório contém as configurações e manifestos Kubernetes específicos para implantação do sistema de detecção de fraudes Pix no Google Kubernetes Engine (GKE). O GKE é a plataforma gerenciada de orquestração de contêineres do Google Cloud Platform, proporcionando uma maneira eficiente e escalável de implantar e gerenciar aplicativos em contêineres.
## Por que GKE?
A escolha do GKE como plataforma de orquestração de contêineres foi baseada em várias considerações críticas:
1. **Escalabilidade Automática**: O GKE oferece recursos robustos de auto-scaling, permitindo que os pods sejam escalados automaticamente com base na carga de trabalho, garantindo performance ótima e uso eficiente de recursos.
2. **Gerenciamento Simplificado**: Com o GKE, muitos aspectos da gestão do cluster Kubernetes, como atualizações, patches de segurança e monitoramento, são tratados pela plataforma, reduzindo a sobrecarga operacional.
3. **Integração Nativa com GCP**: Sendo parte do ecossistema Google Cloud, o GKE se integra perfeitamente com outros serviços GCP, como Cloud Storage, Cloud Logging, e Cloud Monitoring, simplificando a arquitetura geral.
4. **Segurança Robusta**: O GKE fornece múltiplas camadas de segurança, incluindo isolamento de nós, upgrade e reparo automáticos, e integração com o GCP IAM para controle de acesso granular.
## Organização do Diretório
O diretório `gke/` contém dois arquivos principais:
### deployment.yaml
Este arquivo define os deployments Kubernetes para os vários componentes do sistema de detecção de fraudes:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fraud-detection-engine
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fraud-detection-engine
  template:
    metadata:
      labels:
        app: fraud-detection-engine
    spec:
      containers:
      - name: fraud-detection-engine
        image: gcr.io/projeto/fraud-detection-engine:v1
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
```
### service.yaml
Este arquivo define os serviços Kubernetes que expõem os deployments:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: fraud-detection-engine
spec:
  selector: 
    app: fraud-detection-engine
  type: ClusterIP
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```
## Decisões Técnicas Importantes
### 1. Estratégia de Deployment
Utilizamos a estratégia RollingUpdate para atualizações de deployment:
```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
```
Isso garante atualizações sem downtime, criando novos pods antes de terminar os antigos.
### 2. Probes de Saúde
Implementamos liveness e readiness probes para todos os deployments críticos:
```yaml
spec:
  containers:
  - name: fraud-detection-engine
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 30
      periodSeconds: 10
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 10
      periodSeconds: 5
```
Isso permite que o Kubernetes detecte e substitua pods não responsivos, melhorando a resiliência geral do sistema.
## Para Recrutadores e Revisores de Código 
Ao revisar as configurações do GKE, sugiro focar nos seguintes aspectos:
### 1. Uso Eficiente de Recursos
- Definição adequada de requests e limits para CPU e memória
- Utilização de HorizontalPodAutoscaler para escalonamento automático
- Configuração de Pod Disruption Budgets para disponibilidade durante atualizações
### 2. Configurações de Segurança
- Contexto de segurança e permissões para os pods
- Utilização de secrets para dados sensíveis
- Habilitação de NetworkPolicies para controle do tráfego entre os pods
### 3. Probes de Saúde e Resiliência  
- Uso adequado de liveness e readiness probes
- Configurações de recursos para garantir disponibilidade (ex: multiple replicas, PodAntiAffinity)
- Estratégias de deployment para atualizações sem downtime
### 4. Exposição de Serviços
- Escolha apropriada de tipos de serviço (ClusterIP, NodePort, LoadBalancer)
- Uso de Ingress para expor serviços HTTP(S)
- Anotações de serviço para integração com balanceadores de carga do GCP
### 5. Melhores Práticas de Configuração
- Uso de labels e seletores para organização e descoberta de serviços
- Namespaces para isolar recursos
- Configuração de limites de recursos e quotas
Espero que esta visão geral e pontos de revisão demonstrem tanto meu conhecimento técnico do GKE quanto minha capacidade de projetar e documentar configurações robustas e seguras. Estou ansioso para discutir essas escolhas e arquiteturas em mais detalhes.
## Contato
Para qualquer dúvida ou discussão adicional sobre as configurações do GKE:
- Email: lugonc.lga@gmail.com
- LinkedIn: [(https://www.linkedin.com/in/luanagoncalves05/)]
