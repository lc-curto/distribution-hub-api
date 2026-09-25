# Modelo de dados — MVP

**Produto:** Cosmetics Hub
**Escopo:** MVP

<!-- ============================================================
     CONTEXTO: UTILIZADORES
     ============================================================ -->

## users

Representa os utilizadores que podem autenticar-se no sistema.

| Campo | Tipo | Obrigatório | Regra |
|---|---|---:|---|
| `id` | UUID | Sim | Chave primária |
| `name` | VARCHAR(120) | Sim | Nome do utilizador |
| `email` | VARCHAR(255) | Sim | Único e usado no login |
| `password_hash` | VARCHAR(255) | Sim | Nunca armazena a palavra-passe original |
| `status` | ENUM | Sim | `ACTIVE` ou `INACTIVE` |
| `created_at` | TIMESTAMP | Sim | Data de criação |
| `updated_at` | TIMESTAMP | Sim | Data da última alteração |

<!-- CONTEXTO: SEPARAÇÃO ENTRE UTILIZADOR, EMPRESA E PAPEL -->

O papel e a empresa não pertencem diretamente a `users`. Essas informações

ficam em `tenant_users`, permitindo que o mesmo utilizador tenha papéis

diferentes em empresas diferentes.

### Regras

- `id` deve ser a chave primária.

- `email` deve ser único.

- `password_hash` nunca deve armazenar a palavra-passe original.

- `status` deve ser `ACTIVE` ou `INACTIVE`.

- `created_at` não deve ser alterado.

- `updated_at` deve ser atualizado quando os dados mudarem.

### Índices

Definir os índices iniciais de `users` antes da migration.

### Relacionamentos

- `tenant_users.user_id` → `users.id`

<!-- ============================================================
     CONTEXTO: EMPRESAS / TENANTS
     ============================================================ -->

## tenants

Representa as empresas cadastradas no Cosmetics Hub.

| Campo | Tipo | Obrigatório | Regra |
|---|---|---:|---|
| `id` | UUID | Sim | Chave primária |
| `legal_name` | VARCHAR(150) | Sim | Nome legal da empresa |
| `trade_name` | VARCHAR(150) | Não | Nome comercial |
| `tax_id` | VARCHAR(30) | Não | Identificação fiscal |
| `email` | VARCHAR(255) | Não | Email geral |
| `phone` | VARCHAR(30) | Não | Telefone geral |
| `website` | VARCHAR(255) | Não | Site da empresa |
| `address_line` | VARCHAR(200) | Não | Morada principal |
| `address_complement` | VARCHAR(100) | Não | Complemento |
| `postal_code` | VARCHAR(20) | Não | Código postal |
| `city` | VARCHAR(100) | Não | Cidade |
| `state` | VARCHAR(100) | Não | Distrito ou região |
| `country` | VARCHAR(100) | Não | País |
| `status` | ENUM | Sim | `ACTIVE` ou `INACTIVE` |
| `created_at` | TIMESTAMP | Sim | Data de criação |
| `updated_at` | TIMESTAMP | Sim | Data da última alteração |

### Regras

- `id` deve ser a chave primária.

- `legal_name` é obrigatório.

- `status` deve ser `ACTIVE` ou `INACTIVE`.

- Uma empresa deve possuir pelo menos um `ADMIN` ativo.

- Uma empresa nunca deve ser eliminada fisicamente no fluxo normal.

- `created_at` não deve ser alterado.

- `updated_at` deve ser atualizado quando os dados mudarem.

### Índices

Definir os índices iniciais de `tenants` antes da migration.

### Relacionamentos

- `tenant_users.tenant_id` → `tenants.id`

- `customers.tenant_id` → `tenants.id`

<!-- ============================================================
     CONTEXTO: VÍNCULO UTILIZADOR–EMPRESA
     ============================================================ -->

## tenant_users

Representa a associação entre utilizadores e empresas.

