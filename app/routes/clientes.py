from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.clientes import Cliente as ClienteModel
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
    db = Depends(get_db)
):

    return cliente_service.criar_cliente(db, Session)

@router.get(
        "",
        response_model=list[ClienteResponse]
        )

def listar_clientes( 
    db = Depends(get_db)
):

    clientes = db.query(ClienteModel).all()

    return clientes


@router.get( "/{cliente_id}",
             response_model=ClienteResponse
               )
def buscar_cliente(
    cliente_id: int,
      db = Depends(get_db)
      ):
    
    cliente = db.query(ClienteModel).filter(
        ClienteModel.id == cliente_id
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    return cliente

@router.delete(
        "/{cliente_id}"
        )

def deletar_cliente(
    cliente_id: int,
    db = Depends(get_db)
):
    
    cliente = db.query(ClienteModel).filter(
        ClienteModel.id == cliente_id
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    db.delete(cliente)
    db.commit()

    return {"mensagem": "Cliente excluído com sucesso!"}

@router.put(
        "/{cliente_id}",
        response_model=ClienteResponse
         )

def atualizar_cliente(
    cliente_id: int,
    cliente: ClienteCreate,
    db = Depends(get_db)
):
    
    cliente_existente = db.query(ClienteModel).filter(
        ClienteModel.id == cliente_id
    ).first()

    if cliente_existente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    cliente_existente.nome = cliente.nome
    cliente_existente.email = cliente.email
    cliente_existente.telefone = cliente.telefone

    db.commit()
    db.refresh(cliente_existente)

    return cliente_existente
