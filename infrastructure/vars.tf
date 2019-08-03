variable "dockerhost_address" {
  default = "unix:///var/run/docker.sock"
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