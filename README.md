# Distribution Hub API

Backend for Distribution Hub, a multi-tenant commercial management application. The API is maintained separately from the web frontend and exposes the HTTP contract consumed by the web application.

## Current status

The API is currently in its foundation stage. Implemented capabilities are:

- `GET /health`;
- configuration through environment variables;
- PostgreSQL connectivity through SQLAlchemy;
- Alembic migrations;
- `User`, `Tenant`, `TenantUser`, and `Customer` models;
- persistence and database-constraint tests for the data model.

Authentication, tenant and membership endpoints, customer endpoints, catalog, inventory, orders, and receivables are not implemented. The frontend is also still a scaffold.

## Architecture and documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Data model](docs/DATA_MODEL.md)
- [Domain and product](docs/DOMAIN.md)
- [Local runbook](docs/RUNBOOK.md)
- [Frontend](https://github.com/lc-curto/distribution-hub-web)

The documentation distinguishes implemented behavior, domain decisions, and planned capabilities. SQLAlchemy models do not automatically represent available HTTP endpoints.

## Technologies

- Python 3.12 in CI;
- FastAPI;
- SQLAlchemy 2;
- Alembic;
- PostgreSQL 16;
- Docker Compose;
- pytest;
- Ruff;
- GitHub Actions.

The project requires Python `>=3.11`; CI uses Python `3.12`.

## Quick start

Requirements: Python, Docker with Compose, and Git.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
cp .env.example .env
docker compose up -d postgres
alembic upgrade head
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

- Interactive documentation: `http://127.0.0.1:8000/docs`
- OpenAPI schema: `http://127.0.0.1:8000/openapi.json`
- Health check: `http://127.0.0.1:8000/health`

See the [runbook](docs/RUNBOOK.md) for complete procedures.

## Tests and quality

Integration tests require `TEST_DATABASE_URL` to point to a separate database named `distribution_hub_test`. CI creates that database, applies migrations, and runs:

```bash
pytest
ruff check .
```

## Main structure

```text
app/                  application code
app/core/             configuration
app/db/               base, session, and SQLAlchemy models
app/modules/          reserved application-module directories
alembic/              migrations
tests/                unit and integration tests
docs/                 technical and domain documentation
```

This repository does not contain production infrastructure, deployment, automated backup, or a validated recovery procedure.
