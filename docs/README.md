# Distribution Hub Documentation

Product documentation maintained in the API repository. The frontend repository is [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web).

## Start Here

- [Product Scope](product.md)
- [Domain and Core Rules](domain.md)
- [Requirements and Open Questions](requirements.md)
- [Architecture](architecture.md)
- [API](api.md)
- [Learning and Development Roadmap](learning-roadmap.md)
- [Specification 001 — Authentication, Tenants, and Customers](specs/001-auth-tenants-customers.md)

## Current Status

The API currently exposes `GET /health`, covered by a test. Commercial endpoints have not yet been implemented. The frontend remains a scaffold.

The backend includes the SQLAlchemy `User`, `Tenant`, and `TenantUser` models, together with database migrations for `users`, `tenants`, and `tenant_users`. The `tenant_users` association links users to tenants and stores each user's role and access status within a tenant.

Customer management and the remaining commercial workflows are still pending.

## Documentation Status

- **Implemented:** Verified in code and supported by appropriate tests or checks.
- **Specified:** Intended behavior documented but not yet implemented.
- **To be decided:** A decision or acceptance criterion remains unresolved.

Requirements and diagrams describe intended behavior; they are not evidence that a feature has been delivered.
