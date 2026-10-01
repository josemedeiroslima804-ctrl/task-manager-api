# 🥖 Sistema de Padaria API

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)

API REST desenvolvida em **Python** utilizando **FastAPI** para gerenciamento de uma padaria.

O projeto foi criado com foco em estudos de desenvolvimento Back-end, aplicando conceitos de arquitetura em camadas, autenticação com JWT, banco de dados relacional e boas práticas de organização de código.

---

## 🚀 Tecnologias utilizadas

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn
- python-dotenv

---

## 📂 Estrutura do projeto

```text
app/
├── models/
├── routes/
├── schemas/
├── services/
├── database.py
├── dependencies.py
├── security.py
└── main.py
```

---

## 📌 Funcionalidades

### 👤 Usuários

![Login](images/swagger-login.png)

- Cadastro de usuários
- Login com JWT
- Senhas criptografadas com bcrypt
- Rotas protegidas por autenticação

### 📦 Produtos

![Produtos](images/swagger-produtos.png)

- Criar produtos
- Listar produtos
- Buscar produto por ID
- Atualizar produto
- Excluir produto

### 👥 Clientes

![Clientes](images/swagger-clientes.png)

- Criar clientes
- Listar clientes
- Buscar cliente por ID
- Atualizar cliente
- Excluir cliente

### 🛒 Pedidos

![Pedidos](images/swagger-pedidos.png)

- Criar pedidos
- Listar pedidos
- Buscar pedido
- Excluir pedido
- Verificação de estoque
- Relacionamento entre clientes e produtos

---

## 🔐 Segurança

O projeto utiliza:

- Hash de senhas com bcrypt
- Autenticação JWT
- Variáveis de ambiente (.env)
- Proteção das rotas por Token Bearer

---

## ⚙️ Como executar

Clone o projeto

```bash
git clone https://github.com/josemedeiroslima804-ctrl/task-manager-api.git
```

Entre na pasta

```bash
cd task-manager-api
```

Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env`

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/padaria_db
SECRET_KEY=sua_chave_secreta
```

Execute a aplicação

```bash
uvicorn app.main:app --reload
```

---

## 📖 Documentação

Após iniciar a aplicação:

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 🎯 Objetivo

Este projeto foi desenvolvido com o objetivo de praticar:

- Desenvolvimento de APIs REST
- Organização de projetos em camadas
- SQLAlchemy
- PostgreSQL
- Autenticação JWT
- Relacionamentos entre tabelas
- Boas práticas de Back-end

---

## 👨‍💻 Autor

José Augusto Medeiros de Lima

GitHub:
https://github.com/josemedeiroslima804-ctrl

LinkedIn:
https://www.linkedin.com/in/jos%C3%A9-augusto-medeiros/?isSelfProfile=true