# Skynet Ops Audit Service

A minimal cloud-ready audit event service built with **Python FastAPI**, containerized with **Docker**, and infrastructure defined using **Terraform**.

## Features
- Health check endpoint
- Event ingestion API
- Event retrieval API
- Containerized deployment
- Infrastructure as Code

## API Endpoints

GET /health  
Returns service health status.

POST /events  
Stores an audit event.

GET /events  
Returns stored events.

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
