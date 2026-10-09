
import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.models.tenant import Tenant
from app.db.models.tenant_user import TenantUser
from app.db.models.user import User


def test_tenant_user_has_default_role_and_status(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            user = User(email="tenant-user-defaults@example.com")
            tenant = Tenant(name="Tenant User Defaults Test")
            session.add_all([user, tenant])
            session.flush()

            association = TenantUser(
                tenant_id=tenant.id,
                user_id=user.id,
            )
            session.add(association)
            session.flush()

            assert association.role == "OPERATOR"
            assert association.status == "ACTIVE"
    finally:
        transaction.rollback()
        connection.close()


def test_tenant_user_can_be_persisted(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            user = User(email="tenant-user@example.com")
            tenant = Tenant(name="Tenant User Test")
            session.add_all([user, tenant])
            session.flush()

            association = TenantUser(
                tenant_id=tenant.id,
                user_id=user.id,
                role="ADMIN",
            )
            session.add(association)
            session.flush()

            saved = session.scalar(
                select(TenantUser).where(TenantUser.id == association.id)
            )

            assert saved is not None
            assert saved.role == "ADMIN"
            assert saved.status == "ACTIVE"
            assert saved.created_at is not None
            assert saved.updated_at is not None
    finally:
        transaction.rollback()
        connection.close()


def test_tenant_user_rejects_duplicate_membership(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            user = User(email="duplicate-membership@example.com")
            tenant = Tenant(name="Duplicate Membership Test")
            session.add_all([user, tenant])
            session.flush()

            session.add(TenantUser(tenant_id=tenant.id, user_id=user.id))
            session.flush()

            with pytest.raises(IntegrityError), session.begin_nested():
                session.add(
                    TenantUser(
                        tenant_id=tenant.id,
                        user_id=user.id,
                    )
                )
                session.flush()
    finally:
        transaction.rollback()
        connection.close()


@pytest.mark.parametrize(
    ("role", "status"),
    [
        ("INVALID", "ACTIVE"),
        ("ADMIN", "INVALID"),
    ],
)
def test_tenant_user_rejects_invalid_role_or_status(
    test_engine, role, status
):
    connection = test_engine.connect()
    transaction = connection.begin()

    try:
        with Session(bind=connection) as session:
            user = User(email=f"invalid-{role}-{status}@example.com")
            tenant = Tenant(name="Invalid Membership Test")
            session.add_all([user, tenant])
            session.flush()

            with pytest.raises(IntegrityError), session.begin_nested():
                session.add(
                    TenantUser(
                        tenant_id=tenant.id,
                        user_id=user.id,
                        role=role,
                        status=status,
                    )
                )
                session.flush()
    finally:
        transaction.rollback()
        connection.close()