import json

import pytest
from fastapi.testclient import TestClient

from src.main import app

ENDPOINT = "/obterEstabelecimentoPorId"
client = TestClient(app)


@pytest.mark.parametrize("cnes_id", [2187396, 9729135, "2187396", "9729135"])
def test_get_by_cnes_id_success(cnes_id):
    response = client.get(f"{ENDPOINT}/{cnes_id}")
    assert response.status_code == 200

    with open(f"tests/mocks/get_by_cnes_id_{cnes_id}.json", "r") as file:
        content = file.read()
        mocked_json = json.loads(content)
    assert response.json() == mocked_json


def test_get_without_cnes_id():
    response = client.get(f"{ENDPOINT}/")
    assert response.status_code == 404


def test_get_by_inexistent_cnes_id():
    response = client.get(f"{ENDPOINT}/0")
    assert response.status_code == 404
    assert response.json() == {"error": "Establishment not found"}


@pytest.mark.parametrize("cnes_id", ["abfgdrf", "9729dgf"])
def test_get_by_invalid_cnes_id(cnes_id):
    response = client.get(f"{ENDPOINT}/{cnes_id}")
    assert response.status_code == 400
    assert response.json() == {
        "error": "1 validation error for Request path -> cnes_id"
        " value is not a valid integer (type=type_error.integer)"
    }
