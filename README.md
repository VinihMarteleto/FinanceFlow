# 💰 FinanceFlow

> Plataforma completa de controle financeiro pessoal com dashboard inteligente, autentação segura e análise de dados em tempo real.

---

## 🎬 Demonstração

![Demo do sistema](./assets/demo.gif)

---

## 📌 Sobre o projeto

O **FinanceFlow** é uma aplicação full stack desenvolvida para fornecer uma experiência moderna de controle financeiro, permitindo que o usuário tenha **visão clara e controle total sobre seu dinheiro**.

A ideia do projeto é simular uma aplicação real do mercado financeiro, com foco em:

* Organização financeira mensal
* Visualização clara de dados
* Experiência de usuário moderna
* Backend estruturado e escalável

Sistemas desse tipo são amplamente usados hoje em fintechs para controle financeiro, análise de gastos e tomada de decisão. ([Finance Flow][1])

---

## 🚀 Principais funcionalidades

### 🔐 Autenticação

* Cadastro de usuário
* Login com JWT
* Proteção de rotas

---

### 💳 Gestão de contas

* Criação de contas financeiras
* Tipos:

  * Conta corrente
  * Poupança
  * Carteira
* Controle de saldo por conta

---

### 💸 Transações

* Registro de receitas e despesas
* Categorias personalizadas
* Filtros por:

  * Tipo
  * Categoria
  * Conta

---

### 📊 Dashboard inteligente

* Saldo total consolidado
* Receitas do mês
* Despesas do mês
* Saldo líquido
* Últimas transações

---

### 📈 Relatórios financeiros

* Resumo mensal
* Análise por categoria
* Visualização proporcional de gastos

---

## 🎨 Interface

* Design moderno estilo SaaS
* Inspirado em plataformas como Spotify
* Feedback visual com:

  * Toasts
  * Loading states
  * Skeleton loading
* Navegação lateral intuitiva

---

## 🧠 Diferencial do projeto

Diferente de apps comuns que apenas registram gastos, o FinanceFlow foi pensado para:

* Centralizar o salário primeiro
* Permitir análise mensal de despesas
* Ajudar o usuário a entender quanto pode economizar

Esse modelo segue práticas reais de organização financeira usadas em plataformas modernas. ([Finance Flow][2])

---

## 🏗️ Arquitetura

```bash
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
├── assets/
│   └── demo.gif
│
└── README.md
```

---

## 🖥️ Tecnologias utilizadas

### Backend:

* Python
* FastAPI
* SQLite
* Uvicorn

---

### Frontend:

* HTML
* CSS (custom)
* JavaScript Vanilla

---

## 🔐 Segurança

* Autenticação via JWT
* Rotas protegidas
* Validação de dados no backend

---

## ⚙️ Como rodar o projeto

### 🔹 Backend

```bash
cd backend

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload
```

---

### 🔹 Frontend

Abra:

```bash
frontend/index.html
```

ou utilize o Live Server.

---

## 🌐 API

Base URL:

```
http://localhost:8000/api/v1
```

---

## 📡 Endpoints principais

### 🔐 Auth

* POST /auth/login
* POST /auth/registrar

### 💳 Contas

* GET /accounts
* POST /accounts
* DELETE /accounts/{id}

### 💸 Transações

* GET /transactions
* POST /transactions
* DELETE /transactions/{id}

### 📊 Relatórios

* GET /reports/saldos
* GET /reports/resumo

---

## 🧪 Testes

Swagger disponível em:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Melhorias futuras

* Integração com bancos (Open Banking)
* Gráficos com Chart.js
* Responsividade mobile
* Deploy em nuvem
* Upload de imagem de comprovantes
* Inteligência artificial para categorização

---

## 👨‍💻 Autor

**Vinicius Marteleto**

* GitHub: https://github.com/VinihMarteleto

