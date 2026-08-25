from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_current_user

from app.services import pedidos as pedido_service

from app.schemas.pedidos import ( PedidoCreate, PedidoResponse, PedidoDetalhado)

from sqlalchemy.orm import Session  

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
    db: Session = Depends(get_db),
    usuario_atual= Depends(get_current_user)
):
    return pedido_service.criar_pedido(db, pedido)

#Lista Pedidos

@router.get(
        "",
        response_model=list[PedidoDetalhado]
        )
def listar_pedidos(
    db: Session = Depends(get_db),
    usuario_atual=Depends(get_current_user)
):

    return pedido_service.listar_pedidos(db)

#Busca Pedido

@router.get("/{pedido_id}",
            response_model=PedidoResponse
            )

def buscar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db),
    usuario_atual=Depends(get_current_user)
):
    return pedido_service.buscar_pedido(db, pedido_id)

#Deleta Pedido

@router.delete("/{pedido_id}")
def deletar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db),
    usuario_atual=Depends(get_current_user)
):
    return pedido_service.deletar_pedido(db, pedido_id)
