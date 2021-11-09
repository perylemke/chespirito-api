from fastapi.testclient import TestClient
from app.main import app


# Starts API for tests
client = TestClient(app)


# Actors (Atores)
def test_actors_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/atores/")
    assert response.status_code == 200


def test_actors_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/atores/")
    assert response.json() == {"Status": "Work in Progress"}


# Actresses (Atrizes)
def test_actresses_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/atrizes/")
    assert response.status_code == 200


def test_actresses_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/atrizes/")
    assert response.json() == {"Status": "Work in Progress"}


# Houses (Casas)
def test_houses_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/casas/")
    assert response.status_code == 200


def test_houses_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/casas/")
    assert response.json() == {"Status": "Work in Progress"}


# Voice Actresses (Dubladoras)
def test_voice_actresses_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/dubladoras/")
    assert response.status_code == 200


def test_voice_actresses_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/dubladoras/")
    assert response.json() == {"Status": "Work in Progress"}


# Voice Actors (Dubladores)
def test_voice_actors_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/dubladores/")
    assert response.status_code == 200


def test_voice_actors_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/dubladores/")
    assert response.json() == {"Status": "Work in Progress"}


# Episodes (Episódios)
def test_episodes_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/episodios/")
    assert response.status_code == 200


def test_episodes_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/episodios/")
    assert response.json() == {"Status": "Work in Progress"}


# Voice Studios (Estúdios de Dublagem)
def test_voice_studios_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/estudios/")
    assert response.status_code == 200


def test_voice_studios_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/estudios/")
    assert response.json() == {"Status": "Work in Progress"}


# Movies (Filmes)
def test_movies_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/filmes/")
    assert response.status_code == 200


def test_movies_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/filmes/")
    assert response.json() == {"Status": "Work in Progress"}


# Quotes (Frases)
def test_quotes_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/frases/")
    assert response.status_code == 200


def test_quotes_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/frases/")
    assert response.json() == {"Status": "Work in Progress"}


# Characters (Personagens)
def test_character_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/personagens/")
    assert response.status_code == 200


def test_character_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/personagens/")
    assert response.json() == {"Status": "Work in Progress"}


# Shows (Programas)
def test_shows_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/programas/")
    assert response.status_code == 200


def test_shows_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/programas/")
    assert response.json() == {"Status": "Work in Progress"}


# Seasons (Temporadas)
def test_seasons_status_code():
    """
    Verifica se Status Code é 200.
    """
    response = client.get("/api/v1/temporadas/")
    assert response.status_code == 200


def test_seasons_response_json():
    """
    Verifica se o retorno é um JSON.
    """
    response = client.get("/api/v1/temporadas/")
    assert response.json() == {"Status": "Work in Progress"}
