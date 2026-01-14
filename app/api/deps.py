from typing import Generator
from app.db.session import SessionLocal

def get_db() -> Generator:
    """
    Cria uma sessão de banco de dados para cada requisição 
    e fecha ela automaticamente quando terminar.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        