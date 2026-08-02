from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Olá, mundo!"}


@app.get("/sobre")
def sobre():
    return {
        "projeto": "Sistema de Padaria",
        "autor": "José Augusto Medeiros de Lima"
    }