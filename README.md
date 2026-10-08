# Distribution Hub API

API backend do Distribution Hub, uma aplicação de gestão comercial construída para servir como MVP e portefólio profissional.

O frontend está no repositório [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web).

## Stack

- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- Alembic
- PostgreSQL 16
- Docker Compose
- Pydantic Settings
- pytest
- Ruff
- GitHub Actions

## Arquitetura

O projeto é um monólito modular em FastAPI. A separação entre os repositórios da API e do frontend não significa que existam microserviços.

```text
Utilizador
    ↓
Frontend React/TypeScript
    ↓ HTTP/JSON
API FastAPI
    ↓ SQLAlchemy
PostgreSQL
```

Repositórios:

- API: `distribution-hub-api`
- Web: `distribution-hub-web`

A documentação de produto, domínio, arquitetura e requisitos é mantida neste repositório.

## Estado atual

A API possui atualmente:

- `GET /health` implementado e coberto por teste;
- configuração da aplicação carregada através de `.env`;
- `SQLAlchemy Engine` configurado;
- `DeclarativeBase` configurada;
- Alembic configurado para migrations;
- modelo `User` implementado;
- modelo `Tenant` implementado;
- tabela `users` criada e atualizada através de migrations;
- tabela `tenants` criada através de migration;
- unicidade global do e-mail sem distinção entre maiúsculas e minúsculas;
- testes unitários e de integração da persistência inicial;
- validação automática através do GitHub Actions.

Ainda não existem endpoints comerciais para utilizadores, empresas, clientes, catálogo, pedidos, estoque ou recebíveis.

O frontend continua num estado inicial, sem fluxos comerciais implementados.

## Configuração local

### Pré-requisitos

- Python 3.12 ou compatível com `pyproject.toml`;
- Docker Desktop;
- Git;
- Docker Compose.

### Preparar o ambiente

No terminal, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
Copy-Item .env.example .env
```

Inicia o PostgreSQL local:

```powershell
docker compose up -d postgres
```

Confirma o estado do serviço:

```powershell
docker compose ps
```

Aplica as migrations:

```powershell
alembic upgrade head
```

Inicia a API:

```powershell
uvicorn app.main:app --reload
```

A API fica disponível em:

```text
http://127.0.0.1:8000
```

Documentação OpenAPI:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

## Base de dados e migrations

O PostgreSQL de desenvolvimento é executado pelo Docker Compose. A aplicação lê a ligação através de `DATABASE_URL` no `.env`.

Comandos úteis:

```powershell
alembic current
alembic heads
alembic upgrade head
alembic downgrade -1
```

Para gerar uma nova migration depois de alterar um modelo:

```powershell
alembic revision --autogenerate -m "describe the change"
```

Uma migration gerada automaticamente deve ser analisada antes de ser aplicada.

Migrations principais existentes:

- criação da tabela `users`;
- expansão do modelo `User`;
- índice de unicidade case-insensitive para o e-mail;
- criação da tabela `tenants`.

## Modelos atuais

### `User`

Representa a identidade global de uma pessoa:

```text
id
email
first_name
last_name
is_active
email_verified_at
last_login_at
created_at
updated_at
```

`first_name` e `last_name` são opcionais. O e-mail é obrigatório e existe uma restrição única baseada em `lower(email)`, para que estes valores sejam considerados iguais:

```text
lucas@email.com
Lucas@Email.com
LUCAS@EMAIL.COM
```

A relação do utilizador com uma empresa será representada posteriormente por `tenant_users`; o papel não pertence diretamente a `users`.

### `Tenant`

Representa uma empresa que utiliza a plataforma:

```text
id
name
legal_name
tax_id
is_active
created_at
updated_at
```

`legal_name` e `tax_id` são opcionais. A empresa começa ativa por defeito.

## Testes

Executa os testes com:

```powershell
pytest
```

A cobertura atual inclui:

- teste do endpoint `/health`;
- teste unitário do modelo `Tenant`;
- teste de persistência do modelo `Tenant`;
- teste unitário da validação de `TEST_DATABASE_URL`.

Os testes de integração utilizam uma base de dados separada chamada:

```text
distribution_hub_test
```

A fixture de integração valida a URL antes de criar um `Engine`. Assim, uma URL apontando para a base de desenvolvimento `distribution_hub` é rejeitada sem abrir uma ligação à base de dados.

Para executar os testes de integração localmente, define uma URL de teste:

```powershell
$env:TEST_DATABASE_URL="postgresql+psycopg://distribution:test_password@localhost:5432/distribution_hub_test"
pytest
```

A base de testes deve existir e não deve ser a mesma base utilizada pelo desenvolvimento.

## Integração contínua

O GitHub Actions executa automaticamente:

1. PostgreSQL 16 como serviço;
2. instalação das dependências;
3. migrations na base `distribution_hub_test`;
4. `pytest`;
5. verificação de estilo com `ruff check .`.

A configuração da CI utiliza exclusivamente a base de testes e não a base de desenvolvimento.

## Estrutura principal

```text
app/
├── core/                 # Configuração da aplicação
├── db/                   # Engine, Base e modelos SQLAlchemy
├── modules/              # Módulos previstos do domínio
│   ├── auth/
│   ├── catalog/
│   ├── customers/
│   ├── inventory/
│   ├── orders/
│   ├── receivables/
│   └── tenants/
└── main.py               # Instância FastAPI e endpoints básicos

alembic/
├── versions/             # Histórico de migrations
└── env.py                # Integração entre Alembic e a aplicação

tests/
├── unit/                 # Testes sem dependência de serviços externos
├── integration/          # Testes que utilizam PostgreSQL
├── conftest.py           # Fixtures e validações de ambiente de teste
└── test_health.py        # Teste do endpoint health

docs/
├── README.md
├── product.md
├── domain.md
├── requirements.md
├── architecture.md
├── api.md
├── er.md
├── learning-roadmap.md
└── specs/
```

## Documentação do projeto

- [Documentação da pasta docs](docs/README.md)
- [Produto e escopo](docs/product.md)
- [Domínio e regras essenciais](docs/domain.md)
- [Requisitos e pendências](docs/requirements.md)
- [Arquitetura](docs/architecture.md)
- [API](docs/api.md)
- [Modelo Entidade–Relacionamento](docs/er.md)
- [Roadmap de aprendizagem e desenvolvimento](docs/learning-roadmap.md)
- [Spec 001 — acesso, empresas e clientes](docs/specs/001-auth-tenants-customers.md)

Os documentos distinguem:

- **Implementado:** existe no código e possui validação adequada;
- **Especificado:** comportamento pretendido, ainda não implementado;
- **Por definir:** decisão ou critério ainda pendente.

Requisitos, diagramas e especificações não são evidência de funcionalidade entregue.

## Próximas etapas

A ordem de implementação prevista para o MVP é:

1. consolidar `User` e `Tenant`;
2. criar `tenant_users`;
3. criar clientes;
4. criar produtos;
5. criar listas de preços;
6. criar saldo e movimentos de estoque por empresa e produto;
7. criar pedidos e itens;
8. criar recebíveis e pagamentos;
9. criar endpoints e autorização por empresa.

As alterações devem continuar a ser desenvolvidas em branches próprias, com commits em inglês, testes e Pull Requests antes da integração na `main`.
