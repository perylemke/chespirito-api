from http import HTTPStatus
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.api import app
from app.db import DB_CAST

client = TestClient(app)


mock_db_cast = [
    {'_id': 1, 'name': 'Actor 1'},
    {'_id': 2, 'name': 'Actor 2'},
]


@patch('app.db.DB_CAST', mock_db_cast)
def test_get_cast_and_returns_all_cast():
    response = client.get('/api/elenco')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == DB_CAST


@patch('app.db.DB_CAST', mock_db_cast)
def test_get_actor_and_returns_a_actor():
    actor_id = DB_CAST[0]['_id']
    response = client.get(f'/api/elenco/{actor_id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == DB_CAST[0]


@patch('app.db.DB_CAST', mock_db_cast)
def test_get_actor_not_found_and_throw_a_error():
    response = client.get('/api/elenco/9999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Ator não encontrado.'}
