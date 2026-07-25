from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: float
    estoque: int
from fastapi import FastAPI
from schemas.produto import Produto

app = FastAPI()


@app.post("/produtos")
def criar_produto(produto: Produto):
    return {
        "mensagem": f"Produto {produto.nome} cadastrado com sucesso!"
    }