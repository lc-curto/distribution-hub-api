# ADR-002 — React no frontend e FastAPI na API

**Estado:** Aceito
**Data da decisão original:** não registrada na fonte preservada. Revisado em 2026-09-27.

## Contexto

O projeto precisa de uma interface web e de uma API que possa atender clientes independentes. A escolha também considera o objetivo formativo e de portfólio do projeto.

## Decisão

Usar **React, TypeScript e Vite** para o frontend e **Python com FastAPI** para a API. PostgreSQL está configurado como banco local; SQLAlchemy e Alembic fazem parte das dependências e do espaço de evolução do backend, sem schema comercial implementado.

## Consequências

- Frontend e backend se integram por contrato HTTP/JSON.
- FastAPI fornece OpenAPI gerado para as rotas existentes.
- O frontend não deve importar código Python do backend.
- A existência do scaffold e das dependências não significa que os fluxos do produto estejam implementados.
- O contrato OpenAPI e sua validação pelo frontend precisam evoluir junto com os endpoints.

## Reavaliação

Reavaliar apenas diante de restrições técnicas ou de produto que não possam ser atendidas pela stack atual.
