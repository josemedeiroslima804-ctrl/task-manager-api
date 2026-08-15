from fastapi import APIRouter, HTTPException, Depends
from app.dependencies import get_db, get_current_user

from app.models.produto import Produto as ProdutoModel
from app.schemas.produto import ProdutoCreate, ProdutoResponse
from app.services import produtos as produto_service

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.post(
        "",
        response_model=ProdutoResponse,
        status_code=201
        )

def criar_produto(
    produto: ProdutoCreate,
    db=Depends(get_db),
    usuario_atual=Depends(get_current_user)
):

    return produto_service.criar_produto(
        db,
        produto
    )

@router.get(
        "",
        response_model=list[ProdutoResponse]
        )

def listar_produtos( 
    db = Depends(get_db),
    usuario_atual =Depends(get_current_user)
):
    

    return produto_service.listar_produtos(db)


# Busca um Produto


@router.get(
    "/{produto_id}",
    response_model=ProdutoResponse
)
def buscar_produto(
    produto_id: int,
    db=Depends(get_db),
    usuario_atual=Depends(get_current_user)
):

    return produto_service.buscar_produto(
        db,
        produto_id
    )


# Deleta um Produto


@router.delete ("/{produto_id}",
                
                )

def deletar_produtos(produto_id: int,
                     db = Depends(get_db) ):

    produto = db.query(ProdutoModel).filter(
        ProdutoModel.id == produto_id
    ).first()

    if produto is None:
            raise HTTPException(
                status_code=404,
                detail= "Produto não encontrado"
                )

    db.delete(produto)
    db.commit()


    return {"mensagem": "Produto excluído com sucesso!"}


""" Função para atualizar produtos"""


@router.put("/{produto_id}",
            response_model= ProdutoResponse
            )

def atualizar_produto(produto_id: int, produto: ProdutoCreate,
                      db = Depends(get_db) ):

    

    produto_db = db.query(ProdutoModel).filter(
        ProdutoModel.id == produto_id
    ).first()

    if produto_db is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    produto_db.nome = produto.nome
    produto_db.preco = produto.preco
    produto_db.estoque = produto.estoque

    db.commit()
    db.refresh(produto_db)


    return produto_db