import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import URL, make_url


def validate_test_database_url(database_url: str) -> str:
    parsed_url: URL = make_url(database_url)

    if parsed_url.database != "distribution_hub_test":
        pytest.fail("Integration tests must use the distribution_hub_test database.")

    return database_url


@pytest.fixture(scope="session")
def test_database_url() -> str:
    database_url = os.getenv("TEST_DATABASE_URL")

    if not database_url:
        pytest.fail("TEST_DATABASE_URL must be set to run database integration tests.")

    return validate_test_database_url(database_url)


@pytest.fixture(scope="session")
def test_engine(test_database_url: str):
    engine = create_engine(test_database_url, pool_pre_ping=True)

    try:
        yield engine
    finally:
        engine.dispose()
