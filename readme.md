# 💰 FinanceFlow — Sistema Completo de Controle Financeiro

## 📌 Visão Geral

O **FinanceFlow** é uma aplicação full stack desenvolvida com o objetivo de fornecer um controle financeiro pessoal completo, moderno e intuitivo.

A proposta do sistema é permitir que o usuário tenha **visibilidade total sobre sua vida financeira**, organizando receitas, despesas e contas de forma centralizada.

O projeto simula uma aplicação real utilizada por fintechs, com foco em **usabilidade, performance e organização de dados**.

---

## 🎯 Objetivo do Projeto

O sistema foi desenvolvido com os seguintes objetivos:

* Criar uma aplicação real de mercado para portfólio
* Aplicar conceitos de desenvolvimento full stack
* Trabalhar com arquitetura organizada (backend + frontend)
* Implementar autenticação segura com JWT
* Desenvolver uma interface moderna estilo SaaS

---

## 🧠 Proposta da Solução

Diferente de sistemas simples de controle financeiro, o FinanceFlow adota uma abordagem mais estratégica:

1. O usuário registra sua renda (salário)
2. Registra suas despesas ao longo do mês
3. O sistema calcula automaticamente:

   * Total de gastos
   * Saldo disponível
   * Possível economia

Essa abordagem permite uma análise mais realista e prática da vida financeira.

---

## 🏗️ Arquitetura do Sistema

O projeto segue uma arquitetura **Full Stack desacoplada**, composta por:

### 🔹 Backend (API REST)

Responsável por:

* Regras de negócio
* Processamento de dados
* Autenticação
* Persistência em banco de dados

### 🔹 Frontend (Client)

Responsável por:

* Interface do usuário
* Consumo da API
* Renderização dos dados

---

## 🧰 Tecnologias Utilizadas

### 🔙 Backend

* **Python**
* **FastAPI** → Framework moderno para APIs
* **SQLite** → Banco de dados leve e eficiente
* **JWT (JSON Web Token)** → Autenticação segura

### 🎨 Frontend

* **HTML5**
* **CSS3 (Custom Design System)**
* **JavaScript (Vanilla JS)**

### ⚙️ Ferramentas

* Git & GitHub
* Uvicorn (servidor ASGI)

---

## 🔐 Segurança

O sistema implementa autenticação baseada em **JWT**, garantindo:

* Proteção de rotas privadas
* Sessão persistente no frontend
* Controle de acesso por usuário

---

## 🚀 Funcionalidades Implementadas

### 🔐 Autenticação

* Cadastro de usuários
* Login com validação
* Geração de token JWT

---

### 💳 Gestão de Contas

* Criação de contas financeiras
* Tipos suportados:

  * Conta corrente
  * Poupança
  * Carteira
* Controle de saldo individual

---

### 💸 Transações

* Registro de receitas e despesas
* Classificação por categoria
* Associação com contas
* Exclusão de registros

---

### 📊 Dashboard

* Saldo total consolidado
* Receitas do mês
* Despesas do mês
* Saldo líquido
* Listagem de transações recentes

---

### 📈 Relatórios

* Resumo financeiro mensal
* Total de receitas e despesas
* Quantidade de transações
* Análise por categoria com barras proporcionais

---

## 🎨 Experiência do Usuário (UX/UI)

O frontend foi desenvolvido com foco em:

* Interface moderna estilo SaaS
* Navegação lateral intuitiva
* Feedback visual em tempo real:

  * Toast notifications
  * Skeleton loading
  * Loading progress bar
* Design inspirado em plataformas como Spotify

---

## 📡 Comunicação Frontend ↔ Backend

A comunicação é feita via **requisições HTTP (REST API)**:

* JSON como formato padrão
* Autenticação via header:

```http
Authorization: Bearer <token>
```

---

## 📊 Estrutura de Dados

O sistema trabalha com entidades principais:

* Usuário
* Conta
* Transação
* Relatórios (dados agregados)

---

## ⚙️ Execução do Projeto

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

---

### Frontend

Abrir o arquivo:

```bash
frontend/index.html
```

---

## 🧪 Testes da API

Documentação automática disponível via Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Possíveis Evoluções

* Integração com APIs bancárias (Open Banking)
* Gráficos interativos (Chart.js)
* Versão mobile responsiva
* Deploy em nuvem (AWS / Vercel / Railway)
* Upload de comprovantes
* Inteligência artificial para categorização automática

---

## 👨‍💻 Autor

**Vinicius Gonçalves Marteleto**

---

## 🧾 Conclusão

O FinanceFlow é um projeto completo que demonstra:

* Conhecimento em backend com APIs modernas
* Integração com frontend
* Aplicação de autenticação segura
* Organização de código em arquitetura real
* Criação de interfaces modernas e funcionais

👉 Projeto ideal para demonstrar capacidade técnica em vagas de desenvolvimento.
