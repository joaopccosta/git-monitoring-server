output "grafana_address" {
  value = "${docker_container.grafana.*.ip_address}"
}

output "prometheus_address" {
  value = "${docker_container.prometheus.*.ip_address}"
}

output "webserver_address" {
  value = "${docker_container.webserver.*.ip_address}"
}