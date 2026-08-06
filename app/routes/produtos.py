from fastapi import APIRouter, HTTPException, Depends
from app.dependencies import get_db

from app.models.produto import Produto as ProdutoModel
from app.schemas.produto import ProdutoCreate, ProdutoResponse

router = APIRouter()

@router.post(
        "/produtos",
        response_model=ProdutoResponse,
        status_code=201
        )
def criar_produto(
    produto: ProdutoCreate,
    db = Depends(get_db)
):

    novo_produto = ProdutoModel(
        nome=produto.nome,
        preco=produto.preco,
        estoque=produto.estoque
    )

# Marca o objeto para ser inserido no banco
    db.add(novo_produto)

# Confirma a transação e grava o produto no banco
    db.commit()

# Atualiza o objeto com o ID gerado pelo banco
    db.refresh(novo_produto)


    return novo_produto

@router.get(
        "/produtos",
        response_model=list[ProdutoResponse]
        )

def listar_produtos( 
    db = Depends(get_db)
):

    produtos = db.query(ProdutoModel).all()

    return produtos


""" Filtro de Produtos """


@router.get("/produtos/{produto_id}",
            response_model=ProdutoResponse
            )

def buscar_produto(produto_id : int,
                   db = Depends(get_db)):


    produto = db.query(ProdutoModel).filter(
        ProdutoModel.id == produto_id
    ).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail= "Produto não encontrado"
            )

    return produto


""" O código abaixo serve para deletar produtos """


@router.delete ("/produtos/{produto_id}",
                status_code=204
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


@router.put("/produtos/{produto_id}",
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