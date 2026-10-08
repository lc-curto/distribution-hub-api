import pytest

from tests.conftest import validate_test_database_url


def test_accepts_test_database_url():
    database_url = (
        "postgresql+psycopg://distribution:example@localhost:5432/distribution_hub_test"
    )

    result = validate_test_database_url(database_url)

    assert result == database_url


def test_rejects_development_database_url():
    database_url = (
        "postgresql+psycopg://distribution:example@localhost:5432/distribution_hub"
    )

    with pytest.raises(pytest.fail.Exception):
        validate_test_database_url(database_url)
