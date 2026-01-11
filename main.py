from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import SessionLocal, engine

# 1. Cria as tabelas no banco de dados automaticamente


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 2. Dependência para pegar a sessão do banco


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Garante que a conexão feche, evitando travamentos

# --- ENDPOINTS ---

# POST: Criar Cliente


@app.post(
    "/clientes/",
    response_model=schemas.ClienteResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_cliente(
    cliente: schemas.ClienteCreate,
    db: Session = Depends(get_db)
):
    # Verifica se já existe cliente com este CPF

    cliente_existente = db.query(models.Cliente).filter(
        models.Cliente.cpf == cliente.cpf
    ).first()
    if cliente_existente:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")

    # Cria o objeto do modelo

    novo_cliente = models.Cliente(
        nome=cliente.nome,
        cpf=cliente.cpf,
        email=cliente.email,
        limite_credito=cliente.limite_credito,
        ativo=cliente.ativo
    )
    db.add(novo_cliente)  # Adiciona na sessão
    db.commit()           # Salva no banco (efetiva a transação)
    db.refresh(novo_cliente)  # Atualiza o objeto com o ID gerado pelo banco
    return novo_cliente

# GET: Listar todos os clientes


@app.get("/clientes/", response_model=List[schemas.ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).all()
    return clientes

# GET: Buscar cliente por ID


@app.get("/clientes/{cliente_id}", response_model=schemas.ClienteResponse)
def buscar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

# PUT: Atualizar dados do cliente


@app.put("/clientes/{cliente_id}", response_model=schemas.ClienteResponse)
def atualizar_cliente(
    cliente_id: int,
    cliente_atualizado: schemas.ClienteCreate,
    db: Session = Depends(get_db)
):
    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id).first()
    if not cliente_db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    # Atualiza os campos

    cliente_db.nome = cliente_atualizado.nome
    cliente_db.email = cliente_atualizado.email
    cliente_db.limite_credito = cliente_atualizado.limite_credito
    cliente_db.ativo = cliente_atualizado.ativo
    # Nota: CPF geralmente não se muda, mas pode ser incluído se
    # quiser logicamente

    db.commit()
    db.refresh(cliente_db)
    return cliente_db

# DELETE: Remover cliente


@app.delete("/clientes/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_db = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id).first()
    if not cliente_db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db.delete(cliente_db)
    db.commit()
    return None
