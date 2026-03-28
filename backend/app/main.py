from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.api.v1.endpoints import auth, accounts, transactions, reports
from app.db.session import Base, engine

# Cria tabelas automaticamente ao iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FinanceFlow API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Autenticação"])
app.include_router(accounts.router, prefix="/api/v1/accounts", tags=["Contas"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["Transações"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Relatórios"])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(title=app.title, version=app.version, routes=app.routes)
    schema["components"]["securitySchemes"] = {
        "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }
    for path in schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = schema
    return schema

app.openapi = custom_openapi


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "message": "FinanceFlow API rodando!"}
