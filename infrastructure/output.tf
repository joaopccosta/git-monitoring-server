output "grafana_address" {
  value = "${docker_container.grafana.*.ip_address}"
}
output "grafana_port" {
  value = "${docker_container.grafana.*.ports}"
}

output "prometheus_address" {
  value = "${docker_container.prometheus.*.ip_address}"
}

output "prometheus_port" {
  value = "${docker_container.prometheus.*.ports}"
}

output "webserver_address" {
  value = "${docker_container.webserver.*.ip_address}"
}

output "webserver_port" {
  value = "${docker_container.webserver.*.ports}"
}