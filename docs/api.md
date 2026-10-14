# API

## Current Status

The API currently exposes the following endpoint:

| Method | Path | Response | Status |
|---|---|---|---|
| `GET` | `/health` | `200` with `{"status":"ok"}` | Implemented and tested |

No API endpoints for authentication, tenants, customers, catalog, inventory, orders, or receivables have been implemented.

## Customer Domain

The `Customer` SQLAlchemy model and its database migration are implemented. Unit and integration tests cover the model's persistence and database constraints.

This does not mean customer management is available through HTTP. Customer creation, retrieval, search, update, and deactivation endpoints remain pending.

## OpenAPI

FastAPI generates the API contract at `/openapi.json` and interactive documentation at `/docs`.

The generated contract describes the routes currently registered in the application, including `/health`. It does not imply that planned customer or commercial endpoints exist.

As additional capabilities are implemented, the API contract must evolve alongside endpoint tests and frontend integration.

API versioning and contract validation between the backend and frontend repositories remain pending decisions.