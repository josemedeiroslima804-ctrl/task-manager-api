from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: float
    estoque: int