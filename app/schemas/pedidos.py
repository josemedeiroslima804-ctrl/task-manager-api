from pydantic import BaseModel, ConfigDict

class PedidoCreate(BaseModel):

    cliente_id: int
    produto_id: int
    quantidade: int

class PedidoResponse(BaseModel):

    id: int
    cliente_id: int
    produto_id: int
    quantidade: int

    model_config = ConfigDict(from_attributes=True)

class ClienteResumo(BaseModel):

    id: int
    nome: str

    model_config = ConfigDict(from_attributes=True)

class ProdutoResumo(BaseModel):

    id: int
    nome: str

    model_config = ConfigDict(from_attributes=True)

class PedidoDetalhado(BaseModel):

    id: int
    cliente: ClienteResumo
    produto: ProdutoResumo
    quantidade: int

    model_config = ConfigDict(from_attributes=True)