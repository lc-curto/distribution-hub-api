# Distribution Hub — Development TODO

## Project rule

Work on one active phase at a time. Do not start a later phase before the previous phase meets its exit criteria. A task is complete only when its implementation, tests, documentation, and acceptance criteria are complete.

## Status legend

- [x] Done
- [ ] Pending
- [~] In progress
- [!] Blocked or awaiting a decision

## Current focus

**Phase:** Identity, tenancy, and API structure

**Goal:** Build the protected foundation required for the first customer-management flow.

**Next action:** Define the temporary development identity and active-tenant mechanism.

## Phase 1 — Product and domain decisions

### Deliverables

- [x] Define the product vision and tenant boundary
- [x] Define the initial actors and membership concept
- [x] Define the initial customer rules
- [x] Define the first end-to-end flow
- [x] Finalize the permission matrix
- [ ] Finalize the authentication direction
- [ ] Finalize the active-tenant transport
- [x] Record the permission decision in the domain documentation
- [ ] Record remaining decisions before implementing affected modules

### Exit criteria

- [ ] The first flow has no unresolved decisions that block implementation
- [ ] Roles and tenant rules are explicit
- [ ] Future modules have defined boundaries

## Phase 2 — Technical foundation

### Deliverables

- [x] FastAPI application
- [x] PostgreSQL configuration
- [x] SQLAlchemy setup
- [x] Alembic migrations
- [x] Docker Compose configuration
- [x] Health endpoint
- [x] Initial CI
- [x] Local technical documentation
- [ ] Validate migrations from an empty database

### Exit criteria

- [ ] A new database can be created from migrations
- [ ] `alembic current` matches `alembic heads`
- [ ] Tests and quality checks pass from a clean environment

## Phase 3 — Base data model

### Access and tenancy

- [x] `users` table and model
- [x] `tenants` table and model
- [x] `tenant_users` table and model
- [x] Membership role and status constraints
- [x] Unique membership per user and tenant
- [ ] Rules for invitations and onboarding
- [ ] Rule preventing removal or demotion of the last active `ADMIN`

### Customers

- [x] `customers` table and model
- [x] Customer constraints
- [x] Customer persistence tests
- [ ] Customer audit history
- [ ] Customer reactivation rule

### Exit criteria

- [ ] All tables required by the first flow are implemented
- [ ] Database constraints cover the agreed integrity rules
- [ ] Persistence tests pass against a fresh database

## Phase 4 — Identity, tenancy, and authorization

### Deliverables

- [ ] Temporary development identity
- [ ] Current-user dependency
- [ ] Active-tenant mechanism
- [ ] Membership authorization
- [ ] Role-based authorization
- [ ] Tenant isolation at the API layer
- [ ] Consistent unauthorized and forbidden responses

### Exit criteria

- [ ] Requests without identity are rejected
- [ ] Inactive users or memberships are rejected
- [ ] Access to an unauthorized tenant is rejected
- [ ] Cross-tenant access tests pass
- [ ] The temporary mechanism is clearly documented as non-production

## Phase 5 — Customer management API

### Deliverables

- [ ] Customer request and response schemas
- [ ] `POST /customers`
- [ ] `GET /customers`
- [ ] `GET /customers/{customer_id}`
- [ ] `PATCH /customers/{customer_id}`
- [ ] Customer deactivation action
- [ ] Customer reactivation, if approved
- [ ] Search, filtering, and pagination, if required for the first flow
- [ ] Success, validation, not-found, and authorization tests

### Exit criteria

- [ ] Authorized users can manage customers
- [ ] Customer data is isolated by tenant
- [ ] Inactive customers are preserved
- [ ] The generated OpenAPI contract matches the implemented endpoints

## Phase 6 — First frontend flow

### Deliverables

- [x] React/Vite scaffold
- [ ] Customer list
- [ ] Customer creation form
- [ ] Customer editing
- [ ] Customer deactivation
- [ ] Loading, empty, success, and error states
- [ ] Frontend tests

### Exit criteria

- [ ] The frontend consumes the customer API
- [ ] A complete customer flow works locally
- [ ] Frontend and API contracts are aligned

## Phase 7 — Catalog and pricing

### Data model

- [ ] Categories
- [ ] Products
- [ ] Price lists
- [ ] Price-list items
- [ ] Tenant-scoped integrity constraints

### Delivery

- [ ] Database migrations
- [ ] API endpoints and authorization
- [ ] Persistence and API tests
- [ ] Frontend screens

### Exit criteria

- [ ] Products can be managed inside a tenant
- [ ] Valid prices can be associated with products
- [ ] Tenant isolation is tested

## Phase 8 — Inventory

### Data model

- [ ] Stock balances
- [ ] Stock movements
- [ ] Movement types and audit context

### Delivery

- [ ] Receipts
- [ ] Issues
- [ ] Adjustments
- [ ] Transactional consistency
- [ ] API, tests, and frontend

### Exit criteria

- [ ] Stock balances are correct
- [ ] Invalid issues are rejected
- [ ] No operation leaves partial data
- [ ] Movement history is preserved

## Phase 9 — Orders

### Data model

- [ ] Orders
- [ ] Order items
- [ ] Order statuses
- [ ] Order history

### Delivery

- [ ] Create order drafts
- [ ] Add and update items
- [ ] Calculate subtotal, discounts, and total
- [ ] Confirm orders
- [ ] Cancel orders
- [ ] Integrate inventory
- [ ] API, tests, and frontend

### Exit criteria

- [ ] Orders validate customer, products, prices, and inventory
- [ ] Confirmation is atomic
- [ ] Cancellation follows defined rules
- [ ] Order history is preserved

## Phase 10 — Receivables and payments

### Data model

- [ ] Receivables
- [ ] Payments
- [ ] Payment and receivable statuses
- [ ] Due dates and historical records

### Delivery

- [ ] Create receivables after order confirmation
- [ ] Record partial payments
- [ ] Record full payments
- [ ] Calculate balances
- [ ] API, tests, and frontend

### Exit criteria

- [ ] Confirmed orders can generate receivables
- [ ] Payments update balances correctly
- [ ] Overpayment rules are enforced
- [ ] Financial history is preserved

## Phase 11 — Dashboard and operations

### Deliverables

- [ ] Tenant-based indicators
- [ ] Sales metrics
- [ ] Order metrics
- [ ] Receivables metrics
- [ ] Low-stock indicators
- [ ] Production deployment
- [ ] Structured logging and monitoring
- [ ] Backup and recovery
- [ ] Production migration procedure

### Exit criteria

- [ ] Metrics are calculated from real data
- [ ] Operational procedures are validated
- [ ] Production risks and limitations are documented

## Open decisions

- [ ] Production authentication provider and flow
- [ ] Active-tenant transport
- [ ] Final permission matrix
- [ ] Customer pagination and filtering
- [ ] Country-specific tax-identifier validation
- [ ] Inventory reversal on order cancellation
- [ ] Payment methods and retention
- [ ] API versioning and contract compatibility

## Current blockers

None. The next implementation decision is the temporary development identity and active-tenant mechanism.
