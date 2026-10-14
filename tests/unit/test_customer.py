
from app.db.models import Customer


def test_customer_code_is_normalized():
    customer = Customer(
        tenant_id=1,
        customer_code="  cli-001  ",
        customer_type="INDIVIDUAL",
        name="Maria Silva",
    )

    assert customer.customer_code == "CLI-001"


def test_customer_code_is_normalized_to_uppercase():
    customer = Customer(
        tenant_id=1,
        customer_code="abc-123",
        customer_type="COMPANY",
        name="Example Company",
    )

    assert customer.customer_code == "ABC-123"


def test_customer_defaults_to_active():
    customer = Customer(
        tenant_id=1,
        customer_code="CLI-002",
        customer_type="INDIVIDUAL",
        name="Joana Costa",
    )

    assert customer.is_active is True


def test_customer_accepts_optional_fields_as_none():
    customer = Customer(
        tenant_id=1,
        customer_code="CLI-003",
        customer_type="INDIVIDUAL",
        name="Ana Martins",
    )

    assert customer.email is None
    assert customer.phone is None
    assert customer.tax_id is None
    assert customer.tax_id_country is None
    assert customer.address is None
