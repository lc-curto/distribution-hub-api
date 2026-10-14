# Domain and Core Rules

The domain includes system identity, tenant isolation, customer management, and future commercial workflows. Some domain entities are implemented in SQLAlchemy, but most business capabilities are not yet exposed through API endpoints.

## Concepts

- **User:** A person who has or may have access to the platform.
- **Tenant:** An organization that uses the platform and isolates its data.
- **Membership:** A user–tenant association that stores the user's role and access status within that tenant.
- **Customer:** A person or organization served commercially. Customers are not system users in this scope.

A person may belong to multiple tenants and have different roles in each one.

## Implemented Data Models

The following SQLAlchemy models exist:

- `User`
- `Tenant`
- `TenantUser`
- `Customer`

Database migrations exist for these entities, including the `customers` table.

### Customer

A customer belongs to a tenant and represents either an individual or a company.

| Field | Description |
|---|---|
| `id` | Integer primary key |
| `tenant_id` | Required reference to the owning tenant |
| `customer_code` | Required internal customer code, unique case-insensitively within the tenant |
| `customer_type` | `INDIVIDUAL` or `COMPANY` |
| `name` | Required customer name |
| `email` | Optional email address |
| `phone` | Optional phone number |
| `tax_id` | Optional tax identifier |
| `tax_id_country` | Optional two-character country code, required when `tax_id` is supplied |
| `address` | Optional address |
| `is_active` | Active status, defaulting to `true` |
| `created_at` | Creation timestamp |
| `updated_at` | Update timestamp |

The customer code is trimmed and normalized to uppercase by the model. The database enforces case-insensitive uniqueness for each tenant.

The database also enforces the allowed customer types, rejects blank customer codes, and requires `tax_id` and `tax_id_country` to be either both present or both absent.

The customer references `tenants.id` with `ON DELETE RESTRICT`.

Tax identifier format validation by country and external verification are not implemented. Tax identifiers are not required to be unique.

The model, migration, and unit and integration tests are implemented. Customer API endpoints are not yet implemented.

## Planned Actors and Permissions

| Area | `ADMIN` | `OPERATOR` |
|---|---|---|
| Users, roles, and settings | Manage | No permission |
| Customers | Create, read, update, and deactivate | Create, read, update, and deactivate |
| Catalog and pricing | Manage | View and use permitted prices |
| Inventory | Manage operations | View and record permitted operations |
| Orders | Create, confirm, and cancel according to business rules | Create and view; confirmation permissions remain undecided |
| Receivables and payments | Manage according to business rules | Record permitted operations |

The permission matrix is not ready for implementation. Permissions for `OPERATOR` users concerning products, inventory, and payments still require clarification.

## Core Business Rules

1. A user's role belongs to the membership with a tenant, not to the global user account.
2. The backend must enforce authorization and tenant isolation; the frontend is not a security boundary.
3. Every protected operation requires an active, authorized tenant context.
4. Each tenant must have at least one active `ADMIN`.
5. The last active `ADMIN` cannot be removed or demoted.
6. Customers belong to a tenant and must be deactivated rather than deleted.
7. Inactive customers cannot be used in new orders.
8. Order confirmation must validate the customer, products, prices, and inventory atomically.
9. Relevant operations must preserve the actor, tenant, timestamp, and context for auditing.

Rules that depend on API authorization and commercial workflows remain pending implementation.

The catalog, inventory, orders, receivables, and dashboard indicators are not yet implemented. Open questions and verifiable requirements are documented in [Requirements and Open Questions](requirements.md).