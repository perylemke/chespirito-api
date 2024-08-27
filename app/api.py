from http import HTTPStatus

from fastapi import FastAPI

from app.config import API_URL
from app.routers import cast

app = FastAPI()

app.include_router(cast.router)


@app.get('/api', status_code=HTTPStatus.OK)
@app.get('/api/', status_code=HTTPStatus.OK)
def home():
    return {
        'Geral': {
            'Elenco': f'{API_URL}/api/elenco/',
            'Dublagem': f'{API_URL}/api/dublagem/',
        },
    }
