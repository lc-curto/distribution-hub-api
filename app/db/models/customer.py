from datetime import datetime
from typing import Literal

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, validates

from app.db.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id", ondelete="RESTRICT"),
        nullable=False,
    )

    customer_code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    customer_type: Mapped[Literal["INDIVIDUAL", "COMPANY"]] = (
        mapped_column(String(20), nullable=False)
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    email: Mapped[str | None] = mapped_column(
        String(320),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    tax_id: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    tax_id_country: Mapped[str | None] = mapped_column(
        String(2),
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default=text("true"),
        nullable=False,
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
        CheckConstraint(
            "customer_type IN ('INDIVIDUAL', 'COMPANY')",
            name="ck_customers_customer_type",
        ),
        CheckConstraint(
            "customer_code = btrim(customer_code) "
            "AND customer_code <> ''",
            name="ck_customers_customer_code_not_blank",
        ),
        CheckConstraint(
            "(tax_id IS NULL AND tax_id_country IS NULL) "
            "OR (tax_id IS NOT NULL AND tax_id_country IS NOT NULL)",
            name="ck_customers_tax_id_country",
        ),
        Index(
            "uq_customers_tenant_customer_code_lower",
            "tenant_id",
            func.lower(customer_code),
            unique=True,
        ),
        Index(
            "ix_customers_tenant_id",
            "tenant_id",
        ),
    )

    def __init__(self, **kwargs):
        kwargs.setdefault("is_active", True)
        super().__init__(**kwargs)

    @validates("customer_code")
    def normalize_customer_code(
        self,
        key: str,
        value: str,
    ) -> str:
        return value.strip().upper()