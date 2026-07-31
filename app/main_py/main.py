from fastapi import FastAPI

from schemas.produto import Produto as ProdutoSchema
from models.produto import Produto as ProdutoModel

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API Sistema de Padaria"}


@app.get("/sobre")
def sobre():
    return {
        "projeto": "Sistema de Padaria",
        "autor": "José Augusto Medeiros de Lima"
    }


produtos = [
    {
        "id": 1,
        "nome": "Pão Francês",
        "preco": 0.80
    },
    {
        "id": 2,
        "nome": "Sonho",
        "preco": 6.50
    }
]


@app.get("/produtos")
def listar_produtos():
    return produtos


@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):

    for produto in produtos:
        if produto["id"] == produto_id:
            return produto

    return {"erro": "Produto não encontrado"}


@app.post("/produtos")
def criar_produto(produto: ProdutoSchema):

    novo_produto = ProdutoModel(
        nome=produto.nome,
        preco=produto.preco,
        estoque=produto.estoque
    )

    return {
        "mensagem": f"Produto {novo_produto.nome} cadastrado com sucesso!"
    }
from database import engine
from models.produto import base

app =FastAPI()

Base.metadata.create_all(bind=engine)
