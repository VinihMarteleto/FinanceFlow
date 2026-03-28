from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from app.db.session import get_db
from app.models.account import Account, TipoConta
from app.core.security import get_current_user

router = APIRouter()


class ContaInput(BaseModel):
    nome: str
    tipo: TipoConta = TipoConta.corrente
    saldo_inicial: float = 0.0


class ContaResponse(BaseModel):
    id: int
    nome: str
    tipo: TipoConta
    saldo_inicial: float
    saldo: float
    model_config = {"from_attributes": True}


def buscar_conta(conta_id: int, usuario, db):
    conta = db.query(Account).filter(Account.id == conta_id, Account.usuario_id == usuario.id).first()
    if not conta:
        raise HTTPException(404, "Conta não encontrada")
    return conta


@router.post("", response_model=ContaResponse, status_code=201)
def criar_conta(dados: ContaInput, db=Depends(get_db), usuario=Depends(get_current_user)):
    conta = Account(usuario_id=usuario.id, nome=dados.nome, tipo=dados.tipo, saldo_inicial=dados.saldo_inicial)
    db.add(conta)
    db.commit()
    db.refresh(conta)
    return conta


@router.get("", response_model=List[ContaResponse])
def listar_contas(db=Depends(get_db), usuario=Depends(get_current_user)):
    return db.query(Account).filter(Account.usuario_id == usuario.id).all()


@router.get("/{conta_id}", response_model=ContaResponse)
def detalhar_conta(conta_id: int, db=Depends(get_db), usuario=Depends(get_current_user)):
    return buscar_conta(conta_id, usuario, db)


@router.patch("/{conta_id}", response_model=ContaResponse)
def atualizar_conta(conta_id: int, dados: ContaInput, db=Depends(get_db), usuario=Depends(get_current_user)):
    conta = buscar_conta(conta_id, usuario, db)
    conta.nome = dados.nome
    conta.tipo = dados.tipo
    db.commit()
    db.refresh(conta)
    return conta


@router.delete("/{conta_id}", status_code=204)
def excluir_conta(conta_id: int, db=Depends(get_db), usuario=Depends(get_current_user)):
    conta = buscar_conta(conta_id, usuario, db)
    db.delete(conta)
    db.commit()
