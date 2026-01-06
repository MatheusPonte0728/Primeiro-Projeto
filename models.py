from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Cliente(Base):
    __tablename__ = "clientes"  # Nome da Tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)  # CPF deve ser único
    email = Column(String, unique=True, index=True)  # Email deve ser unico
    limite_credito = Column(Float, default=0.0)
    ativo = Column(Boolean, default=True)
    