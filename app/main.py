from fastapi import FastAPI

from app.database import Base, engine

from app.routes.produtos import router as produtos_router
from app.routes.clientes import router as clientes_router
from app.routes.pedidos import router as pedidos_router
from app.models.usuarios import Usuario
from app.routes.usuarios import router as usuarios_router

app = FastAPI(
    title="Sistema de Padaria",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(produtos_router)
app.include_router(clientes_router)
app.include_router(pedidos_router)
app.include_router(usuarios_router)

@app.get("/")
def home():
    return {"message": "Olá, mundo!"}


@app.get("/")
def sobre():
    return {
        "projeto": "Sistema de Padaria",
        "autor": "José Augusto Medeiros de Lima"
    }
