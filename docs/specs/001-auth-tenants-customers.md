# Spec 001 — Auth, Tenants e Customers

## Objetivo

Permitir que um utilizador entre no sistema, selecione uma empresa à qual pertence e faça a gestão de clientes dessa empresa.

## Fluxo principal

1. Utilizador informa email e senha.
2. Sistema valida credenciais.
3. Sistema disponibiliza as empresas associadas.
4. Utilizador seleciona uma empresa ativa.
5. Sistema permite listar, criar, consultar e editar clientes.

## Regras

- Senhas são armazenadas apenas como hash.
- Rotas privadas exigem autenticação.
- O utilizador só acede a empresas às quais está associado.
- Clientes só podem ser consultados dentro da empresa ativa.
- Nome do cliente é obrigatório.
- Email, quando informado, deve ser válido.

## Critérios de aceitação

- Login válido cria uma sessão/token seguro.
- Credencial inválida retorna erro genérico de autenticação.
- Utilizador sem associação não acede aos dados de uma empresa.
- Cliente válido é criado na empresa ativa.
- Consulta nunca devolve clientes de outro tenant.

## Entregas

- migrations;
- schemas Pydantic;
- routers FastAPI;
- regras de autorização;
- telas React;
- testes unitários, integração e E2E.
