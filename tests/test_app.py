import pytest
from httpx import AsyncClient
from asyncio import get_event_loop

from app.main import app


@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="module")
def event_loop():
    loop = get_event_loop()
    yield loop


# Actors (Atores)
@pytest.mark.asyncio
async def test_get_actors_status_code(async_client: AsyncClient) -> None:
    """
    Verifica se o Status Code é 200.
    """
    response = await async_client.get("/api/v1/atores/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_actors_response_all(async_client: AsyncClient) -> None:
    """
    Verifica se retorna um número maior que 0 do Banco de Dados.
    """
    response = await async_client.get("/api/v1/atores/")
    assert len(response.json()) > 0


# Actresses (Atrizes)
@pytest.mark.asyncio
async def test_get_actresses_status_code(async_client: AsyncClient) -> None:
    """
    Verifica se o Status Code é 200.
    """
    response = await async_client.get("/api/v1/atrizes/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_actresses_response_all(async_client: AsyncClient) -> None:
    """
    Verifica se retorna um número maior que 0 do Banco de Dados.
    """
    response = await async_client.get("/api/v1/atrizes/")
    assert len(response.json()) > 0


# Voice Actresses (Dubladoras)
@pytest.mark.asyncio
async def test_get_voice_actresses_status_code(async_client: AsyncClient) -> None:
    """
    Verifica se Status Code é 200.
    """
    response = await async_client.get("/api/v1/dubladoras/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_voice_actresses_response_all(async_client: AsyncClient) -> None:
    """
    Verifica se retorna um número maior que 0 do Banco de Dados.
    """
    response = await async_client.get("/api/v1/dubladoras/")
    assert len(response.json()) > 0


# Voice Actors (Dubladores)
@pytest.mark.asyncio
async def test_get_voice_actors_status_code(async_client: AsyncClient) -> None:
    """
    Verifica se Status Code é 200.
    """
    response = await async_client.get("/api/v1/dubladores/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_voice_actors_response_all(async_client: AsyncClient) -> None:
    """
    Verifica se retorna um número maior que 0 do Banco de Dados.
    """
    response = await async_client.get("/api/v1/dubladores/")
    assert len(response.json()) > 0


# Episodes (Episódios)
@pytest.mark.asyncio
async def test_get_episodes_status_code(async_client: AsyncClient) -> None:
    """
    Verifica se Status Code é 200.
    """
    response = await async_client.get("/api/v1/episodios/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_episodes_response_all(async_client: AsyncClient) -> None:
    """
    Verifica se retorna um número maior que 0 do Banco de Dados.
    """
    response = await async_client.get("/api/v1/episodios/")
    assert len(response.json()) > 0


# Quotes (Frases)
@pytest.mark.asyncio
async def test_get_quotes_status_code(async_client: AsyncClient) -> None:
    """
    Verifica se Status Code é 200.
    """
    response = await async_client.get("/api/v1/frases/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_quotes_response_all(async_client: AsyncClient) -> None:
    """
    Verifica se retorna um número maior que 0 do Banco de Dados.
    """
    response = await async_client.get("/api/v1/frases/")
    assert len(response.json()) > 0


# Characters (Personagens)
@pytest.mark.asyncio
async def test_get_characters_status_code(async_client: AsyncClient) -> None:
    """
    Verifica se Status Code é 200.
    """
    response = await async_client.get("/api/v1/personagens/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_characters_response_all(async_client: AsyncClient) -> None:
    """
    Verifica se retorna um número maior que 0 do Banco de Dados.
    """
    response = await async_client.get("/api/v1/personagens/")
    assert len(response.json()) > 0


# Shows (Programas)
@pytest.mark.asyncio
async def test_get_shows_status_code(async_client: AsyncClient) -> None:
    """
    Verifica se Status Code é 200.
    """
    response = await async_client.get("/api/v1/programas/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_shows_response_all(async_client: AsyncClient) -> None:
    """
    Verifica se retorna um número maior que 0 do Banco de Dados.
    """
    response = await async_client.get("/api/v1/programas/")
    assert len(response.json()) > 0
