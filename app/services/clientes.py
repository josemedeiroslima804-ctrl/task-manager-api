from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.clientes import Cliente as ClienteModel
from app.schemas.clientes import ClienteCreate


def criar_cliente(
    db: Session,
    cliente: ClienteCreate
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

def listar_clientes( 
    db: Session
):
    return db.query(ClienteModel).all()

def buscar_cliente(
    db: Session,
    cliente_id: int
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

def deletar_cliente(
    db: Session,
    cliente_id: int
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

def atualizar_cliente(
    db: Session,
    cliente_id: int,
    cliente: ClienteCreate
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