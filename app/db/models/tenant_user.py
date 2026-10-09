from datetime import datetime
from typing import Literal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class TenantUser(Base):
    __tablename__ = "tenant_users"

    id: Mapped[int] = mapped_column(primary_key=True)

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="RESTRICT"),
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    )

    role: Mapped[Literal["ADMIN", "OPERATOR"]] = mapped_column(
        String(20),
        nullable=False,
        default="OPERATOR",
        server_default="OPERATOR",
    )

    status: Mapped[Literal["ACTIVE", "SUSPENDED"]] = mapped_column(
        String(20),
        nullable=False,
        default="ACTIVE",
        server_default="ACTIVE",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            "tenant_id",
            "user_id",
            name="uq_tenant_users_tenant_user",
        ),
        CheckConstraint(
            "role IN ('ADMIN', 'OPERATOR')",
            name="ck_tenant_users_role",
        ),
        CheckConstraint(
            "status IN ('ACTIVE', 'SUSPENDED')",
            name="ck_tenant_users_status",
        ),
        Index("ix_tenant_users_tenant_id", "tenant_id"),
        Index("ix_tenant_users_user_id", "user_id"),
    )
