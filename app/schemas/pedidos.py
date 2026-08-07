from pydantic import BaseModel, ConfigDict

class PedidoSchema(BaseModel):
    cliente_id: int
    produto_id: int
    quantidade: int

class PedidoResponse(BaseModel):
    id: int
    cliente_id: int
    produto_id: int
    quantidade: int

    model_config = ConfigDict(from_attributes=True)