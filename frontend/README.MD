# 💰 FinanceFlow

> Sistema completo de controle financeiro pessoal com dashboard interativo, autenticação segura e relatórios inteligentes.

---

## 📌 Visão Geral

O **FinanceFlow** é uma aplicação full stack desenvolvida para ajudar usuários a **organizar, visualizar e controlar suas finanças pessoais** de forma simples, moderna e eficiente.

O sistema foi projetado com foco em:

* Experiência do usuário (UI/UX)
* Organização financeira mensal
* Visualização clara de dados
* Arquitetura backend estruturada

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

* Praticar desenvolvimento **Full Stack**
* Criar uma **API REST profissional**
* Trabalhar com **autenticação segura (JWT)**
* Desenvolver um **frontend moderno estilo SaaS**
* Simular um sistema real de mercado

---

## 🚀 Funcionalidades

### 🔐 Autenticação

* Cadastro de usuário
* Login com validação
* Geração de token JWT
* Proteção de rotas privadas

---

### 💳 Contas

* Criar contas (ex: Nubank, Carteira, Banco)
* Tipos:

  * Conta corrente
  * Poupança
  * Carteira
* Visualização de saldo por conta
* Exclusão de contas

---

### 💸 Transações

* Registro de:

  * Receitas (entrada de dinheiro)
  * Despesas (saída de dinheiro)
* Campos:

  * Valor
  * Categoria
  * Descrição
  * Observações
* Filtros:

  * Tipo (receita/despesa)
  * Categoria
  * Conta

---

### 📊 Dashboard

* Saldo total
* Receitas do mês
* Despesas do mês
* Saldo líquido mensal
* Últimas transações

---

### 📈 Relatórios

* Resumo mensal por:

  * Receita
  * Despesa
  * Saldo
* Agrupamento por categoria
* Barras visuais de proporção

---

### 🎨 Interface (UI)

* Design moderno inspirado em SaaS (estilo Spotify)
* Feedback visual:

  * Toasts (mensagens)
  * Skeleton loading
  * Loading progress bar
* Navegação lateral
* Modais interativos

---

## 🧠 Arquitetura do Projeto

```
FinanceFlow/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   │
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
└── README.md
```

---

## 🖥️ Tecnologias Utilizadas

### Backend:

* Python
* FastAPI
* SQLite
* Uvicorn

### Frontend:

* HTML
* CSS (customizado)
* JavaScript Vanilla

---

## 🔐 Segurança

* Autenticação baseada em JWT
* Rotas protegidas via token
* Validação de dados no backend

---

## ⚙️ Como Executar o Projeto

---

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/VinihMarteleto/FinanceFlow.git
cd FinanceFlow
```

---

### 🔹 2. Backend

```bash
cd backend

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

📍 Backend rodando em:

```
http://127.0.0.1:8000
```

---

### 🔹 3. Frontend

Abra o arquivo:

```
frontend/index.html
```

OU use extensão **Live Server** no VS Code.

---

## 🌐 API

Base URL:

```
http://localhost:8000/api/v1
```

---

## 📡 Endpoints

### 🔐 Autenticação

* `POST /auth/login`
* `POST /auth/registrar`

---

### 💳 Contas

* `GET /accounts`
* `POST /accounts`
* `DELETE /accounts/{id}`

---

### 💸 Transações

* `GET /transactions`
* `POST /transactions`
* `DELETE /transactions/{id}`

---

### 📊 Relatórios

* `GET /reports/saldos`
* `GET /reports/resumo?ano=YYYY&mes=MM`

---

## 📸 Preview

> Adicione prints aqui

Exemplo:

```markdown
![Dashboard](./assets/dashboard.png)
```

---

## 🧪 Testes

Você pode testar a API via:

```
http://127.0.0.1:8000/docs
```

(Swagger automático do FastAPI)

---

## 💡 Melhorias Futuras

* Gráficos reais (Chart.js)
* Responsividade mobile
* Integração com bancos (Open Banking)
* Exportação em PDF
* Deploy online (Vercel + Render)
* Modo claro/escuro
* Upload de avatar

---

## 🧑‍💻 Autor

**Vinicius Marteleto**

* GitHub: https://github.com/VinihMarteleto

---

## 📄 Licença

Este projeto é de uso livre para estudos e portfólio.

---

## ⭐ Considerações Finais

Este projeto representa uma aplicação completa com:

* Backend estruturado
* Frontend funcional
* Boas práticas de desenvolvimento

Ideal para demonstrar habilidades em processos seletivos 🚀
