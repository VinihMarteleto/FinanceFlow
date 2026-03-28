from fastapi import APIRouter, Depends, Query
from sqlalchemy import extract
from app.db.session import get_db
from app.models.account import Account
from app.models.transaction import Transaction, TipoTransacao
from app.core.security import get_current_user

router = APIRouter()


@router.get("/resumo")
def resumo_mensal(
    ano: int = Query(...), mes: int = Query(..., ge=1, le=12),
    db=Depends(get_db), usuario=Depends(get_current_user)
):
    ids = [c.id for c in db.query(Account).filter(Account.usuario_id == usuario.id).all()]
    transacoes = db.query(Transaction).filter(
        Transaction.conta_id.in_(ids),
        extract("year", Transaction.data) == ano,
        extract("month", Transaction.data) == mes,
    ).all()
    receitas = sum(float(t.valor) for t in transacoes if t.tipo == TipoTransacao.receita)
    despesas = sum(float(t.valor) for t in transacoes if t.tipo == TipoTransacao.despesa)
    por_categoria = {}
    for t in transacoes:
        k = t.categoria.value
        if k not in por_categoria:
            por_categoria[k] = {"receitas": 0.0, "despesas": 0.0}
        if t.tipo == TipoTransacao.receita:
            por_categoria[k]["receitas"] += float(t.valor)
        else:
            por_categoria[k]["despesas"] += float(t.valor)
    return {
        "ano": ano, "mes": mes,
        "total_receitas": round(receitas, 2),
        "total_despesas": round(despesas, 2),
        "saldo_liquido": round(receitas - despesas, 2),
        "total_transacoes": len(transacoes),
        "por_categoria": por_categoria,
    }


@router.get("/saldos")
def saldos(db=Depends(get_db), usuario=Depends(get_current_user)):
    contas = db.query(Account).filter(Account.usuario_id == usuario.id).all()
    resultado = [{"id": c.id, "nome": c.nome, "tipo": c.tipo.value, "saldo": c.saldo} for c in contas]
    return {"contas": resultado, "saldo_total": round(sum(c["saldo"] for c in resultado), 2)}
