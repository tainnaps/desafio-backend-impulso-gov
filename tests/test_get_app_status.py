from fastapi.testclient import TestClient

from src.main import app

ENDPOINT = "/"
client = TestClient(app)


def test_get_app_status_success():
    response = client.get(ENDPOINT)
    assert response.status_code == 200
    assert response.json() == {"message": "Webservice OK"}
