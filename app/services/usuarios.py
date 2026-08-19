from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.usuarios import Usuario as UsuarioModel
from app.schemas.usuarios import UsuarioCreate
from app.security import hash_password

