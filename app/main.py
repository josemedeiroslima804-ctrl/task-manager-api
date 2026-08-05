from fastapi import FastAPI

from app.database import engine
from app.models.produto import Base
from app.routes.produtos import router as produtos_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(produtos_router)


@app.get("/")
def home():
    return {"message": "Olá, mundo!"}


@app.get("/sobre")
def sobre():
    return {
        "projeto": "Sistema de Padaria",
        "autor": "José Augusto Medeiros de Lima"
    }
