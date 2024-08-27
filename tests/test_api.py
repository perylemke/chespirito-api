from http import HTTPStatus

from fastapi.testclient import TestClient

from app.api import app
from app.config import API_URL

client = TestClient(app)


def test_home():
    response = client.get('/api')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'Geral': {
            'Elenco': f'{API_URL}/api/elenco/',
        },
    }
