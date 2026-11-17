# Task Management API

A lightweight REST API built with Python for managing tasks. The project demonstrates application development, containerization with Docker, Kubernetes deployment, and GitOps automation with Argo CD.

## Features

- Simple HTTP API for task management
- Health check endpoint
- Configurable port via environment variable
- Docker image built and published to GHCR with GitHub Actions
- Kubernetes deployment with two replicas, probes, resource limits and security settings
- Configuration via ConfigMaps and sensitive values via Secrets
- Automated sync and self-healing with Argo CD

## API Endpoints

| Method | Endpoint   | Description                       |
|--------|------------|-----------------------------------|
| GET    | `/`        | Returns information about the API |
| GET    | `/healthz` | Checks application health         |
| GET    | `/tasks`   | Returns the list of tasks         |

Example:

```bash
curl http://localhost:8080/
curl http://localhost:8080/healthz
curl http://localhost:8080/tasks
```

## Requirements

- Python 3
- Bash
- Docker (optional, for containerization)
- kubectl and a Kubernetes cluster (optional, for deployment)
- Argo CD (optional, for GitOps deployment)

## Quick Start

```bash
git clone https://github.com/mazhenovnurzhan1606-code/Task-Management-API.git
cd Task-Management-API
./scripts/run.sh
```

The API is now available at `http://localhost:8080`.

## Configuration

| Variable | Default | Description                     |
|----------|---------|---------------------------------|
| `PORT`   | `8080`  | Port the application listens on |

The application binds to `0.0.0.0`.

```bash
PORT=9000 ./scripts/run.sh
```

## Running Tests

```bash
./scripts/test.sh
```

The script runs 3 tests and prints `TESTS: 3/3` on success.

## Project Structure

```text
Task-Management-API/
├── src/
│   └── server.py          # Application code
├── tests/
│   └── test_server.py     # Tests
├── scripts/
│   ├── run.sh             # Start the service
│   └── test.sh            # Run the tests
├── k8s/
│   ├── configmap.yaml
│   ├── deployment.yaml
│   └── service.yaml
├── argocd/
│   └── application.yaml   # Argo CD Application
├── .gitignore
└── README.md
```

## Docker

Images are published to GitHub Container Registry:

```text
ghcr.io/mazhenovnurzhan1606-code/task-management-api
```

GitHub Actions builds and publishes an image on every push. Images are tagged with the full Git commit SHA for version tracking and reproducible deployments.

```bash
docker run --rm -p 8080:8080 \
  ghcr.io/mazhenovnurzhan1606-code/task-management-api:YOUR_COMMIT_SHA
```

## Kubernetes

Manifests live in `k8s/` and include:

- Deployment with two replicas
- Service for in-cluster access
- ConfigMap for application configuration
- Secret for sensitive environment variables
- Readiness and liveness probes
- CPU and memory requests and limits
- Container security settings

## GitOps with Argo CD

The Argo CD Application is defined in `argocd/application.yaml`. Argo CD watches the `main` branch and syncs manifests from `k8s/`:

- **Automated Sync** applies changes from Git.
- **Prune** removes resources no longer defined in Git.
- **Self-Heal** restores the desired state after manual changes in the cluster.

Git is the source of truth for the Kubernetes configuration.

## CI/CD

| Stage | Tool           | Responsibility                                      |
|-------|----------------|-----------------------------------------------------|
| CI    | GitHub Actions | Build the image and publish it to GHCR              |
| CD    | Argo CD        | Watch Git, sync manifests, heal configuration drift |

Building and deploying are independent processes.

## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s` folder.
To roll back, undo the commit that deployed the bad version, with a new commit:

    git log --oneline -- k8s/deployment.yaml
    git revert COMMIT_SHA
    git push

Argo CD deploys the previous version within three minutes. Do not use
`kubectl rollout undo`: self-heal would put the bad version back.

## Repository

[Task Management API on GitHub](https://github.com/mazhenovnurzhan1606-code/Task-Management-API)