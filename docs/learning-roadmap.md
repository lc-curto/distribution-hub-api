# Learning and Development Roadmap

This document is the project's **main to-do list**. Before implementing a task, study enough to understand what is being done and why.

Do not measure progress by the amount of code written. Move forward when you can explain the task in your own words.

## How to Use This Document

1. Work on only one task marked as **Now**.
2. Complete the recommended study before writing code.
3. Record questions and unfamiliar terms.
4. Implement a small version.
5. Test manually and run automated tests where applicable.
6. Mark a task complete only when its acceptance criteria are satisfied.
7. If a task seems too large, break it down before starting.

## How to Study a Task

For each task, follow this short cycle:

1. **Understand:** explain what the technology does and which problem it solves.
2. **Observe:** read the official documentation and review a minimal example.
3. **Practice:** complete an isolated exercise before integrating it into the project.
4. **Explain:** describe the exercise in your own words.
5. **Apply:** only then make the change in Distribution Hub.

Do not try to learn the entire technology before starting. Study only what is needed for the current task and record what can be learned later.

## Work Queue

Keep three groups to avoid working on everything at once:

- **Now:** validate that all database migrations can be applied to a fresh database, then review the customer domain requirements.
- **Next:** define the `Customer` fields and business rules, then implement its SQLAlchemy model, migration, and persistence tests.
- **Later:** improvements and commercial modules that are not yet needed for the first end-to-end workflow.

When a task is completed, move only the next task to **Now**. Do not reorganize the entire project every week.

## Recommended Pace

Complete three study sessions per week, each lasting 60–90 minutes:

- **Session A — Study:** review the concept, official documentation, and a small example.
- **Session B — Implement:** make one small, functional change.
- **Session C — Test and Review:** fix issues, explain what you learned, and update this file.

If you have less time, reduce the task size rather than skipping the study.

## Completion Criteria

A task is complete only when:

- [ ] I can explain what I implemented without copying an explanation.
- [ ] I know which files were changed.
- [ ] I can run the functionality locally.
- [ ] A test or manual verification has been recorded.
- [ ] I have documented any important unresolved questions.
- [ ] I updated the documentation when behavior changed.

---
## Phase 0 — Prepare the Study Environment

**Objective:** Run the API locally before implementing any features.

### Executable Steps

Complete one step at a time and verify the result before continuing:

```bash
# 1. Navigate to the repository
cd caminho/para/distribution-hub-api

# 2. Check the required tools
python3 --version
git --version
docker --version
docker compose version

# 3. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 4. Install project dependencies
python -m pip install --upgrade pip
pip install -e ".[dev]"

# 5. Create the local configuration
cp .env.example .env

# 6. Start only the local PostgreSQL service
docker compose up -d postgres

# 7. Start the API and keep this terminal open
uvicorn app.main:app --reload
```

Open another terminal, activate the environment again, and verify:

```bash
cd caminho/para/distribution-hub-api
source .venv/bin/activate
curl http://127.0.0.1:8000/health
pytest
```

**Expected result:** `curl` returns `{"status":"ok"}` and the tests pass. Then open `http://127.0.0.1:8000/docs` to view the automatic API documentation.

**If something fails:** copy the error message into your notes. Do not try to fix several things at once. First identify whether the problem involves Python, dependencies, Docker, the database, or the API.

### Study Example

Before starting, explain in one sentence: “The virtual environment separates this project dependencies from those installed on my computer.” Do the same for Docker Compose, FastAPI, endpoint, test, and migration.


### Study First

- [ ] Review Git: branch, commit, diff, restore, and log.

- [ ] Review Python: virtual environments, imports, functions, classes, and exceptions.

- [ ] Review HTTP: requests, responses, methods, status codes, and JSON.

- [ ] Understand APIs, backends, frontends, databases, and migrations.

- [ ] Read the README and [architecture](architecture.md).

### Complete

- [x] Clone and run the API locally.

- [x] Call `GET /health`.

- [x] Run the existing tests.

- [x] Create a working branch for the first feature.

- [x] Record questions in personal notes.

**Deliverable:** I can start the API, call `/health`, and explain the basic request flow.

**Before proceeding:** I must know where the API code, tests, and configuration are located, and how to run the project.

---

## Phase 1 — Database and Persistence

> Do not build the entire future database. Implement only what is needed for the first workflow.

### 1.1 PostgreSQL and Migrations

**Example:** Create a minimal `users` table with `id`, `email`, and `created_at`. The model was created first, followed by the migration, migration execution, and verification of the table in PostgreSQL.

