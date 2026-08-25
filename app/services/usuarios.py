from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.models.usuarios import Usuario as UsuarioModel
from app.schemas.usuarios import Token, UsuarioCreate
from app.security import create_access_token, hash_password, verify_password

def criar_usuario(
    db: Session,
    usuario: UsuarioCreate
):

    usuario_existente = db.query(UsuarioModel).filter(
        UsuarioModel.email == usuario.email
    ).first()

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

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

    senha_valida = verify_password(
        form_data.password,
        usuario.senha
    )

    if not senha_valida:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    access_token = create_access_token(
        data={
            "sub": usuario.email
        }
    )

    return Token(
        access_token=access_token,
        token_type="bearer"
    )


def listar_usuarios(
    db: Session
):

    return db.query(UsuarioModel).all()


def buscar_usuario(
    db: Session,
    usuario_id: int
):

    usuario = db.query(UsuarioModel).filter(
        UsuarioModel.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return usuario


def atualizar_usuario(
    db: Session,
    usuario_id: int,
    usuario: UsuarioCreate
):

    usuario_db = db.query(UsuarioModel).filter(
        UsuarioModel.id == usuario_id
    ).first()

    if usuario_db is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )


    usuario_db.nome = usuario.nome
    usuario_db.email = usuario.email

    # Atualiza senha somente se for enviada
    if usuario.senha:
        usuario_db.senha = hash_password(usuario.senha)


    db.commit()
    db.refresh(usuario_db)

    return usuario_db


def deletar_usuario(
    db: Session,
    usuario_id: int
):

    usuario = db.query(UsuarioModel).filter(
        UsuarioModel.id == usuario_id
    ).first()


    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )


    db.delete(usuario)
    db.commit()


    return {
        "Mensagem": "Usuário excluído com sucesso!"
    }

