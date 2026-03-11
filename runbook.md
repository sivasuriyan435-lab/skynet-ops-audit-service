# Operations Runbook

## Service Down
1. Check if the container is running:
   docker ps

2. Restart the container if necessary.

## High Latency
Check system resources and application logs.

## Deployment Issues
Rebuild the Docker image:

docker build -t skynet-ops .

## Cost Spike
Check running cloud resources and log retention settings.

