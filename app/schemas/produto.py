from pydantic import BaseModel, ConfigDict

# Dados que o cliente envia para criar um produto.
class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    estoque: int

#Os dados que a API devolve.    
class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    estoque: int

#converte automaticamente um objeto do SQLAlchemy
    model_config = ConfigDict(from_attributes= True)    