from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.session import Base


class TipoTransacao(str, enum.Enum):
    receita = "receita"
    despesa = "despesa"


class CategoriaTransacao(str, enum.Enum):
    salario = "salario"
    freelance = "freelance"
    investimento = "investimento"
    alimentacao = "alimentacao"
    transporte = "transporte"
    saude = "saude"
    educacao = "educacao"
    lazer = "lazer"
    contas = "contas"
    outros = "outros"


class Transaction(Base):
    __tablename__ = "transacoes"
    id = Column(Integer, primary_key=True, index=True)
    conta_id = Column(Integer, ForeignKey("contas.id"), nullable=False)
    tipo = Column(Enum(TipoTransacao), nullable=False)
    categoria = Column(Enum(CategoriaTransacao), nullable=False, default=CategoriaTransacao.outros)
    valor = Column(Numeric(15, 2), nullable=False)
    descricao = Column(String(255), nullable=False)
    notas = Column(Text, nullable=True)
    data = Column(DateTime(timezone=True), server_default=func.now())
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    conta = relationship("Account", back_populates="transacoes")
