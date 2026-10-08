# Distribution Hub API

Backend do **Distribution Hub**, uma aplicação de gestão comercial desenvolvida como MVP e projeto de portefólio profissional.

O frontend está no repositório [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web).

## Tecnologias

- Python 3.12
- FastAPI
- SQLAlchemy 2
- Alembic
- PostgreSQL 16
- Docker Compose
- pytest e Ruff
- GitHub Actions

## Arquitetura

A aplicação utiliza uma arquitetura de monólito modular. O frontend comunica com a API por HTTP/JSON, e a API utiliza SQLAlchemy para aceder à base de dados PostgreSQL.

```text
Frontend React/TypeScript
        ↓ HTTP/JSON
     API FastAPI
        ↓ SQLAlchemy
     PostgreSQL
```

## Estado atual

A base do backend inclui:

- Endpoint `GET /health`;
- Configuração através de variáveis de ambiente;
- Ligação ao PostgreSQL com SQLAlchemy;
- Migrations com Alembic;
- Modelos iniciais `User` e `Tenant`;
- Testes automatizados e validação com GitHub Actions.

Os módulos comerciais — como clientes, catálogo, encomendas, inventário e recebíveis — ainda não têm os respetivos fluxos de API implementados. Consulta a documentação para distinguir funcionalidades implementadas de requisitos planeados.

## Como executar localmente

### Pré-requisitos

- Python 3.12;
- Docker Desktop com Docker Compose;
- Git.

### Preparar o ambiente

Na pasta do projeto, cria e ativa um ambiente virtual e instala as dependências:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
Copy-Item .env.example .env
```

Inicia o PostgreSQL:

```powershell
docker compose up -d postgres
```

Aplica as migrations:

```powershell
alembic upgrade head
```

Inicia a API:

```powershell
uvicorn app.main:app --reload
```

A API fica disponível em `http://127.0.0.1:8000`.

- **Documentação interativa:** http://127.0.0.1:8000/docs
- **Health check:** http://127.0.0.1:8000/health

Confirma no ficheiro `.env` se a variável `DATABASE_URL` aponta para a base de dados local correta.

## Testes

Executa os testes com:

```powershell
pytest
```

Os testes de integração necessitam de uma base de dados de teste separada. Configura `TEST_DATABASE_URL` para essa base antes de executar os testes de integração. Não utilizes a base de dados de desenvolvimento para testes.

A integração contínua executa os testes e a verificação de estilo com Ruff.

## Estrutura principal

```text
app/
├── core/       # Configuração da aplicação
├── db/         # Base de dados e modelos
├── modules/    # Módulos da aplicação
└── main.py     # Entrada da API
alembic/        # Migrations da base de dados
tests/          # Testes automatizados
docs/           # Documentação do produto e arquitetura
```

## Documentação

- [Índice da documentação](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/README.md)
- [Produto e âmbito](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/product.md)
- [Domínio e regras de negócio](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/domain.md)
- [Requisitos](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/requirements.md)
- [Arquitetura](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/architecture.md)
- [API](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/api.md)
- [Modelo Entidade–Relacionamento](https://github.com/lc-curto/distribution-hub-api/blob/main/docs/er.md)

## Repositórios relacionados

- **Frontend:** [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web)
