# Modelo de dados documentado

Este documento descreve um modelo relacional **especificado**, não um schema já criado. O repositório contém PostgreSQL para desenvolvimento local e espaço para migrations, mas não possui modelos de domínio ou migrations comerciais. Tipos, campos e regras abaixo provêm da documentação de domínio preservada e ainda precisam ser validados antes de uso em produção.

## `users` — pessoas que acessam o sistema

| Campo documentado | Tipo descrito | Observação |
|---|---|---|
| `id` | UUID | Chave primária proposta. |
| `name` | VARCHAR(120) | Nome de apresentação. |
| `email` | VARCHAR(255) | A política de obrigatoriedade, unicidade, verificação e associação à identidade OAuth ainda está por definir. |
| `status` | ENUM | Valores documentados: `ACTIVE`, `INACTIVE`. |
| `created_at` | TIMESTAMP | Data de criação; não deve ser alterada. |
| `updated_at` | TIMESTAMP | Atualizada quando os dados mudam. |

A versão preservada do modelo incluía `password_hash` e tratava email como login. Esses campos **não são considerados decisão vigente** após a escolha de OAuth 2.0. Identidade externa, OIDC e necessidade de armazenar credenciais continuam por definir.

## `tenants` — empresas

| Campo documentado | Tipo descrito | Obrigatório no rascunho | Observação |
|---|---|---:|---|
| `id` | UUID | Sim | Chave primária proposta. |
| `legal_name` | VARCHAR(150) | Sim | Nome legal. |
| `trade_name` | VARCHAR(150) | Não | Nome comercial. |
| `tax_id` | VARCHAR(30) | Não | Identificação fiscal; regra por país pendente. |
| `email` | VARCHAR(255) | Não | Contato geral. |
| `phone` | VARCHAR(30) | Não | Contato geral. |
| `website` | VARCHAR(255) | Não | Site. |
| `address_line` | VARCHAR(200) | Não | Endereço principal. |
| `address_complement` | VARCHAR(100) | Não | Complemento. |
| `postal_code` | VARCHAR(20) | Não | Código postal. |
| `city` | VARCHAR(100) | Não | Cidade. |
| `state` | VARCHAR(100) | Não | Estado, distrito ou região. |
| `country` | VARCHAR(100) | Não | País. |
| `status` | ENUM | Sim | `ACTIVE` ou `INACTIVE`. |
| `created_at`, `updated_at` | TIMESTAMP | Sim | Datas de criação e atualização. |

Regras documentadas: a empresa mantém ao menos um `ADMIN` ativo e não é apagada fisicamente no fluxo normal.

## `tenant_users` — associação entre pessoa e empresa

| Campo documentado | Tipo descrito | Obrigatório no rascunho | Observação |
|---|---|---:|---|
| `id` | UUID | Sim | Chave primária proposta. |
| `user_id` | UUID | Sim | Referência a `users.id`. |
| `tenant_id` | UUID | Sim | Referência a `tenants.id`. |
| `role` | ENUM | Sim | `ADMIN` ou `OPERATOR`. |
| `status` | ENUM | Sim | `ACTIVE` ou `INACTIVE`. |
| `created_at`, `updated_at` | TIMESTAMP | Sim | Datas de criação e atualização. |

A combinação `user_id + tenant_id` é única. Um vínculo inativo não permite acesso à empresa. O papel pertence ao vínculo. O primeiro administrador é criado no fluxo de criação/associação da empresa, cujo desenho completo depende das decisões de identidade e onboarding.

## `customers` — clientes comerciais

| Campo documentado | Tipo descrito | Obrigatório no rascunho | Observação |
|---|---|---:|---|
| `id` | UUID | Sim | Chave primária proposta. |
| `tenant_id` | UUID | Sim | Referência a `tenants.id`. |
| `customer_code` | VARCHAR(30) | Não | Código interno, único dentro da empresa quando informado. |
| `customer_type` | ENUM | Sim | Valores documentados: `INDIVIDUAL` ou `BUSINESS`. |
| `name` | VARCHAR(150) | Sim | Nome de apresentação. |
| `legal_name` | VARCHAR(150) | Não | Nome legal. |
| `trade_name` | VARCHAR(150) | Não | Nome comercial. |
| `tax_id` | VARCHAR(30) | Não | Identificação fiscal. |
| `contact_name` | VARCHAR(120) | Não | Pessoa de contato. |
| `email` | VARCHAR(255) | Não | Email de contato; se fornecido, deve ter formato válido. |
| `phone`, `mobile_phone` | VARCHAR(30) | Não | Telefones de contato. |
| `address_line` | VARCHAR(200) | Não | Rua e número. |
| `address_complement` | VARCHAR(100) | Não | Complemento. |
| `postal_code` | VARCHAR(20) | Não | Código postal. |
| `city`, `state`, `country` | VARCHAR(100) | Não | Localização. |
| `notes` | TEXT | Não | Observações internas. |
| `status` | ENUM | Sim | `ACTIVE` ou `INACTIVE`. |
| `created_at`, `updated_at` | TIMESTAMP | Sim | Datas de criação e atualização. |

Clientes pertencem a uma empresa, não têm acesso próprio no escopo documentado, e clientes inativos não podem ser usados em novos pedidos. A operação normal é inativar, mantendo o histórico.

## Relações e integridade propostas

```text
users   1 ── N tenant_users
                       N ── 1 tenants
                               1 ── N customers
```

As chaves estrangeiras descritas são `tenant_users.user_id → users.id`, `tenant_users.tenant_id → tenants.id` e `customers.tenant_id → tenants.id`. `tenant_users(user_id, tenant_id)` deve ser único; `customers(tenant_id, customer_code)` deve ser único quando o código existir. `tenant_id` é a fronteira de isolamento dos dados comerciais.

O rascunho cita índices em `customers.tenant_id`, `name`, `customer_code`, `email`, `tax_id` e `status`; confirme-os com os padrões de consulta antes de criar migrations. Nenhuma migration ou constraint de negócio existe ainda.

## Áreas sem modelo de campos

Produtos, categorias, preços, movimentos de estoque, pedidos e itens, recebíveis e pagamentos aparecem nas regras de negócio, mas não têm schema detalhado neste documento. Seus campos, estados, relacionamentos e histórico são questões abertas, não dados a inferir.
