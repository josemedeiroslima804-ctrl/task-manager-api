from fastapi import APIRouter, Depends

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user

from app.schemas.usuarios import (
    UsuarioCreate,
    UsuarioResponse,
    Token
)

from app.services import usuarios as usuario_service


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)



@router.post(
    "/",
    response_model=UsuarioResponse,
    status_code=201
)
def criar_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):

    return usuario_service.criar_usuario(
        db,
        usuario
    )



@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    return usuario_service.login(
        db,
        form_data
    )



@router.get(
    "/",
    response_model=list[UsuarioResponse]
)
def listar_usuarios(
    db: Session = Depends(get_db),
    usuario_atual = Depends(get_current_user)
):

    return usuario_service.listar_usuarios(db)



@router.get(
    "/{usuario_id}",
    response_model=UsuarioResponse
)
def buscar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    usuario_atual = Depends(get_current_user)
):

    return usuario_service.buscar_usuario(
        db,
        usuario_id
    )



@router.put(
    "/{usuario_id}",
    response_model=UsuarioResponse
)
def atualizar_usuario(
    usuario_id: int,
    usuario: UsuarioCreate,
    db: Session = Depends(get_db),
    usuario_atual = Depends(get_current_user)
):

    return usuario_service.atualizar_usuario(
        db,
        usuario_id,
        usuario
    )



@router.delete(
    "/{usuario_id}"
)
def deletar_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    usuario_atual = Depends(get_current_user)
):

    return usuario_service.deletar_usuario(
        db,
        usuario_id
    )