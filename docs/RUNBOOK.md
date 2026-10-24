# Local runbook

This runbook covers only the local execution and CI procedures currently supported. This repository has no validated production deployment, backup, or recovery procedure.

## Prerequisites

- Python 3.11 or newer;
- Docker with Docker Compose;
- Git;
- PostgreSQL does not need to be installed locally because it runs through Compose.

CI uses Python 3.12 and PostgreSQL 16.

## Prepare the environment

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
cp .env.example .env
```

Use the activation command appropriate for PowerShell when working on Windows.

## Configure environment variables

`.env.example` contains:

```text
APP_NAME=Distribution Hub API
ENVIRONMENT=development
POSTGRES_DB=distribution_hub
POSTGRES_USER=distribution
POSTGRES_PASSWORD=distribution_dev
DATABASE_URL=postgresql+psycopg://distribution:distribution_dev@localhost:5432/distribution_hub
JWT_SECRET=replace-me-with-a-local-development-secret
```

Use a local secret of your own. `JWT_SECRET` exists in configuration, but the current API does not implement JWT authentication.

## Start and stop PostgreSQL

```bash
docker compose up -d postgres
docker compose ps
docker compose logs postgres
docker compose stop postgres
```

The service health check uses `pg_isready`. To also remove the local data volume, which is destructive for persisted data:

```bash
docker compose down -v
```

## Run migrations

With the database available:

```bash
alembic upgrade head
alembic current
alembic heads
```

`current` should point to the same final revision reported by `heads`.

To review SQL without applying it:

```bash
alembic upgrade head --sql
```

Migration testing against an empty database must use a database separate from development.

## Start the API

```bash
uvicorn app.main:app --reload
```

Verify the API locally:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

The generated FastAPI documentation is also available at `/docs` and `/openapi.json`. No manually maintained OpenAPI file exists in the repository.

## Run tests

Unit tests can be run with:

```bash
pytest tests/unit tests/test_health.py
```

Integration tests require a separate database and the following variable:

```bash
export TEST_DATABASE_URL=postgresql+psycopg://distribution:test_password@localhost:5432/distribution_hub_test
pytest
```

The test configuration rejects a URL whose database is not `distribution_hub_test`.

## Quality checks

```bash
ruff check .
```

CI installs the project, runs migrations, executes `pytest`, and runs `ruff check .` against PostgreSQL 16.

## Quick diagnosis

If the application does not start, confirm that `.env` exists and that `DATABASE_URL` points to an accessible PostgreSQL instance. If a migration fails, confirm that the service is healthy and that the selected database is correct. If integration tests fail before running, confirm `TEST_DATABASE_URL` and the `distribution_hub_test` database name.

The current API has no structured logging, metrics, tracing, separate readiness endpoint, or automated backup and recovery mechanism.
