# Arquitetura

## Visão

O sistema é composto por uma aplicação web e uma API em dois repositórios. A API segue uma arquitetura de **monólito modular**: uma aplicação FastAPI organizada por módulos, sem microserviços.

```mermaid
flowchart LR
    Pessoa[Equipa comercial] --> Web[distribution-hub-web<br/>React + TypeScript + Vite]
    Web -->|HTTP / JSON| API[distribution-hub-api<br/>FastAPI + Python]
    API --> DB[(PostgreSQL)]
```

## Repositórios e stack

| Camada | Tecnologia | Estado |
|---|---|---|
| Web | React, TypeScript e Vite | Scaffold; sem fluxos comerciais |
| API | Python e FastAPI | `GET /health` implementado; sem endpoints comerciais |
| Dados | PostgreSQL | Configurado para desenvolvimento local via Docker Compose |
| Persistência | SQLAlchemy e Alembic | Configurados; modelos `User` e `Tenant` e migrations existentes |
| Testes | pytest | Testes de health e testes do modelo/persistência de `Tenant` existentes |
| Integração | HTTP/JSON e OpenAPI | O contrato da API ainda é essencialmente o health check |

A documentação comum fica no repositório da API. A separação de repositórios não significa que existam microserviços ou deploy independente já configurado.

## Persistência atual

A aplicação possui a fundação de persistência configurada:

```text
.env
  ↓
app/core/config.py
  ↓
app/db/session.py
  ↓
SQLAlchemy Engine
  ↓
PostgreSQL
```

### Modelos existentes

- **`User` / `users`:** conta global, com e-mail obrigatório, nome e apelido opcionais, estado ativo, datas de verificação/login e timestamps. Existe um índice único sobre `lower(email)`, para evitar duplicados que diferem apenas em maiúsculas/minúsculas.
- **`Tenant` / `tenants`:** empresa, com nome obrigatório, nome legal e identificador fiscal opcionais, estado ativo e timestamps.

Existem migrations para a tabela `users`, para a evolução do modelo de usuário, para a unicidade case-insensitive do e-mail e para a tabela `tenants`. Existe também `tests/test_tenant.py`, que testa atributos do modelo e persistência.

### Ainda por implementar

- `tenant_users`: associação entre usuário e empresa, incluindo papel e estado;
- `customers`: clientes pertencentes a uma empresa;
- endpoints da API para gerir usuários, empresas e clientes;
- autenticação e autorização efetivas, incluindo isolamento multiempresa;
- integração dos fluxos comerciais no frontend.

A existência de modelos e migrations não significa que os respetivos fluxos de negócio estejam disponíveis pela API. O endpoint comercial ainda não está implementado.

## Decisões vigentes

- Manter a API como monólito modular.
- Usar React/TypeScript/Vite no frontend e FastAPI/Python na API.
- Manter os repositórios `distribution-hub-web` e `distribution-hub-api`.
- Usar PostgreSQL como banco de dados.
- Usar Docker Compose para executar o PostgreSQL localmente.
- Usar SQLAlchemy para o mapeamento entre Python e banco de dados.
- Usar Alembic para versionar alterações na estrutura do banco.
- Manter as configurações da aplicação no `.env`, carregadas por `pydantic-settings`.
- O desenho concreto de identidade/autenticação continua pendente; OAuth/OIDC não deve ser considerado implementado.

## Isolamento e operação

O papel deverá pertencer ao vínculo entre usuário e empresa. Quando os endpoints protegidos forem implementados, o backend terá de validar identidade, associação, empresa ativa e permissão em cada operação.

A CI valida a API e o frontend separadamente. Ainda não há integração comercial entre as aplicações, ambiente de produção, SLA, alta disponibilidade ou observabilidade avançada.
