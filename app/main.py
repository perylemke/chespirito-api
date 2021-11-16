from fastapi import FastAPI

from .models import Actor, Episode
from typing import List

import motor.motor_asyncio

from decouple import config


# Setup DBs
MONGO_URI = config('DB_URI', default='localhost', cast=str)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db_general = client.generaldb
db_chaves = client.chavesdb

# Setup FastAPI
app = FastAPI()


@app.get("/api/v1/atores/", response_model=List[Actor])
async def get_actors():
    """
    View para consultar os atores. Retorna um dict com todos os atores.
    """
    actors_res = await db_general.actors.find().to_list(1000)
    return actors_res


@app.get("/api/v1/atrizes/", response_model=List[Actor])
async def get_actresses():
    """
    View para consultar as atrizes. Retorna um dict com todos as atrizes.
    """
    actress_res = await db_general.actresses.find().to_list(1000)
    return actress_res


@app.get("/api/v1/dubladoras/")
async def get_voice_actresses():
    """
    View para consultar as dubladoras. Retorna um dict com todos as dubladoras.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/dubladores/")
async def get_voice_actors():
    """
    View para consultar os dubladores. Retorna um dict com todos os dubladores.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/episodios/", response_model=List[Episode])
async def get_episodes():
    """
    View para consultar os episódios. Retorna um dict com todos os episódios.
    """
    episodes_res = await db_chaves.episodes.find().to_list(1000)
    return episodes_res


@app.get("/api/v1/frases/")
async def get_quotes():
    """
    View para consultar os frases. Retorna um dict com todas as frases.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/personagens/")
async def get_characters():
    """
    View para consultar os personagens.
    Retorna um dict com todos os personagens.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/programas/")
async def get_shows():
    """
    View para consultar os programas. Retorna um dict com todos os programas.
    """
    return {"Status": "Work in Progress"}
