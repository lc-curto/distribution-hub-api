# Domain and product

## Product vision

Distribution Hub is a commercial-management application for organizations that need to manage customers and, later, catalog, inventory, orders, and receivables. Each organization is a tenant, and its commercial data must remain isolated.

This document describes what the product is intended to be. The [data model](DATA_MODEL.md) describes what currently exists in the database and is not a substitute for the complete domain model.

## Tenant boundary

A user may belong to multiple tenants and may have different roles in each one. The user's association with a tenant is represented by a membership that stores the role and access status.

Every protected operation must occur inside an authorized tenant. A client request must not obtain authorization merely by sending a `tenant_id`. The API must resolve the identity, verify active membership, and apply the authorized tenant to every query and change.

This is a product rule, but HTTP authentication and authorization are not implemented yet.

## Actors and permissions

The system uses tenant-scoped RBAC (Role-Based Access Control). A user's role belongs to the membership in a tenant, not to the global user account. The permission model uses least privilege: a role receives only the actions required for its responsibilities.

### Permission matrix

| Resource or operation | ADMIN | OPERATOR |
|---|---|---|
| View the tenant dashboard | Yes | Yes |
| Manage users, memberships, and tenant settings | Yes | No |
| View customers | Yes | Yes |
| Create customers | Yes | Yes |
| Update customers | Yes | Yes |
| Deactivate customers | Yes | Yes |
| Reactivate customers | Yes | No |
| Physically delete customers | No | No |
| View categories, products, and prices | Yes | Yes |
| Create, update, deactivate, and delete catalog records | Yes | No |
| View stock balances and movement history | Yes | Yes |
| Record ordinary stock receipts and issues | Yes | Yes |
| Perform stock adjustments | Yes | No |
| Create and update order drafts | Yes | Yes |
| View orders | Yes | Yes |
| Confirm orders | Yes | No |
| Cancel orders | Yes | No |
| View receivables and payment history | Yes | Yes |
| Record permitted payments | Yes | Yes |
| Void payments, write off balances, or change financial rules | Yes | No |

`Yes` means that the action is allowed only after identity, active membership, tenant scope, and any resource-specific business rule have been validated. `No` means that the action must be rejected by the API, not merely hidden by the frontend.

### Authorization rules

The following rules apply to every protected operation:

1. Access is denied by default when no permission is explicitly granted.
2. The user account must be active.
3. The membership for the requested tenant must be active.
4. The role is evaluated within the requested tenant.
5. Every query and mutation must be restricted to the authorized tenant.
6. A client-provided `tenant_id` is not proof of authorization.
7. Physical deletion is not available for customers, confirmed orders, stock movements, receivables, or confirmed payments.
8. The last active `ADMIN` of a tenant cannot be removed or demoted.
9. The frontend may hide unavailable actions, but the backend remains the security boundary.

This matrix is a product decision. The authorization code, request dependencies, and authorization tests are still pending implementation.

## Customers

A customer can be an individual (`INDIVIDUAL`) or a company (`COMPANY`). It belongs to a tenant, has an internal code, and may contain contact, address, and tax-identification data.

The code is required and must be unique within the tenant without case sensitivity. Customers should be deactivated instead of physically deleted. Inactive customers must not be used in new orders.

The customer API has not been implemented. The database already contains the `Customer` model and its constraints.

## Catalog and pricing

The product is expected to organize categories, products, and prices. Products and prices will belong to a tenant and must respect activity status and consistency rules.

These entities do not exist in the current database.

## Inventory

Inventory is expected to record balances and movements, including receipts, issues, and adjustments. Operations that would result in an invalid balance must fail without a partial update. Relevant movements should preserve actor, tenant, timestamp, and context.

These entities and operations are not implemented.

## Orders

The planned flow is:

1. create a draft order;
2. add items;
3. calculate subtotal, discounts, and total;
4. confirm while validating customer, products, prices, and inventory;
5. cancel according to the defined rules.

Confirmation must be atomic: a validation failure must not leave the order or inventory partially updated. Orders and order items do not exist in the current database.

## Receivables and payments

A confirmed order may create a receivable. Payments may be partial or full while preserving the balance and receivable status. Confirmed financial records should not be deleted without traceability.

Receivables and payments are not implemented.

## First functional flow

The first functional product flow is customer management by an authorized user inside a tenant. It should cover development identity, active tenant, authorization, customer creation, reading, updating, and deactivation, together with a corresponding frontend screen.

Catalog, inventory, orders, receivables, and dashboards are outside this first flow.

## Documentation status

- **Implemented:** code, migration, or test evidence exists.
- **Defined:** a product rule is approved, even if code does not implement it yet.
- **Planned:** a capability is expected in a later stage.
- **Pending:** a decision is required before implementation.

## Open decisions

- production authentication provider and flow;
- active-tenant transport;
- implementation mechanism for the approved permission matrix;
- customer pagination, filtering, and ordering;
- customer reactivation;
- country-specific tax-identifier validation;
- cancellation and inventory-reversal policy;
- payment methods and historical retention;
- API version and contract compatibility.
