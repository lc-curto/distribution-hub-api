from fastapi.testclient import TestClient

from app.main import app


def test_list_customers_returns_empty_list():
    response = TestClient(app).get("/customers/")

    assert response.status_code == 200
    assert response.json() == []
