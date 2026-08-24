from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user

from app.models.usuarios import Usuario as UsuarioModel
from app.schemas.usuarios import UsuarioCreate, UsuarioResponse

from app.services import usuarios as usuario_service

from fastapi.security import OAuth2PasswordRequestForm

from app.security import (
    verify_password,
    create_access_token
)

from app.schemas.usuarios import Token

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post("/", response_model=UsuarioResponse, 
             status_code=201)

def criar_usuario(
    usuario: UsuarioCreate,
    db: Session =Depends(get_db)
    ):

    return usuario_service.criar_usuario(db, usuario)

@router.post("/login",
              response_model=Token
              )

def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
      db: Session = Depends(get_db)
      ):
    return usuario_service.login(db,form_data)

@router.get(
    "",
    response_model=list[UsuarioResponse]
)

def listar_usuarios(
    db: Session = Depends(get_db)
    ):
    return usuario_service.listar_usuarios(db)