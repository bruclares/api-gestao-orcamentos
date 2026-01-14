from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def get_user_by_email(db: Session, email:str):
    """Busca um usuário pelo email (para verificar duplicidade)"""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    """Cria um novo usuário no banco com senha criptografada"""
    # criptografa a senha
    hashed_password = get_password_hash(user.password)

    # cria o objeto user no banco 
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        is_active=True
    )

    # adiciona e salva
    db.add(db_user)
    db.commit()
    db.refresh(db.user) # recarrega para pegar i ID gerado e datas

    return db_user