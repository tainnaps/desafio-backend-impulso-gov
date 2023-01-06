import json

import pytest
from fastapi.testclient import TestClient

from src.main import app

ENDPOINT = "/listarEstabelecimentosPorMunicipio"
client = TestClient(app)


@pytest.mark.parametrize("city_id", [316292, 320140, "316292", "320140"])
def test_get_all_by_city_id_success(city_id):
    response = client.get(f"{ENDPOINT}/{city_id}")
    assert response.status_code == 200

    with open(f"tests/mocks/get_all_by_city_id_{city_id}.json", "r") as file:
        content = file.read()
        mocked_json = json.loads(content)
    assert response.json() == mocked_json


def test_get_all_without_city_id():
    response = client.get(f"{ENDPOINT}/")
    assert response.status_code == 404


def test_get_all_by_inexistent_city_id():
    response = client.get(f"{ENDPOINT}/0")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.parametrize("city_id", ["abfgdf", "972dgf"])
def test_get_by_invalid_city_id(city_id):
    response = client.get(f"{ENDPOINT}/{city_id}")
    assert response.status_code == 400
    assert response.json() == {
        "error": "1 validation error for Request path -> city_id"
        " value is not a valid integer (type=type_error.integer)"
    }
