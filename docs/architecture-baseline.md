# Fundamentos da arquitetura

## Forma geral

A arquitetura prevista combina uma aplicação web, uma API e uma base de dados relacional. O backend é organizado como um **monólito modular**: uma aplicação de API estruturada em módulos, sem pressupor serviços independentes.

## Stack prevista

- **Web:** React, TypeScript e Vite.
- **API:** FastAPI e Python.
- **Base de dados:** PostgreSQL.
- **Persistência e evolução do schema:** SQLAlchemy e Alembic.
- **Desenvolvimento local:** Docker Compose.
- **Autenticação:** OAuth 2.0; o provedor, o fluxo e os detalhes de tokens ou cookies não são especificados neste baseline.

## Separação por empresa

O produto é multiempresa. Os utilizadores pertencem a empresas através de uma associação que também representa o papel do utilizador naquela empresa. O acesso aos dados deve respeitar o contexto da empresa correspondente.

## Limites deste baseline

Este documento regista a forma geral da arquitetura e as tecnologias previstas. Não é um guia operacional nem uma especificação de implementação; detalhes que possam mudar durante o desenvolvimento não são definidos aqui.
