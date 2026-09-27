# Distribution Hub API

Backend FastAPI do Distribution Hub. O frontend React/TypeScript fica no repositório separado [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web).

## Comece por aqui

- [Documentação consolidada](docs/README.md)
- [Produto e escopo](docs/product.md)
- [Estado da API](docs/api.md)
- [Arquitetura](docs/architecture.md)
- [Roadmap de aprendizagem e desenvolvimento](docs/learning-roadmap.md)

## Desenvolvimento local

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
docker compose up -d postgres
uvicorn app.main:app --reload
```

Execute os testes com `pytest`. Atualmente, a API fornece `GET /health`, coberto por teste. FastAPI disponibiliza `/docs` e `/openapi.json` para os endpoints existentes.

## Estado do produto

Autenticação, empresas, clientes, catálogo, estoque, pedidos e recebíveis estão especificados, mas ainda não implementados. Consulte o [estado e pendências](docs/README.md) antes de tratar qualquer capacidade como disponível.
