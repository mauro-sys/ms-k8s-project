# Mini Kubernetes Project
 
This is a small project I'm building to practice Kubernetes.
 
It's a simple two-part app:
- A backend (Flask) that returns some data as JSON
- A frontend (a basic webpage served by nginx) that calls the backend
I'm deploying both to a local Kubernetes cluster (minikube), using things like
Deployments, Services, ConfigMaps, Secrets, and Ingress.
 
## Status
 
Just started — building this step by step.
 
## Folders
 
- `backend/` — the Flask app
- `frontend/` — the webpage + nginx config
- `kubernetes/` — the YAML files that deploy everything to Kubernetes
## Why I'm building this
 
I've been learning Kubernetes from scratch and wanted a real, working project.
 
