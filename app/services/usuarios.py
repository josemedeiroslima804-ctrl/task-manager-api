from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.models.usuarios import Usuario as UsuarioModel
from app.schemas.usuarios import Token, UsuarioCreate
from app.security import create_access_token, hash_password, verify_password

def criar_usuario(
        db: Session,
        usuario: UsuarioCreate
) -> UsuarioCreate:
    
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

def login(
    db: Session,
    form_data: OAuth2PasswordRequestForm
):
    usuario = db.query(UsuarioModel).filter(
        UsuarioModel.email == form_data.username
    ).first()

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

    access_token = create_access_token(
        data={"sub": usuario.email}
    )

    return Token(
        access_token=access_token,
        token_type="bearer"
    )

def listar_usuarios(
    db: Session):
    
    usuarios = db.query(UsuarioModel).all()

    return usuarios

