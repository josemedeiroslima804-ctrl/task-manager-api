from pydantic import BaseModel
from pydantic import ConfigDict

class ProdutoSchema(BaseModel):
    nome: str
    preco: float
    estoque: int
    
class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    estoque: int

    model_config = ConfigDict(from_attributes= True)    