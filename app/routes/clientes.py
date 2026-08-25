from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.schemas.clientes import ClienteCreate, ClienteResponse
from app.services import clientes as cliente_service

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.post(
        "",
        response_model=ClienteResponse,
        status_code=201
        )

def criar_cliente(
    cliente: ClienteCreate,
    db: Session = Depends(get_db),
    usuario_atual=Depends(get_current_user)
):

    return cliente_service.criar_cliente(db, cliente)

@router.get(
        "",
        response_model=list[ClienteResponse]
        )

def listar_clientes( 
    db = Depends(get_db),
    usuario_atual=Depends(get_current_user)
):

    return cliente_service.listar_clientes(db)


@router.get( "/{cliente_id}",
             response_model=ClienteResponse
               )
def buscar_cliente(cliente_id:int,
                   db: Session = Depends(get_db),
                   usuario_atual = Depends(get_current_user)
                   ):
    
    return cliente_service.buscar_cliente(db,cliente_id)

@router.delete(
        "/{cliente_id}"
        )

def deletar_cliente(
    cliente_id: int,
    db : Session = Depends(get_db),
    usuario_atual=Depends(get_current_user)
):
    return cliente_service.deletar_cliente(db, cliente_id)

@router.put(
        "/{cliente_id}",
        response_model=ClienteResponse
         )

def atualizar_cliente(
    cliente_id: int,
    cliente: ClienteCreate,
    db: Session = Depends(get_db),
    usuario_atual = Depends(get_current_user)
):
    return cliente_service.atualizar_cliente(db,cliente_id, cliente)
