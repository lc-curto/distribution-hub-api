# Cosmetics Hub API

Backend FastAPI do Cosmetics Hub. O frontend React/TypeScript fica no repositório separado [cosmetics-hub-web](https://github.com/lc-curto/cosmetics-hub-web). A documentação comum do produto, da API e da arquitetura fica neste repositório.

## Comece por aqui

- [Índice de toda a documentação](docs/README.md)
- [Visão do produto](docs/product/vision.md)
- [Escopo](docs/product/scope.md)
- [Estado atual e funcionalidades implementadas](docs/project-status.md)
- [Arquitetura e decisões](docs/architecture/overview.md)

## Desenvolvimento local

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
docker compose up -d postgres
uvicorn app.main:app --reload
```

Executar os testes com `pytest`. Atualmente, a API fornece `GET /health`, coberto por teste. FastAPI disponibiliza `/docs` e `/openapi.json` para os endpoints existentes; não há ainda endpoints de produto.

## Estado do produto

Os requisitos e as regras estão documentados, mas autenticação, empresas, clientes, catálogo, estoque, pedidos e recebíveis ainda não foram implementados. Consulte [estado atual](docs/project-status.md) antes de tratar uma capacidade como disponível.
