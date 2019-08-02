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
  upload {
    content = replace(data.local_file.prometheus-yml.content, "server-ip", docker_container.webserver.ip_address)
    file = "/etc/prometheus/prometheus.yml"
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

provider "grafana" {
  url = "http://${docker_container.grafana.ip_address}:${var.grafanaport}"
  auth = "admin:admin"
}

resource "grafana_data_source" "prometheus" {
  type = "prometheus"
  name = "prometheus-source"
  url = "http://${docker_container.prometheus.ip_address}:${var.prometheusport}/"
  depends_on = [docker_container.grafana, docker_container.prometheus]
}

resource "grafana_dashboard" "metrics1" {
  config_json = data.local_file.prometheus-dashboard-1.content
  depends_on = [grafana_data_source.prometheus]
}