from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/atores/")
def actors():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/atrizes/")
def actresses():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/casas/")
def houses():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/dubladoras/")
def voice_actresses():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/dubladores/")
def voice_actors():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/episodios/")
def episodes():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/estudios/")
def voice_studios():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/filmes/")
def movies():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/frases/")
def quotes():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/personagens/")
def character():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/programas/")
def shows():
    return {"Status": "Work in Progress"}


@app.get("/api/v1/temporadas/")
def seasons():
    return {"Status": "Work in Progress"}
