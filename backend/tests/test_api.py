from backend.api.main import health_check, mock_classifications


def test_health_endpoint_returns_ok():
    response = health_check()

    assert response["status"] == "ok"
    assert response["service"] == "backend"


def test_mock_classifications_endpoint_returns_items():
    body = mock_classifications()

    assert body["count"] > 0
    assert body["items"][0]["review"] == "R1"
