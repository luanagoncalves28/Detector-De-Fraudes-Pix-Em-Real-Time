variable "project_id" {
  description = "O ID do projeto GCP"
  type        = string
}

variable "region" {
  description = "A região GCP para implantar os recursos"
  type        = string
  default     = "us-central1" 
}

variable "zone" {
  description = "A zona GCP para implantar os recursos"
  type        = string
  default     = "us-central1-a"
}

variable "cluster_name" {
  description = "O nome do cluster GKE"
  type        = string
  default     = "fraud-detection-cluster"
}

variable "machine_type" {
  description = "O tipo de máquina para os nós do cluster"
  type        = string
  default     = "n1-standard-4"
}

variable "min_node_count" {
  description = "O número mínimo de nós no cluster"
  type        = number
  default     = 1
}

variable "max_node_count" {
  description = "O número máximo de nós no cluster"
  type        = number
  default     = 5
}
