from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_db
from app.security import hash_password

from app.models.usuarios import Usuario as UsuarioModel
from app.schemas.usuarios import UsuarioCreate, UsuarioResponse

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