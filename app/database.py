from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:SUA_SENHA@localhost:5432/padaria_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)