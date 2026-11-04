from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.tenant import Tenant
from app.db.models.tenant_user import TenantUser
from app.db.models.user import User
from app.db.session import get_db


def get_current_tenant_user(
    x_user_id: Annotated[int | None, Header()] = None,
    x_tenant_id: Annotated[int | None, Header()] = None,
    db: Annotated[Session, Depends(get_db)] = None,
) -> TenantUser:
    if x_user_id is None or x_tenant_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-User-Id and X-Tenant-Id headers are required.",
        )

    statement = (
        select(TenantUser)
        .join(User, User.id == TenantUser.user_id)
        .join(Tenant, Tenant.id == TenantUser.tenant_id)
        .where(
            TenantUser.user_id == x_user_id,
            TenantUser.tenant_id == x_tenant_id,
            TenantUser.status == "ACTIVE",
            User.is_active.is_(True),
            Tenant.is_active.is_(True),
        )
    )

    tenant_user = db.scalar(statement)

    if tenant_user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is not authorized for this tenant.",
        )

    return tenant_user
