# Definir o provedor Google Cloud
provider "google" {
  project = var.project_id
  region  = var.region
}

# Criar um cluster GKE
resource "google_container_cluster" "primary" {
  name     = "fraud-detection-cluster"
  location = var.region
  
  # Configuração para alta disponibilidade
  node_config {
    machine_type = "n1-standard-4"
    oauth_scopes = [
      "https://www.googleapis.com/auth/compute",
      "https://www.googleapis.com/auth/devstorage.read_only",
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }
  initial_node_count = 3
  enable_autopilot   = false

  release_channel {
    channel = "REGULAR"
  }
  
  # Configurações de segurança
  private_cluster_config {
    enable_private_nodes    = true
    enable_private_endpoint = false
    master_ipv4_cidr_block  = "172.16.0.0/28"
  }

  # Políticas de segurança do pod
  pod_security_policy_config {
    enabled = true
  }
}

# Criar uma VPC para o cluster
resource "google_compute_network" "vpc" {
  name                    = "fraud-detection-vpc"
  auto_create_subnetworks = false
}

# Criar uma sub-rede privada para o cluster 
resource "google_compute_subnetwork" "private" {
  name          = "private-subnet"
  ip_cidr_range = "10.0.0.0/20" 
  network       = google_compute_network.vpc.id

  # Habilita logs de fluxo para auditoria
  log_config {
    aggregation_interval = "INTERVAL_5_SEC"
    flow_sampling        = 0.5
    metadata             = "INCLUDE_ALL_METADATA"
  }
}

# Configurar autoscaling para o cluster
resource "google_container_node_pool" "primary_nodes" {
  name       = "fraud-detection-node-pool"
  cluster    = google_container_cluster.primary.id
  node_count = 1

  autoscaling {
    min_node_count = 1
    max_node_count = 5
  }
}
