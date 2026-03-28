from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from app.db.session import get_db
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token, get_current_user

router = APIRouter()


class RegistroInput(BaseModel):
    nome: str
    email: EmailStr
    senha: str


class LoginInput(BaseModel):
    email: EmailStr
    senha: str


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    usuario: UsuarioResponse


@router.post("/registrar", response_model=UsuarioResponse, status_code=201)
def registrar(dados: RegistroInput, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == dados.email).first():
        raise HTTPException(400, "E-mail já cadastrado")
    usuario = User(nome=dados.nome, email=dados.email, senha_hash=hash_password(dados.senha))
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


@router.post("/login", response_model=TokenResponse)
def login(dados: LoginInput, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.email == dados.email, User.ativo == True).first()
    if not usuario or not verify_password(dados.senha, usuario.senha_hash):
        raise HTTPException(401, "E-mail ou senha incorretos")
    return {
        "access_token": create_access_token(usuario.id),
        "refresh_token": create_refresh_token(usuario.id),
        "usuario": usuario
    }


@router.get("/me", response_model=UsuarioResponse)
def me(usuario=Depends(get_current_user)):
    return usuario
