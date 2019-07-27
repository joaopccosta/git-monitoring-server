data "local_file" "prometheus-yml" {
    filename = abspath("${path.module}/prometheus/prometheus.yml")
}

data "local_file" "prometheus-dashboard-1" {
    filename = abspath("${path.module}/prometheus/prometheus-dashboard-template1.json")
}