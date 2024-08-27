from typing import List

from pydantic import BaseModel, Field


class Actor(BaseModel):
    id: int = Field(..., alias='_id')
    nome: str = Field(...)
    nome_artistico: str = None
    data_nascimento: str = Field(...)
    data_falecimento: str = None
    programas: List[str] = Field(...)
    personagens: List[str] = Field(...)
