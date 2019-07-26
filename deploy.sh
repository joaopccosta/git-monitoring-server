#!/bin/bash
set -e

docker build -t server .

cd infrastructure
terraform init
terraform apply --auto-approve
cd ..
