# 🥖 Sistema de Padaria API

API REST desenvolvida em **Python** com **FastAPI** para gerenciamento de uma padaria.

Este projeto foi desenvolvido com o objetivo de praticar conceitos de desenvolvimento Back-end, arquitetura em camadas, autenticação com JWT e integração com banco de dados PostgreSQL.

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

---

## 📂 Estrutura do projeto

```
app/
│
├── models/          # Modelos do banco de dados
├── schemas/         # Schemas do Pydantic
├── routes/          # Rotas da API
├── services/        # Regras de negócio
│
├── database.py
├── dependencies.py
├── security.py
└── main.py
```

---

## 🔐 Autenticação

A API utiliza autenticação baseada em **JWT**.

Fluxo:

1. Criar um usuário
2. Fazer login
3. Receber um Access Token
4. Utilizar o token no botão **Authorize** do Swagger
5. Acessar os endpoints protegidos

---

## 📦 Funcionalidades

### Usuários

- Criar usuário
- Login com JWT
- Listar usuários

### Produtos

- Criar produto
- Listar produtos
- Buscar produto
- Atualizar produto
- Excluir produto

### Clientes

- Criar cliente
- Listar clientes
- Buscar cliente
- Atualizar cliente
- Excluir cliente

### Pedidos

- Criar pedido
- Listar pedidos
- Buscar pedido
- Excluir pedido
- Controle automático de estoque

---

## 🗄️ Banco de Dados

O projeto utiliza PostgreSQL.

As tabelas são criadas automaticamente pelo SQLAlchemy na primeira execução.

---

## ▶️ Como executar

### Clone o projeto

```bash
git clone https://github.com/josemedeiroslima804/task-manager-api.git
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

Execute a aplicação

```bash
uvicorn app.main:app --reload
```

---

## 📖 Documentação

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 🧠 Conceitos praticados

- Arquitetura em camadas
- CRUD completo
- Relacionamentos com SQLAlchemy
- Injeção de dependências
- Autenticação JWT
- Hash de senhas
- Services (camada de regras de negócio)
- Validação com Pydantic
- Organização de projeto FastAPI

---

## 📌 Próximas melhorias

- Testes automatizados
- Docker
- Alembic para migrações
- Variáveis de ambiente (.env)
- CI/CD com GitHub Actions
- Deploy em nuvem

---

## 👨‍💻 Autor

José Augusto Medeiros de Lima

Projeto desenvolvido para estudos e composição de portfólio Back-end.