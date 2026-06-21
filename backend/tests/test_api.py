from starlette.testclient import TestClient

from backend.api.main import app


client = TestClient(app)


def test_root_endpoint_returns_200():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["health"] == "/health"


def test_health_endpoint_returns_200():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_mock_classifications_endpoint_returns_200_and_items():
    response = client.get("/reviews/mock-classifications")
    body = response.json()

    assert response.status_code == 200
    assert body["count"] > 0
    assert body["items"][0]["review"] == "R1"


def test_docs_endpoint_returns_200():
    response = client.get("/docs")

    assert response.status_code == 200
