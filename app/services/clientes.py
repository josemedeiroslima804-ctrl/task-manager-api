from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.clientes import Cliente as ClienteModel
from app.schemas.clientes import ClienteCreate


def criar_cliente(
    db: Session,
    cliente: ClienteCreate
):

    criar_cliente = ClienteModel(
        nome=cliente.nome,
        email=cliente.email,
        telefone=cliente.telefone
    )

    db.add(criar_cliente)
    db.commit()
    db.refresh(criar_cliente)


    return criar_cliente