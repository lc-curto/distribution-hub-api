# Cosmetics Hub

MVP de uma plataforma de gestão comercial para distribuidores de cosméticos.

## Stack

- **Web:** React + TypeScript + Vite
- **API:** FastAPI + Python
- **Banco:** PostgreSQL
- **Persistência:** SQLAlchemy 2 + Alembic
- **Mobile:** React Native + Expo (fase posterior)
- **Testes:** Pytest, Vitest e Playwright
- **Ambiente:** Docker Compose

## MVP

Auth, empresas/tenants, clientes, catálogo, estoque, pedidos, contas a receber e dashboard.

## Método

O projeto segue **Spec-Driven Development incremental**: cada fatia é especificada, modelada, implementada, testada e documentada antes da próxima.

Consulte [`docs/product/scope.md`](docs/product/scope.md) e [`docs/specs/001-auth-tenants-customers.md`](docs/specs/001-auth-tenants-customers.md).

## Estado atual

Scaffold inicial. O primeiro incremento é Auth + Tenants + Customers.

## Execução local

```bash
docker compose up -d postgres
cd apps/api && python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]" && uvicorn app.main:app --reload
```

## Licença

Projeto educacional e de portfólio.
