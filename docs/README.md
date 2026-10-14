# Distribution Hub Documentation

Product and technical documentation maintained in the API repository. The frontend repository is [distribution-hub-web](https://github.com/lc-curto/distribution-hub-web).

## Start Here

- [Product Scope](product.md)
- [Domain and Core Rules](domain.md)
- [Requirements and Open Questions](requirements.md)
- [Architecture](architecture.md)
- [API](api.md)
- [Learning and Development Roadmap](learning-roadmap.md)
- [Specification 001 — Authentication, Tenants, and Customers](specs/001-auth-tenants-customers.md)

## Current Status

The API currently exposes `GET /health`, covered by a test. Customer and other commercial endpoints have not yet been implemented. The frontend remains a scaffold.

The backend includes the SQLAlchemy models `User`, `Tenant`, `TenantUser`, and `Customer`, with database migrations for these entities.

The `Customer` model supports individuals and companies, belongs to a tenant, and includes an internal customer code, optional contact and tax information, an active status, and creation and update timestamps.

Database constraints enforce valid customer types, nonblank customer codes, case-insensitive customer code uniqueness within a tenant, and the paired presence of tax identifier and country. Unit and integration tests cover the model and its constraints.

Customer CRUD endpoints, authentication, authorization, and the remaining commercial workflows are still pending.

## Documentation Status

- **Implemented:** Verified in code and supported by appropriate tests or checks.
- **Specified:** Intended behavior is documented but not yet implemented.
- **To be decided:** A decision or acceptance criterion remains unresolved.

Requirements and diagrams describe intended behavior; they are not evidence that a feature has been delivered.