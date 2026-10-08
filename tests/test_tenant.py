from app.db.models.tenant import Tenant


def test_tenant_has_required_name():
    tenant = Tenant(name="Test Company")

    assert tenant.name == "Test Company"
    assert tenant.legal_name is None
    assert tenant.tax_id is None
