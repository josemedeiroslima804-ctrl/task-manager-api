from fastapi import APIRouter, HTTPException, Depends
from app.dependencies import get_db

from app.models.pedidos import Pedido as PedidoModel
from app.models.clientes import Cliente as ClienteModel
from app.models.produto import Produto as ProdutoModel

from app.schemas.pedidos import ( PedidoCreate, PedidoResponse, PedidoDetalhado)

from sqlalchemy.orm import joinedload   

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

@router.post(
    "",
    response_model=PedidoResponse,
    status_code=201
)
def novo_pedido(
    pedido: PedidoCreate,
    db = Depends(get_db)
):

    # Verifica se o cliente existe
    cliente = db.query(ClienteModel).filter(
        ClienteModel.id == pedido.cliente_id
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    # Verifica se o produto existe
    produto = db.query(ProdutoModel).filter(
        ProdutoModel.id == pedido.produto_id
    ).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )
    #Verifica o estoque
    if produto.estoque < pedido.quantidade:
        raise HTTPException(
            status_code=400,
            detail="Estoque insuficiente."
        )

    # Cria o pedido
    novo_pedido = PedidoModel(
        cliente_id=pedido.cliente_id,
        produto_id=pedido.produto_id,
        quantidade=pedido.quantidade
    )
    #Atualiza o estoque
    produto.estoque -= pedido.quantidade 

    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)

    return novo_pedido

#Lista Pedidos

@router.get(
        "",
        response_model=list[PedidoDetalhado]
        )
def listar_pedidos(
    db = Depends(get_db)
):
    pedidos = db.query(PedidoModel).options(
        joinedload(PedidoModel.cliente),
        joinedload(PedidoModel.produto)
    ).all()

    return pedidos

#Busca Pedido

@router.get("/{pedido_id}",
            response_model=PedidoResponse
            )

def buscar_pedido(
    pedido_id: int,
    db = Depends(get_db)
):
    
    pedido = db.query(PedidoModel).filter(
        PedidoModel.id == pedido_id
    ).first()

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado."
        )

    return pedido

#Deleta Pedido

@router.delete("/{pedido_id}")
def deletar_pedido(
    pedido_id: int,
    db = Depends(get_db)
):
    
    pedido = db.query(PedidoModel).filter(
        PedidoModel.id == pedido_id
    ).first()

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado."
        )

    db.delete(pedido)
    db.commit()

    return {"mensagem": "Pedido excluído com sucesso!"}