Um utilizador pode pertencer a várias empresas e possuir papéis diferentes

em cada uma.

| Campo | Tipo | Obrigatório | Regra |
|---|---|---:|---|
| `id` | UUID | Sim | Chave primária |
| `user_id` | UUID | Sim | Referência para `users.id` |
| `tenant_id` | UUID | Sim | Referência para `tenants.id` |
| `role` | ENUM | Sim | `ADMIN` ou `OPERATOR` |
| `status` | ENUM | Sim | `ACTIVE` ou `INACTIVE` |
| `created_at` | TIMESTAMP | Sim | Data da associação |
| `updated_at` | TIMESTAMP | Sim | Data da última alteração |

<!-- CONTEXTO: REGRAS DO VÍNCULO -->

### Regras

- `user_id` deve referenciar um utilizador existente.

- `tenant_id` deve referenciar uma empresa existente.

- O mesmo utilizador não pode ser associado duas vezes à mesma empresa.

- A combinação `user_id + tenant_id` deve ser única.

- O papel pertence ao vínculo, não à tabela `users`.

- O primeiro utilizador de uma empresa recebe `role = ADMIN`.

- Uma empresa deve possuir pelo menos um `ADMIN` ativo.

- Um vínculo `INACTIVE` não permite acesso à empresa.

- `created_at` não deve ser alterado.

- `updated_at` deve ser atualizado quando o vínculo mudar.

<!-- CONTEXTO: ÍNDICES DO VÍNCULO -->

### Índices

Definir os índices iniciais de `tenant_users` antes da migration.

<!-- CONTEXTO: RELACIONAMENTOS DO VÍNCULO -->

### Relacionamentos

- `tenant_users.user_id` → `users.id`

- `tenant_users.tenant_id` → `tenants.id`

<!-- ============================================================
     CONTEXTO: CLIENTES
     ============================================================ -->

## customers

Representa os clientes comerciais de uma empresa.

Um cliente pertence a apenas uma empresa e não possui acesso ao sistema
no MVP.

| Campo | Tipo | Obrigatório | Regra |
|---|---|---:|---|
| `id` | UUID | Sim | Chave primária |
| `tenant_id` | UUID | Sim | Referência para `tenants.id` |
| `customer_code` | VARCHAR(30) | Não | Código interno do cliente |
| `customer_type` | ENUM | Sim | `INDIVIDUAL` ou `BUSINESS` |
| `name` | VARCHAR(150) | Sim | Nome de apresentação |
| `legal_name` | VARCHAR(150) | Não | Nome legal, principalmente para empresas |
| `trade_name` | VARCHAR(150) | Não | Nome comercial |
| `tax_id` | VARCHAR(30) | Não | Identificação fiscal |
| `contact_name` | VARCHAR(120) | Não | Pessoa de contacto |
| `email` | VARCHAR(255) | Não | Email do cliente |
| `phone` | VARCHAR(30) | Não | Telefone principal |
| `mobile_phone` | VARCHAR(30) | Não | Telemóvel |
| `address_line` | VARCHAR(200) | Não | Rua e número |
| `address_complement` | VARCHAR(100) | Não | Complemento da morada |
| `postal_code` | VARCHAR(20) | Não | Código postal |
| `city` | VARCHAR(100) | Não | Cidade |
| `state` | VARCHAR(100) | Não | Distrito ou região |
| `country` | VARCHAR(100) | Não | País |
| `notes` | TEXT | Não | Observações internas |
| `status` | ENUM | Sim | `ACTIVE` ou `INACTIVE` |
| `created_at` | TIMESTAMP | Sim | Data de criação |
| `updated_at` | TIMESTAMP | Sim | Data da última alteração |

### Valores permitidos

`customer_type`:

```text
INDIVIDUAL
BUSINESS
```

`status`:

```text
ACTIVE
INACTIVE
```

### Regras

