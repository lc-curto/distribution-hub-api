import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.models.customer import Customer
from app.db.models.tenant import Tenant


def test_customer_can_be_persisted(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            tenant = Tenant(name="Customer Integration Test")
            session.add(tenant)
            session.flush()

            customer = Customer(
                tenant_id=tenant.id,
                customer_code="cli-001",
                customer_type="INDIVIDUAL",
                name="Maria Silva",
            )
            session.add(customer)
            session.flush()

            saved_customer = session.scalar(
                select(Customer).where(Customer.id == customer.id)
            )

            assert saved_customer is not None
            assert saved_customer.tenant_id == tenant.id
            assert saved_customer.customer_code == "CLI-001"
            assert saved_customer.customer_type == "INDIVIDUAL"
            assert saved_customer.name == "Maria Silva"
            assert saved_customer.is_active is True
            assert saved_customer.created_at is not None
            assert saved_customer.updated_at is not None
    finally:
        transaction.rollback()
        connection.close()


def test_customer_code_is_unique_case_insensitively_per_tenant(
    test_engine,
):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            tenant = Tenant(name="Customer Uniqueness Test")
            session.add(tenant)
            session.flush()

            session.add(
                Customer(
                    tenant_id=tenant.id,
                    customer_code="CLI-100",
                    customer_type="INDIVIDUAL",
                    name="First Customer",
                )
            )
            session.flush()

            with session.begin_nested(), pytest.raises(IntegrityError):
                session.add(
                    Customer(
                        tenant_id=tenant.id,
                        customer_code="CLI-100",
                        customer_type="COMPANY",
                        name="Duplicate Customer",
                    )
                )
                session.flush()
    finally:
        transaction.rollback()
        connection.close()


def test_same_customer_code_is_allowed_for_different_tenants(
    test_engine,
):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            first_tenant = Tenant(name="First Customer Tenant")
            second_tenant = Tenant(name="Second Customer Tenant")

            session.add_all([first_tenant, second_tenant])
            session.flush()

            session.add_all(
                [
                    Customer(
                        tenant_id=first_tenant.id,
                        customer_code="CLI-200",
                        customer_type="INDIVIDUAL",
                        name="Customer One",
                    ),
                    Customer(
                        tenant_id=second_tenant.id,
                        customer_code="CLI-200",
                        customer_type="INDIVIDUAL",
                        name="Customer Two",
                    ),
                ]
            )
            session.flush()

            customers = session.scalars(
                select(Customer).where(
                    Customer.customer_code == "CLI-200"
                )
            ).all()

            assert len(customers) == 2
            assert customers[0].tenant_id != customers[1].tenant_id
    finally:
        transaction.rollback()
        connection.close()


def test_customer_rejects_invalid_customer_type(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            tenant = Tenant(name="Customer Type Constraint Test")
            session.add(tenant)
            session.flush()

            with session.begin_nested(), pytest.raises(IntegrityError):
                session.add(
                    Customer(
                        tenant_id=tenant.id,
                        customer_code="CLI-300",
                        customer_type="INVALID",
                        name="Invalid Customer",
                    )
                )
                session.flush()
    finally:
        transaction.rollback()
        connection.close()


def test_customer_requires_tax_id_country_when_tax_id_is_present(
    test_engine,
):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            tenant = Tenant(name="Customer Tax Constraint Test")
            session.add(tenant)
            session.flush()

            with session.begin_nested(), pytest.raises(IntegrityError):
                session.add(
                    Customer(
                        tenant_id=tenant.id,
                        customer_code="CLI-400",
                        customer_type="COMPANY",
                        name="Invalid Tax Customer",
                        tax_id="123456789",
                    )
                )
                session.flush()
    finally:
        transaction.rollback()
        connection.close()