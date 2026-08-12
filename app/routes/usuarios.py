from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_db
from app.security import hash_password

from app.models.usuarios import Usuario as UsuarioModel
from app.schemas.usuarios import UsuarioCreate, UsuarioResponse

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

def criar_usuario(usuario: UsuarioCreate, db=Depends(get_db)):
    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).first()

    if usuario_existente:
        raise HTTPException(status_code=400,
                             detail="Email já cadastrado")

    novo_usuario = UsuarioModel(
        nome=usuario.nome,
        email=usuario.email,
        senha=hash_password(usuario.senha)
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

@router.post("/login",
              response_model=Token
              )
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
      db=Depends(get_db)
      ):

    usuario = db.query(UsuarioModel).filter(UsuarioModel.email == form_data.username).first()

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
            )

    if not verify_password(form_data.password, usuario.senha):
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
            )
    access_token = create_access_token(data={
        "sub": usuario.email}
        )

    return Token(
        access_token=access_token,
        token_type="bearer"
    )

