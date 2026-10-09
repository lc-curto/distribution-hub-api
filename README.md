# Distribution Hub API

Backend for **Distribution Hub**, a commercial management application developed as a Minimum Viable Product (MVP) and a professional portfolio project.

The frontend is available in the [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web) repository.

## Technologies

- Python 3.12
- FastAPI
- SQLAlchemy 2
- Alembic
- PostgreSQL 16
- Docker Compose
- pytest and Ruff
- GitHub Actions

## Architecture

The application follows a modular monolith architecture. The frontend communicates with the API over HTTP/JSON, and the API uses SQLAlchemy to access the PostgreSQL database.

```text
Frontend React/TypeScript
        ↓ HTTP/JSON
     API FastAPI
        ↓ SQLAlchemy
     PostgreSQL
```

## Current Status

The backend foundation includes:

- `GET /health` endpoint;
- Configuration through environment variables;
- PostgreSQL connectivity using SQLAlchemy;
- Database migrations managed with Alembic;
- Initial `User` and `Tenant` models;
- Automated tests and validation through GitHub Actions.

The business modules — including customers, catalog, orders, inventory, and receivables — do not yet have their corresponding API workflows implemented. Refer to the documentation to distinguish implemented features from planned requirements.

## Running Locally

### Prerequisites

- Python 3.12;
- Docker Desktop with Docker Compose;
- Git.

### Setting Up the Environment

From the project directory, create and activate a virtual environment and install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
Copy-Item .env.example .env
```

Start PostgreSQL:

```powershell
docker compose up -d postgres
```

Apply the database migrations:

```powershell
alembic upgrade head
```

Start the API:

```powershell
uvicorn app.main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

- **Interactive API documentation:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Health check:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

Check the `.env` file to ensure that `DATABASE_URL` points to the correct local database.

## Tests

Run the tests with:

```powershell
pytest
```

Integration tests require a separate test database. Configure `TEST_DATABASE_URL` to point to that database before running the integration tests. Do not use the development database for testing.

The continuous integration pipeline runs the tests and checks code style with Ruff.

## Main Structure

```text
app/
├── core/       # Application configuration
├── db/         # Database and models
├── modules/    # Application modules
└── main.py     # API entry point
alembic/        # Database migrations
tests/          # Automated tests
docs/           # Product and architecture documentation
```

## Documentation

- [Documentation Index](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/README.md)
- [Product and Scope](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/product.md)
- [Domain and Business Rules](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/domain.md)
- [Requirements](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/requirements.md)
- [Architecture](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/architecture.md)
- [API](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/api.md)
- [Entity–Relationship Model](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/er.md)

## Related Repositories

- **Frontend:** [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web)