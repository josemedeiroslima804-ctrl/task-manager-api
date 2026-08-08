from app.database import SessionLocal

def get_db():

    db = SessionLocal()

    try:
        
        yield db #confirma se pode estabelecer da conexão

    finally: #executa independente de erro
        db.close