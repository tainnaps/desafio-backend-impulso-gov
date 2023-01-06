from fastapi.testclient import TestClient

from src.main import app

ENDPOINT = "/listarEstabelecimentosPorMunicipio"
client = TestClient(app)