- `id` deve ser a chave primária.
- `tenant_id` deve referenciar `tenants.id`.
- `name` é obrigatório.
- `customer_type` é obrigatório.
- `legal_name` é recomendado quando `customer_type = BUSINESS`.
- `tax_id` é opcional no MVP.
- `email` é opcional.
- Se informado, o email deve ter formato válido.
- `customer_code`, quando informado, deve ser único dentro da empresa.
- `status` começa como `ACTIVE`.
- Clientes inativos não devem aparecer em novos pedidos.
- Clientes inativos podem permanecer visíveis no histórico.
- Clientes de uma empresa não podem ser consultados por outra.
- A exclusão normal é feita através de inativação.
- `created_at` não deve ser alterado.
- `updated_at` deve ser atualizado quando os dados mudarem.

### Índices

Criar índices para:

```text
customers.tenant_id
customers.name
customers.customer_code
customers.email
customers.tax_id
customers.status
```

A combinação abaixo deve ser única quando os valores estiverem
preenchidos:

```text
customers.tenant_id + customers.customer_code
```

### Relacionamento

```text
customers.tenant_id → tenants.id
```

<!-- ============================================================
     CONTEXTO: CARDINALIDADES
     ============================================================ -->

## Cardinalidades

As cardinalidades representam quantos registros de uma entidade podem

estar relacionados com outra entidade.

```text
users 1 ─── N tenant_users

tenants 1 ─── N tenant_users

tenants 1 ─── N customers
```

<!-- ============================================================
     CONTEXTO: ISOLAMENTO POR TENANT
     ============================================================ -->

## Regras de isolamento

As entidades de negócio pertencentes a uma empresa devem estar associadas

ao respetivo `tenant_id`.

No MVP:

- `customers` possui `tenant_id`.

- `tenant_users` possui `tenant_id`.

- O acesso aos dados deve considerar a empresa ativa.

- O backend deve validar a associação do utilizador à empresa ativa.

- O frontend não pode ser considerado uma camada de segurança.

- Um utilizador não pode consultar ou alterar dados de outra empresa.

<!-- ============================================================
     CONTEXTO: CHAVES E CONSTRAINTS
     ============================================================ -->

## Chaves e constraints principais

- Cada entidade deve possuir uma chave primária.

- Foreign keys devem preservar a integridade dos relacionamentos.

- `tenant_users.user_id` → `users.id`.

- `tenant_users.tenant_id` → `tenants.id`.

- `customers.tenant_id` → `tenants.id`.

- A combinação `user_id + tenant_id` em `tenant_users` deve ser única.

- As regras adicionais de unicidade devem ser definidas antes da migration.

<!-- ============================================================
     CONTEXTO: ÍNDICES
     ============================================================ -->

## Índices iniciais

Os índices definitivos devem ser definidos antes da criação das migrations.

Índices já definidos para o MVP:

- `customers.tenant_id`;

- `customers.name`;

- `customers.email`;

- `customers.status`.

Os restantes índices serão definidos após a revisão do modelo.

<!-- ============================================================
     CONTEXTO: DIAGRAMA ER
     ============================================================ -->

## Diagrama ER

O diagrama entidade-relacionamento será mantido em:

```text
database/diagrams/er-model.mmd
```

O diagrama deve representar:

- `users`;

- `tenants`;

- `tenant_users`;

- `customers`;

- chaves primárias;

- foreign keys;

- cardinalidades;

- relacionamentos entre entidades.

<!-- ============================================================
     CONTEXTO: REVISÃO ANTES DA MIGRATION
     ============================================================ -->

## Revisão antes da migration

Antes de criar as migrations, o modelo deve ser revisto para confirmar:

- chaves primárias;

- foreign keys;

- cardinalidades;

- `tenant_id` nas entidades de negócio;

- regras de unicidade;

- índices iniciais;

- regras de isolamento;

- constraints;

- relacionamento entre utilizadores, empresas e clientes.
