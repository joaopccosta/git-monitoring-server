#!/bin/bash

if [[ $(docker images | grep server) ]]; then
    echo "'server' docker image found on local images. No need to rebuild."
else
    docker build -t server .
fi

#docker network prune -f
cd infrastructure
if [[ $(ls .terraform) ]]; then
    echo ".terraform folder found. No need to run 'terraform init'"
else
    terraform init
fi



terraform apply --auto-approve
#Error: Incorrect attribute value type
#
#  on main.tf line 107, in resource "grafana_dashboard" "metrics1":
# 107:   config_json = data.local_file.prometheus-dashboard-1
# Running terraform apply twice voids this error. It seems that grafana and prometheus need to be running
# before attaching a grafana_dashboard from terraform.

terraform apply --auto-approve
cd ..
