output "cluster_endpoint" {
  description = "O endpoint do cluster GKE"
  value       = google_container_cluster.primary.endpoint
}

output "cluster_ca_certificate" {
  description = "O certificado CA raiz do cluster GKE"
  value       = base64decode(google_container_cluster.primary.master_auth.0.cluster_ca_certificate)
}

output "vpc_network_id" {
  description = "O ID da rede VPC criada"
  value       = google_compute_network.vpc.id
}

output "subnet_id" {
  description = "O ID da sub-rede criada"
  value       = google_compute_subnetwork.private.id
}
