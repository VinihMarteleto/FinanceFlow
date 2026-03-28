from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import datetime
from app.db.session import get_db
from app.models.account import Account
from app.models.transaction import Transaction, TipoTransacao, CategoriaTransacao
from app.core.security import get_current_user

router = APIRouter()


class TransacaoInput(BaseModel):
    conta_id: int
    tipo: TipoTransacao
    categoria: CategoriaTransacao = CategoriaTransacao.outros
    valor: float
    descricao: str
    notas: Optional[str] = None
    data: Optional[datetime] = None

    @field_validator("valor")
    @classmethod
    def validar_valor(cls, v):
        if v <= 0:
            raise ValueError("Valor deve ser maior que zero")
        return v


class TransacaoResponse(BaseModel):
    id: int
    conta_id: int
    tipo: TipoTransacao
    categoria: CategoriaTransacao
    valor: float
    descricao: str
    notas: Optional[str]
    data: datetime
    model_config = {"from_attributes": True}


class ListaTransacoes(BaseModel):
    total: int
    itens: List[TransacaoResponse]


def ids_contas_usuario(usuario, db):
    return [c.id for c in db.query(Account).filter(Account.usuario_id == usuario.id).all()]


@router.post("", response_model=TransacaoResponse, status_code=201)
def criar_transacao(dados: TransacaoInput, db=Depends(get_db), usuario=Depends(get_current_user)):
    ids = ids_contas_usuario(usuario, db)
    if dados.conta_id not in ids:
        raise HTTPException(404, "Conta não encontrada")
    conta = db.query(Account).filter(Account.id == dados.conta_id).first()
    if dados.tipo == TipoTransacao.despesa and conta.saldo - dados.valor < 0:
        raise HTTPException(422, f"Saldo insuficiente. Saldo atual: R$ {conta.saldo:.2f}")
    t = Transaction(
        conta_id=dados.conta_id, tipo=dados.tipo, categoria=dados.categoria,
        valor=dados.valor, descricao=dados.descricao, notas=dados.notas,
        data=dados.data or datetime.utcnow()
    )
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


@router.get("", response_model=ListaTransacoes)
def listar_transacoes(
    conta_id: Optional[int] = None,
    tipo: Optional[TipoTransacao] = None,
    categoria: Optional[CategoriaTransacao] = None,
    pagina: int = Query(1, ge=1),
    limite: int = Query(20, ge=1, le=100),
    db=Depends(get_db), usuario=Depends(get_current_user)
):
    ids = ids_contas_usuario(usuario, db)
    q = db.query(Transaction).filter(Transaction.conta_id.in_(ids))
    if conta_id:
        if conta_id not in ids:
            raise HTTPException(403, "Acesso negado")
        q = q.filter(Transaction.conta_id == conta_id)
    if tipo:
        q = q.filter(Transaction.tipo == tipo)
    if categoria:
        q = q.filter(Transaction.categoria == categoria)
    total = q.count()
    itens = q.order_by(Transaction.data.desc()).offset((pagina - 1) * limite).limit(limite).all()
    return {"total": total, "itens": itens}


@router.delete("/{transacao_id}", status_code=204)
def excluir_transacao(transacao_id: int, db=Depends(get_db), usuario=Depends(get_current_user)):
    ids = ids_contas_usuario(usuario, db)
    t = db.query(Transaction).filter(Transaction.id == transacao_id, Transaction.conta_id.in_(ids)).first()
    if not t:
        raise HTTPException(404, "Transação não encontrada")
    db.delete(t)
    db.commit()
