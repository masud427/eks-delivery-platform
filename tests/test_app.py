
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "EKS Delivery Platform"


def test_health_endpoint():
    response = client.get("/healthz")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_readiness_endpoint():
    response = client.get("/readyz")

    assert response.status_code == 200

    assert response.json()["status"] == "ready"
