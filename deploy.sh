#!/bin/bash
set -e

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
cd ..
