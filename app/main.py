from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/atores/")
def actors():
    """
    View para consultar os atores. Retorna um dict com todos os atores.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/atrizes/")
def actresses():
    """
    View para consultar as atrizes. Retorna um dict com todos as atrizes.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/casas/")
def houses():
    """
    View para consultar as casas. Retorna um dict com todos as casas.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/dubladoras/")
def voice_actresses():
    """
    View para consultar as dubladoras. Retorna um dict com todos as dubladoras.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/dubladores/")
def voice_actors():
    """
    View para consultar os dubladores. Retorna um dict com todos os dubladores.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/episodios/")
def episodes():
    """
    View para consultar os episódios. Retorna um dict com todos os episódios.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/estudios/")
def voice_studios():
    """
    View para consultar os estúdios de dublagem.
    Retorna um dict com todos os estúdios de dublagem.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/filmes/")
def movies():
    """
    View para consultar os filmes. Retorna um dict com todos os filmes.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/frases/")
def quotes():
    """
    View para consultar os frases. Retorna um dict com todos os frases.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/personagens/")
def character():
    """
    View para consultar os personagens.
    Retorna um dict com todos os personagens.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/programas/")
def shows():
    """
    View para consultar os programas. Retorna um dict com todos os programas.
    """
    return {"Status": "Work in Progress"}


@app.get("/api/v1/temporadas/")
def seasons():
    """
    View para consultar as temporadas. Retorna um dict com todos as temporadas.
    """
    return {"Status": "Work in Progress"}
