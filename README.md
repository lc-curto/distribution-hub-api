# Cosmetics Hub API

Backend FastAPI do Cosmetics Hub. O frontend é mantido separadamente em `cosmetics-hub-web`.

## Fundamentos do projeto

- [Fundamentos do produto](docs/product-baseline.md)
- [Fundamentos da arquitetura](docs/architecture-baseline.md)
- [Modelo conceptual do domínio](docs/domain-model.md)
- [Diagrama conceptual do domínio](docs/diagrams/domain-baseline.mmd)

## Desenvolvimento local

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
docker compose up -d postgres
uvicorn app.main:app --reload
```

Executar os testes com `pytest`. A verificação de saúde está disponível em `GET /health`.

Para conectar ao PostgreSQL, copie `.env.example` para `.env` e configure `DATABASE_URL`. A documentação interativa fica em `/docs`; o contrato OpenAPI gerado fica em `/openapi.json`.
