from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.usuarios import Usuario as UsuarioModel
from app.security import decode_access_token

def get_db():

    db = SessionLocal()

    try:
        
        yield db

    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuarios/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido")

    email = payload.get("sub")

    if email is None:
        raise HTTPException(status_code=401, detail="Token inválido")

    usuario = db.query(UsuarioModel).filter(UsuarioModel.email == email).first()

 
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario
