from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.produto import Produto as ProdutoModel
from app.schemas.produto import ProdutoCreate

def criar_produto(
        db: Session,
        produto: ProdutoCreate
        ):

    novo_produto = ProdutoModel(
        nome=produto.nome,
        preco=produto.preco,
        estoque=produto.estoque
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto

def listar_produtos(db: Session):

    produtos = db.query(ProdutoModel).all()

    return produtos

def buscar_produto(db: Session, produto_id: int):

    produto = db.query(ProdutoModel).filter(
        ProdutoModel.id == produto_id
    ).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return produto