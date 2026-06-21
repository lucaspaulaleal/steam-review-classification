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


def test_mock_graph_data_endpoint_returns_200_and_graph_shape():
    response = client.get("/graph/mock-data")
    body = response.json()

    assert response.status_code == 200
    assert len(body["nodes"]) > 0
    assert len(body["links"]) > 0
    assert {"id", "label", "type"}.issubset(body["nodes"][0])
    assert {"source", "target", "type", "weight"}.issubset(body["links"][0])


def test_realtime_classification_endpoint_returns_200_and_scores():
    response = client.post(
        "/reviews/classify",
        json={"text": "O jogo trava muito, tem lag e queda de fps."},
    )
    body = response.json()

    assert response.status_code == 200
    assert body["review"] == "INPUT_REVIEW"
    assert body["category"] == "Performance"
    assert body["score"] > 0
    assert len(body["scores"]) == 4
    assert "fps" in body["tokens"]


def test_realtime_classification_endpoint_rejects_empty_content():
    response = client.post("/reviews/classify", json={"text": "!!! 123 !!!"})

    assert response.status_code == 400


def test_docs_endpoint_returns_200():
    response = client.get("/docs")

    assert response.status_code == 200