**Status:** Completed.

**Study:** Tables, columns, primary keys, foreign keys, indexes, constraints, transactions, SQLAlchemy, and Alembic.

- [x] Understand how PostgreSQL starts through Docker Compose.
- [x] Understand the difference between a Python model, a database table, and a migration.
- [x] Create a simple migration and understand how to reverse it.
- [x] Verify the created table directly in the database.
- [x] Understand `upgrade` and `downgrade`.
- [x] Review the SQL generated by a migration using `--sql`.

### 1.2 User, Tenant, and Membership Models

**Status:** The `User`, `Tenant`, and `TenantUser` SQLAlchemy models and their migrations exist in the repository. Tests cover tenant model persistence. The API does not yet expose commercial endpoints for these models.

- [x] Create the `User` model for global user accounts.
- [x] Create migrations for `users`, including case-insensitive email uniqueness.
- [x] Create the `Tenant` model for organizations.
- [x] Create the migration for `tenants`.
- [x] Add model and persistence tests for `Tenant`.
- [x] Create the `TenantUser` model for the user–tenant membership.
- [x] Add role and access status to the membership.
- [x] Add a uniqueness constraint to prevent duplicate memberships.
- [x] Create and review the `tenant_users` migration.
- [x] Add tests for membership persistence and constraints.
- [ ] Verify that all migrations can be applied to a fresh database and that `alembic current` matches `alembic heads`.

**Key concept:** A user may belong to multiple tenants and have a different role in each. The role belongs to the membership, not to the global `users` record.

**Study:** Many-to-many relationships, foreign keys, uniqueness constraints, referential integrity, roles, and membership status.

### 1.3 Customers

**Example:** Create customer `Loja Rosa` in Tenant A. Authorized users in Tenant A may access it, but users in Tenant B must not. When the customer is deactivated, the record remains available for historical reference but cannot be used in new orders.

**Study:** Soft deletion and deactivation, timestamps, tenant-scoped uniqueness, and customer data modeling.

- [ ] Define the minimum required and optional fields for `Customer`.
- [ ] Define the relationship between `Customer` and `Tenant`.
- [ ] Decide whether `customer_code` is required; if used, make it unique within the tenant.
- [ ] Define customer deactivation and reactivation rules.
- [ ] Create the SQLAlchemy model and migration.
- [ ] Add tests for persistence, tenant ownership, and relevant constraints.
- [ ] Verify that customers cannot be accessed across tenants.

**Phase 1 deliverable:** A database that can be recreated through migrations, with users, tenants, memberships, and customers.

**Before proceeding:** I must be able to recreate the database from migrations and explain why each table exists.

---
## Phase 2 — Backend Fundamentals

### 2.1 API Structure

**Example:** First create a `GET /customers` endpoint that returns an empty list. Then separate the response schema, route, and database query. The initial goal is not a complete CRUD implementation, but understanding the flow “request → validation → business rule → database → response”.


**Study:** FastAPI, dependencies, Pydantic, routers, schemas, and separation between routes, services, and persistence.

- [ ] Understand how a request reaches the database.

- [ ] Define a simple module structure.

- [ ] Create input and output schemas.

- [ ] Learn to validate data and return clear HTTP errors.

### 2.2 Development Identity

**Example:** During development, use a fixed, explicit identity such as `dev-user-a` for tests only. A request without this identity must be rejected. This approach is for learning authorization and must not be presented as production authentication.


> OAuth/OIDC still requires a decision. Do not block learning on a final integration.

**Study:** authentication versus authorization, current user, session/token, and the principle of least privilege.

- [ ] Define a temporary mechanism for development and testing only.

- [ ] Make it explicit in the code that this is not a production solution.

- [ ] Resolve the current user through an API dependency.

- [ ] Reject requests without an identity.

### 2.3 Active Tenant and Authorization

**Example:** User A belongs to Tenants 1 and 2. When querying Tenant 1 customers, the user sees only Tenant 1 customers. If the user changes the tenant identifier to Tenant 2 without authorization, the API rejects the request. Write this negative test before implementing the code.


**Study:** resource-level authorization, multi-tenant isolation, and negative tests.

- [ ] Verify that the user belongs to the tenant.

- [ ] Verify the users role within the correct tenant.

- [ ] Define how the active tenant is provided to the API.

- [ ] Prevent access based solely on a tenant ID supplied by the client.

- [ ] Test a user with two tenants and different roles.

