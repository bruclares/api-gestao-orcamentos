from typing import Any
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id: Any
    __name__: str

    #gera __tablename__ automaticamente pelo nome da classe
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # __repr__ para todos os models
    def __repr__(self):
        cols = []
        # tenta pegar as colunas na tabela
        if hasattr(self, "__table__"):
            for col in self.__table__.columns.keys():
                # filtra só o que interessa 
                if col in ['id', 'email', 'is_active', 'title', 'full_name']:
                    cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__}({', '.join(cols)})>"
