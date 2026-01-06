from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Definimos o nome do banco de dados (sera um arquivo local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./clientes.db"

# 2. Criamos a "engine" que gerencia a comunicação com o banco
# connect_args={"check_same_thread": False} é nescesssario apenas para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Criamos a classe SessionLocal. Cada instância dela será uma sessão no banco.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 4. Base para cria os modelos (tabelas) depois
Base = declarative_base()
