# Requirements and Open Questions

This document distinguishes implemented behavior from planned capabilities and unresolved decisions.

## Current Implementation Status

The API currently exposes `GET /health`.

The SQLAlchemy models `User`, `Tenant`, `TenantUser`, and `Customer` exist. Database migrations exist for these entities, including the `customers` table.

Customer model tests cover persistence, customer code normalization, tenant-scoped uniqueness, customer type constraints, and tax identifier country constraints.

Customer CRUD endpoints, authentication, authorization, and commercial workflows are not yet implemented.

## Specified Capabilities

- **Access and tenants:** identify users, list associated tenants, select an active tenant, and apply `ADMIN`/`OPERATOR` permissions.
- **Customers:** create, retrieve, search, update, and deactivate customers within a tenant.
- **Catalog and pricing:** manage categories, products, and prices according to permissions.
- **Inventory:** query stock, record receipts, issues, and adjustments with history.
- **Orders:** create drafts, calculate totals, confirm atomically, cancel with a reason, and preserve history.
- **Receivables:** create receivables from orders, record partial or full payments, and calculate balances and due dates.
- **Dashboard:** display sales, orders, receivables, and low-stock indicators by tenant and period.

These are planned capabilities, not evidence of implemented endpoints.

## Customer Data Requirements

The implemented `Customer` model contains:

- `id`
- `tenant_id`
- `customer_code`
- `customer_type`
- `name`
- `email`
- `phone`
- `tax_id`
- `tax_id_country`
- `address`
- `is_active`
- `created_at`
- `updated_at`

Customer types are `INDIVIDUAL` and `COMPANY`.

The internal customer code is required, trimmed, normalized to uppercase by the model, and unique case-insensitively within a tenant.

The tax identifier and country must either both be present or both be absent. Country-specific tax identifier format validation and external verification are not implemented. Tax identifiers are not unique by database constraint.

The following customer capabilities remain pending:

- Customer CRUD API endpoints.
- Search, filtering, and pagination behavior.
- API-level authorization and tenant isolation.
- Validation of tax identifier formats by country.
- Integration with orders and prevention of using inactive customers in new orders.

## Quality and Security Requirements

Identity is required for private resources. The backend must enforce permissions and prevent cross-tenant access. Secrets must not appear in responses. Monetary values must use decimal representation. Errors must follow a consistent format.

Critical rules require unit and integration tests, and key workflows require end-to-end tests.

PostgreSQL is the target database, with referential integrity enforced through database constraints. The API must maintain a compatible HTTP/JSON contract and provide a health check.

Performance, availability, retention, and observability criteria remain undefined.

## Authentication

OAuth 2.0 has been selected as an authorization framework, but the concrete identity solution remains undecided.

The following decisions are still required: federated login, OIDC, identity provider, client type, flow, scopes, tokens, cookies or sessions, logout, renewal, onboarding, and account recovery.

Do not implement authentication before these decisions are documented.

## Open Decisions

- Registration flow: account creation, tenant creation, or invitation.
- Identity provider and concrete authentication design.
- Final `OPERATOR` permission matrix.
- Technical transport of the active tenant context.
- Tax identifier format validation by country.
- Filtering, pagination, currency, calendar, and timezone conventions.
- Stock reversal when an order is cancelled.
- Payment methods and historical retention.
- API versioning and contract validation with the frontend.

## Status Definitions

- **Implemented:** verified in code and supported by appropriate tests or checks.
- **Specified:** intended behavior is documented but not implemented.
- **To be decided:** a decision or acceptance criterion remains unresolved.