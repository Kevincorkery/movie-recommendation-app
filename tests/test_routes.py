from app import create_app

def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"


def test_search_missing_title():
    app = create_app()
    client = app.test_client()

    response = client.get("/search")

    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "title parameter is required"