### 2.4 Customer CRUD

**Example sequence:** `POST` creates “Loja Rosa”; `GET` lists the customer; `GET /customers/{id}` retrieves it; `PATCH` updates the phone number; and the deactivation action changes its status. Also test a nonexistent ID, invalid data, and a customer belonging to another tenant.


- [ ] Create `POST /customers`.

- [ ] Create `GET /customers`.

- [ ] Create `GET /customers/{id}`.

- [ ] Create `PATCH /customers/{id}`.

- [ ] Create a deactivation action.

- [ ] Always filter by the authorized tenant.

- [ ] Test success, validation errors, not-found responses, and cross-tenant access.

**Phase 2 deliverable:** A customer API with authorization and tests.

**Before proceeding:** I must be able to explain the request flow, validate invalid data, and prove through a test that one tenant cannot access another tenants customers.

---

## Phase 3 — Initial Frontend

### Study First

**Example:** Before building a feature screen, create a test screen that fetches `/health` and displays “API online”. This teaches HTTP requests without mixing in forms, authentication, and database logic.


- [ ] Review React: components, props, state, and events.

- [ ] Review TypeScript: types, interfaces, and unions.

- [ ] Review HTTP requests and state handling.

- [ ] Understand loading, success, error, and empty states.

- [ ] Understand frontend forms and validation.

### Implementation

**Example:** The first real screen can simply list customers. Then add the creation form, followed by editing and deactivation. At each stage, handle loading, success, error, and empty-list states explicitly.


- [ ] Create a customer list screen.

- [ ] Create a customer form.

- [ ] Integrate customer creation with the API.

- [ ] Integrate editing.

- [ ] Integrate deactivation.

- [ ] Display loading, error, success, and empty-list states.

- [ ] Manually test the complete workflow.

**Phase 3 deliverable:** A user can enter the workflow, select a tenant, and manage customers through the interface.

**Before proceeding:** I must be able to explain how the frontend calls the API and what happens in loading, success, error, and empty-list states.

---

## Phase 4 — Future Modules

Do not start this phase until the first end-to-end workflow is complete.

### Catalog and Pricing

**Example:** Start with a “Lipstick” category and a “Pink Lipstick” product with a decimal price. Do not implement promotions, multiple price lists, or bulk imports in the first version.


- [ ] Study product, category, and monetary value modeling.

- [ ] Define the minimum scope.

- [ ] Create the database tables and migrations.

- [ ] Create endpoints and tests.

- [ ] Create basic screens.

### Inventory

**Example:** Record an incoming quantity of 10 units, an outgoing quantity of 3, and verify a balance of 7. Attempting to remove 8 units must fail without changing the balance. This scenario teaches transactions, validation, and history.


- [ ] Study transactions and consistency.

- [ ] Define stock movements, balances, and history.

- [ ] Build the database, backend, tests, and screens.

### Orders

**Example:** Create a `DRAFT` order with one product, calculate the total, and confirm it. Confirmation may reduce stock only when sufficient inventory exists. If confirmation fails, neither the order nor inventory may be partially updated.


- [ ] Study state machines and transactions.

- [ ] Create order drafts and items.

- [ ] Calculate subtotal, discount, and total.

- [ ] Confirm orders while validating inventory.

- [ ] Integrate orders and inventory.

### Receivables and Dashboard

**Example:** A confirmed order worth 100 creates a receivable of 100. A payment of 40 leaves a balance of 60 and a partially paid status. The dashboard can initially show only monthly sales and the outstanding balance.


- [ ] Study partial payments, balances, and due dates.

- [ ] Create receivables after order confirmation.

- [ ] Create payment records.

- [ ] Create basic metrics by tenant and period.

---

## Weekly Checklist

Copy this section for each week:

**Week of:** ____ / ____ / ____

**Single objective:** __________________________________________

**Study first:** ___________________________________________

- [ ] Study completed

- [ ] Notes written in my own words

- [ ] Small implementation completed

- [ ] Test or verification executed

- [ ] Questions recorded

- [ ] Documentation updated

**What I learned:**

>

**What was difficult:**

>

**Next concrete step:**

>

## When You Are Stuck

Stop coding and answer these questions in writing:

1. What behavior am I trying to deliver?

1. Which concept do I still not understand?

1. What is the smallest example I can build in isolation?

1. How will I know it worked?

1. Is this decision defined in [requirements](requirements.md), or is it still unresolved?

If I cannot answer these questions, the next task is to **study and clarify**, not to implement more code.
