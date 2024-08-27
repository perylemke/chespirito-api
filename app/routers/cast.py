from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from app.db import DB_CAST
from app.schemas import Actor

router = APIRouter()


@router.get(
    '/api/elenco', status_code=HTTPStatus.OK, response_model=list[Actor]
)
@router.get(
    '/api/elenco/', status_code=HTTPStatus.OK, response_model=list[Actor]
)
def get_cast():
    return DB_CAST


@router.get(
    '/api/elenco/{id}', status_code=HTTPStatus.OK, response_model=Actor
)
@router.get(
    '/api/elenco/{id}/', status_code=HTTPStatus.OK, response_model=Actor
)
def get_actor(id: int):
    actor = next(
        (actor for actor in DB_CAST if actor['_id'] == id),
        None,
    )
    if actor is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Ator não encontrado.',
        )
    return actor
