from fastapi import APIRouter, HTTPException, Depends
from app.dependencies import get_db

from app.models.clientes import Cliente as ClienteModel
from app.schemas.clientes import ClienteCreate, ClienteResponse

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.post(
        "",
        response_model=ClienteResponse,
        status_code=201
        )
def novo_cliente(
    cliente: ClienteCreate,
    db = Depends(get_db)
):

    novo_cliente = ClienteModel(
        nome=cliente.nome,
        email=cliente.email,
        telefone=cliente.telefone
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)


    return novo_cliente

@router.get(
        "",
        response_model=list[ClienteResponse]
        )

def listar_clientes( 
    db = Depends(get_db)
):

    clientes = db.query(ClienteModel).all()

    return clientes
