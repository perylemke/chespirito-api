from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import Actor, Episode
from typing import List

import motor.motor_asyncio

from decouple import config


# URL
API_URL = config('API_URL', default='http://localhost:8080', cast=str)

# Setup DBs
MONGO_URI = config('DB_URI', default='localhost', cast=str)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db_general = client.generaldb
db_chaves = client.chavesdb

# Setup FastAPI
app = FastAPI(
    docs_url="/",
    redoc_url=None
)

# Config CORS
origins = [
    "http://chespirito.dev",
    "https://chespirito.dev",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/", include_in_schema=False)
async def home():
    home_text = {
        'Geral': {
            'Atores': f'{API_URL}/api/atores/',
            'Atrizes': f'{API_URL}/api/atrizes/',
            'Dubladores': f'{API_URL}/api/dubladores/',
            'Dubladoras': f'{API_URL}/api/dubladoras/',
            'Programas': f'{API_URL}/api/programas/'
        },
        'Chaves': {
            'Episodios': f'{API_URL}/api/chaves/episodios/',
            'Frases': f'{API_URL}/api/chaves/frases/',
            'Personagens': f'{API_URL}/api/chaves/personagens/',
        },
        'Chapolin': {
            'Episodios': f'{API_URL}/api/chapolin/episodios/',
            'Frases': f'{API_URL}/api/chapolin/frases/',
            'Personagens': f'{API_URL}/api/chapolin/personagens/',
        },
        'Programa Chespirito': {
            'Episodios': f'{API_URL}/api/chapolin/episodios/',
            'Frases': f'{API_URL}/api/chapolin/frases/',
            'Personagens': f'{API_URL}/api/chapolin/personagens/',
            'Quadros': f'{API_URL}/api/chespirito/quadros/'
        }
    }
    return home_text


@app.get("/api/v1/atores/",
         response_model=List[Actor],
         tags=["Geral"])
async def get_actors():
    """
    View para consultar os atores. Retorna um dict com todos os atores.
    """
    actors_res = await db_general.actors.find().to_list(1000)
    return actors_res


@app.get("/api/v1/atrizes/", response_model=List[Actor], tags=["Geral"])
async def get_actresses():
    """
    View para consultar as atrizes. Retorna um dict com todos as atrizes.
    """
    actress_res = await db_general.actresses.find().to_list(1000)
    return actress_res


@app.get("/api/v1/dubladoras/", tags=["Geral"])
async def get_voice_actresses():
    """
    View para consultar as dubladoras. Retorna um dict com todos as dubladoras.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/dubladores/", tags=["Geral"])
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


@app.get("/api/v1/programas/", tags=["Geral"])
async def get_shows():
    """
    View para consultar os programas. Retorna um dict com todos os programas.
    """
    return {"Status": "Work in Progress"}
