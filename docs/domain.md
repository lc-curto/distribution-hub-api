# Domain and Core Rules

Most of the business domain described below is specified but is not yet exposed through API endpoints. The SQLAlchemy `User`, `Tenant`, and `TenantUser` models exist, as do the migrations for `users`, `tenants`, and `tenant_users`. Customer management and the remaining commercial modules are still pending.

## Concepts

- **User:** A person who has or may have access to the platform.
- **Tenant:** An organization that uses the platform and isolates its data.
- **Membership:** A user–tenant association that stores the user's role and access status within that tenant.
- **Customer:** A person or organization served commercially; customers are not system users in this scope.

A person may belong to multiple tenants and have different roles in each one.

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
2. The backend enforces authorization and tenant isolation; the frontend is not a security boundary.
3. Every protected operation requires an active, authorized tenant context.
4. Each tenant must have at least one active `ADMIN`.
5. The last active `ADMIN` cannot be removed or demoted.
6. Customers belong to a tenant, must be deactivated rather than deleted, and cannot be added to new orders when inactive.
7. Order confirmation validates the customer, products, prices, and inventory atomically.
8. Relevant operations preserve the actor, tenant, timestamp, and context for auditing.

The catalog, inventory, orders, receivables, and dashboard indicators are not yet implemented. Open questions and verifiable requirements are documented in [Requirements and Open Questions](requirements.md).
