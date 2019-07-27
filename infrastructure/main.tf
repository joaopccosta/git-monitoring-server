variable "dockerhost_address" {
    default = "127.0.0.1"
}

variable "dockerhost_port" {
    default = 2375
}
variable "serverport" {
    default = 5000
}

variable "prometheusport" {
    default = 9090
}

variable "grafanaport" {
    default = 3000
}

provider "docker" {
    host = "tcp://${var.dockerhost_address}:${var.dockerhost_port}"
}

resource "docker_container" "prometheus" {
    image = docker_image.prometheus.latest
    name = "prometheus-server"
    ports {
        internal = var.prometheusport
        external = var.prometheusport
  }

}

resource "docker_container" "grafana" {
  image = docker_image.grafana.latest
  name = "grafana"
  ports {
    internal = var.grafanaport
    external = var.grafanaport
  }

}

resource "docker_container" "webserver" {
  image = docker_image.server.latest
  name = "server"
  ports {
    internal = var.serverport
    external = var.serverport
  }
}

//resource "docker_network" "private_network" {
//  name = "private_subnet"
//}

resource "docker_image" "prometheus" {
  name = "prom/prometheus:latest"
}

resource "docker_image" "grafana" {
  name = "grafana/grafana:latest"
}

resource "docker_image" "server" {
  name = "server:latest"
  keep_locally = true
}


output "grafana_address" {
  value = "${docker_container.grafana.*.ip_address}"
}


output "prometheus_address" {
  value = "${docker_container.prometheus.*.ip_address}"
}

output "webserver_address" {
  value = "${docker_container.webserver.*.ip_address}"
}

provider "grafana" {
  url  = "http://${docker_container.grafana.ip_address}:${var.grafanaport}"
  auth = "admin:admin"
}

resource "grafana_data_source" "prometheus" {
  type          = "prometheus"
  name          = "prometheus-source"
  url           = "http://${docker_container.prometheus.ip_address}:${var.prometheusport}/"
}

resource "grafana_dashboard" "metrics" {
  config_json = "${file("./prometheus-dashboard.json")}"
}