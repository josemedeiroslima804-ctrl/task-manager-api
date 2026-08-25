from fastapi import APIRouter, HTTPException, Depends
from app.dependencies import get_db

from app.models.pedidos import Pedido as PedidoModel
from app.models.clientes import Cliente as ClienteModel
from app.models.produto import Produto as ProdutoModel
from app.services import pedidos as pedido_service

from app.schemas.pedidos import ( PedidoCreate, PedidoResponse, PedidoDetalhado)

from sqlalchemy.orm import Session, joinedload   

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router.post(
    "",
    response_model=PedidoResponse,
    status_code=201
)
def criar_pedido(
    pedido: PedidoCreate,
    db: Session = Depends(get_db)
):
    return pedido_service.criar_pedido(db, Session)

#Lista Pedidos

@router.get(
        "",
        response_model=list[PedidoDetalhado]
        )
def listar_pedidos(
    db: Session = Depends(get_db)
):
    pedidos = db.query(PedidoModel).options(
        joinedload(PedidoModel.cliente),
        joinedload(PedidoModel.produto)
    ).all()

    return pedido_service.listar_pedidos(db)

#Busca Pedido

@router.get("/{pedido_id}",
            response_model=PedidoResponse
            )

def buscar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    return pedido_service.buscar_pedido(db, pedido_id)

#Deleta Pedido

@router.delete("/{pedido_id}")
def deletar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    return pedido_service.deletar_pedido(db, pedido_id)
