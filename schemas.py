from pydantic import BaseModel
from typing import Optional

# Base para dados comuns
class ClienteBase(BaseModel):
    nome: str
    cpf: str
    email: str
    limite_credito: float
    ativo: bool = True

# Schema para CRIAÇÃO (o usuário envia isso)
class ClienteCreate(ClienteBase):
    pass

# Schema para LEITURA (a API retorna isso)
class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True
