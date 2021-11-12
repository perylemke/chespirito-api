from typing import List
from pydantic import BaseModel, Field


# Ator e Atriz
class Actor(BaseModel):
    id: int = Field(..., alias='_id')
    nome: str = Field(...)
    nome_artistico: str = None
    data_nascimento: str = Field(...)
    data_falecimento: str = None
    programas: List[str] = Field(...)
    personagens: List[str] = Field(...)


# Dubladores e Dubladoras
class VoiceActor(BaseModel):
    id: int = Field(..., alias='_id')
    nome: str = Field(...)
    data_nascimento: str = Field(...)
    data_falecimento: str = Field(...)
    estudio: List[str] = Field(...)
    personagens: List[str] = Field(...)


# Episódios
class Episode(BaseModel):
    id: int = Field(..., alias='_id')
    ano_exibicao: int = Field(...)
    titulo: str = Field(...)
    situacao_mexico: str = Field(...)
    estreia_mexico: str = Field(...)
    quadros: List[dict] = Field(...)


# Frases
class Quote(BaseModel):
    id: int = Field(..., alias='_id')
    frase: str = Field(...)
    personagem: str = Field(...)


# Personagens
class Character(BaseModel):
    id: int = Field(..., alias='_id')
    nome: str = Field(...)
    nome_original: str = Field(...)
    programa: str = Field(...)
    apelidos: List[str] = Field(...)
    idade: int = Field(...)
    genero: str = Field(...)
    oficios: List[str] = Field(...)
    frases: List[str] = Field(...)
    casa: int
    primeira_aparicao: str = Field(...)
    ultima_aparicao: str = Field(...)
    dubladores: List[str] = Field(...)
    ator_atriz: str = Field(...)


# Programas
class Show(BaseModel):
    id: int = Field(..., alias='_id')
    nome: str = Field(...)
    nome_original: str = Field(...)
    primeiro_ano: int = Field(...)
    ultimo_ano: int = Field(...)
    primeiro_episodio: str = Field(...)
    ultimo_episodio: str = Field(...)
    total_temporadas: int = Field(...)
    estudio_dublagem: List[str] = Field(...)
