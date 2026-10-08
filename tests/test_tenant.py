
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.tenant import Tenant


def test_tenant_has_required_name():
    tenant = Tenant(name="Test Company")

    assert tenant.name == "Test Company"
    assert tenant.legal_name is None
    assert tenant.tax_id is None


def test_tenant_can_be_persisted(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            tenant = Tenant(
                name="Integration Test Company",
                legal_name="Integration Test Company Lda",
                tax_id="TEST-123",
            )
            session.add(tenant)
            session.flush()

            tenant_id = tenant.id

            saved_tenant = session.scalar(
                select(Tenant).where(Tenant.id == tenant_id)
            )

            assert saved_tenant is not None
            assert saved_tenant.name == "Integration Test Company"
            assert saved_tenant.legal_name == "Integration Test Company Lda"
            assert saved_tenant.tax_id == "TEST-123"
            assert saved_tenant.is_active is True
            assert saved_tenant.created_at is not None
            assert saved_tenant.updated_at is not None
    finally:
        transaction.rollback()
        connection.close()