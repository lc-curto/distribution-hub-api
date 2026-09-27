# Modelo de domínio

Este modelo explica os conceitos centrais do produto em linguagem de negócio. Ele não representa um schema implementado: o código atual ainda não contém modelos ou migrations de domínio.

## Conceitos documentados

- **Usuário (`users`):** pessoa que tem ou poderá ter acesso ao sistema.
- **Empresa (`tenants`):** organização que usa a plataforma e cujo contexto separa seus dados comerciais.
- **Associação (`tenant_users`):** vínculo de uma pessoa com uma empresa, incluindo o papel e o estado de acesso naquela empresa.
- **Cliente (`customers`):** pessoa ou organização atendida comercialmente por uma empresa; não é necessariamente usuário do sistema.

Uma pessoa pode estar associada a mais de uma empresa, com papéis diferentes. Uma empresa pode ter várias pessoas associadas e vários clientes comerciais. O [diagrama de domínio](diagrams/domain-model.mmd) mostra essas relações.

## Outras áreas do produto

Catálogo, preços, estoque, pedidos, recebíveis e indicadores pertencem ao escopo documentado do produto. Suas regras estão em [regras de negócio](../requirements/business-rules.md), mas ainda não há modelos de dados detalhados ou implementação para essas áreas.

## Limites e fonte detalhada

Os campos e restrições atualmente descritos para `users`, `tenants`, `tenant_users` e `customers` estão em [modelo de dados](../database/data-model.md). Essa descrição é uma especificação documental, não evidência de tabelas existentes no PostgreSQL.
