from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.session import Base


class TipoConta(str, enum.Enum):
    corrente = "corrente"
    poupanca = "poupanca"
    carteira = "carteira"
    salario = "salario"


class Account(Base):
    __tablename__ = "contas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    nome = Column(String(100), nullable=False)
    tipo = Column(Enum(TipoConta), nullable=False, default=TipoConta.corrente)
    saldo_inicial = Column(Numeric(15, 2), default=0.00)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    usuario = relationship("User", back_populates="contas")
    transacoes = relationship("Transaction", back_populates="conta", cascade="all, delete-orphan")

    @property
    def saldo(self):
        total = float(self.saldo_inicial or 0)
        for t in self.transacoes:
            total += float(t.valor) if t.tipo == "receita" else -float(t.valor)
        return round(total, 2)
