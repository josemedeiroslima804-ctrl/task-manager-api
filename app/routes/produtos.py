from fastapi import APIRouter, HTTPException

from app.database import SessionLocal
from app.models.produto import Produto as ProdutoModel
from app.schemas.produto import ProdutoSchema

router = APIRouter()

@router.post(
        "/produtos",
        response_model=ProdutoSchema,
        status_code=201
        )
def criar_produto(produto: ProdutoSchema):

#Abre a conexão com o banco
    db = SessionLocal()

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

# Fecha a conexão com o banco
    db.close()

    return novo_produto

@router.get("/produtos")
def listar_produtos():

    db = SessionLocal()

    produtos = db.query(ProdutoModel).all()

    db.close()

    return produtos

""" Filtro de Produtos """

@router.get("/produtos/{produto_id}")
def buscar_produto(produto_id : int) :

    db = SessionLocal()

    produto = db.query(ProdutoModel).filter(
        ProdutoModel.id == produto_id
    ).first()

    db.close()

    return produto

""" O código abaixo serve para deletar produtos """

@router.delete ("/produtos/{produto_id}")
def deletar_produtos(produto_id: int):

    db = SessionLocal()

    produto = db.query(ProdutoModel).filter(
        ProdutoModel.id == produto_id
    ).first()

    db.delete(produto)
    db.commit()

    db.close()

    return {"mensagem": "Produto excluído com sucesso!"}

""" Função para atualizar produtos"""

@router.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, produto: ProdutoSchema):

    db = SessionLocal()

    produto_db = db.query(ProdutoModel).filter(
        ProdutoModel.id == produto_id
    ).first()

    if produto_db is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    produto_db.nome = produto.nome
    produto_db.preco = produto.preco
    produto_db.estoque = produto.estoque

    db.commit()
    db.refresh(produto_db)

    db.close()

    return produto_db