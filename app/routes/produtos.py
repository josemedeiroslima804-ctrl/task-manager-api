from fastapi import APIRouter, Depends
from app.dependencies import get_db, get_current_user

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

def deletar_produtos(
    produto_id: int,
    db = Depends(get_db),
    usuario_atual= Depends(get_current_user)
):

    return produto_service.deletar_produto(
        db,
        produto_id
    )


#atualizar produto


@router.put("/{produto_id}",
            response_model= ProdutoResponse
            )

def atualizar_produto(
    produto_id: int,
    produto: ProdutoCreate,
    db = Depends(get_db),
    usuario_atual= Depends(get_current_user) 
 ):

    return produto_service.atualizar_produto(
        db,
        produto_id,
        produto
    )