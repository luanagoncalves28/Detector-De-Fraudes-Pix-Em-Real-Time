resource "google_compute_network" "vpc_network" {
  name                    = var.network_name
  auto_create_subnetworks = false
  project                 = var.project_id
}

resource "google_compute_subnetwork" "vpc_subnetwork" {
  count         = length(var.subnets)
  name          = var.subnets[count.index].subnet_name
  ip_cidr_range = var.subnets[count.index].subnet_ip
  region        = var.subnets[count.index].subnet_region
  network       = google_compute_network.vpc_network.id
  project       = var.project_id
}

resource "google_compute_firewall" "allow_internal" {
  name    = "allow-internal"
  network = google_compute_network.vpc_network.name
  project = var.project_id

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["0-65535"]
  }

  allow {
    protocol = "udp"
    ports    = ["0-65535"]
  }

  source_ranges = [for subnet in var.subnets : subnet.subnet_ip]
}
