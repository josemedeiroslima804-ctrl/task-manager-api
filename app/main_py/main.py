from fastapi import FastAPI
from schemas.produto import Produto

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

# Lista temporária (depois será substituída pelo PostgreSQL)
produtos = [
    {
        "id": 1,
        "nome": "pão francês",
        "preco": 0.80
    },
    {
        "id": 2,
        "nome": "sonho",
        "preco": 6.50
    }
]

@app.get("/produtos")
def lista_produtos():
    return produtos

@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto

    return {"erro": "Produto não encontrado"}

@app.post("/produtos")
def criar_produto(produto: Produto):
    return {
        "mensagem": f"Produto {produto.nome} cadastrado com sucesso!"
    }