# 🚀 API de Gestão de Orçamentos para Freelancers

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-336791?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Engine-2496ED?style=for-the-badge&logo=docker)

## 📋 Sobre o Projeto

API RESTful desenvolvida para resolver a dor de freelancers na gestão de propostas comerciais. O sistema permite o cadastro de clientes, geração de orçamentos em PDF e envio automático por e-mail, utilizando uma arquitetura moderna e assíncrona.

### 🛠️ Tech Stack

- **Linguagem:** Python 3.12
- **Framework:** FastAPI
- **Banco de Dados:** PostgreSQL (Neon Serverless)
- **ORM:** SQLAlchemy (Async)
- **Filas/Async:** Celery + Redis
- **Infra:** Docker Engine + WSL

## 🏗️ Arquitetura e Design Patterns

O projeto segue os princípios da **Clean Architecture**, adaptada para o contexto de microframeworks (FastAPI). Utilizamos o padrão **Service-Repository** para garantir o desacoplamento entre as camadas de roteamento, regras de negócio e persistência de dados.

A estrutura de pastas reflete essa organização:

- **api/** (Controller): Camada de entrada, responsável apenas por receber requisições e retornar respostas.
- **schemas/** (DTOs): Pydantic models para validação e serialização de dados (Input/Output).
- **services/** (Business Logic): Onde vive o coração da aplicação. Regras de negócio puras, agnósticas ao banco de dados ou framework web.
- **models/** (Data Layer): Definição das tabelas do banco de dados (SQLAlchemy).
- **core/**: Configurações globais e segurança.

## ⚙️ Configuração do Ambiente (Dev)

### Pré-requisitos
- Python 3.12+
- Gerenciador de pacotes `pip`
- Docker Engine (opcional para rodar o Redis localmente)

### 🚀 Instalação

1. Clone o repositório:
```bash
git clone [https://github.com/bruclares/api-gestao-orcamentos.git](https://github.com/bruclares/api-gestao-orcamentos.git)
cd api-gestao-orcamentos
```
2. Crie e ative o ambiente virtual:
```bash
python3.12 -m venv venv
source venv/bin/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Configure as variáveis de ambiente:
- Duplique o arquivo .env.example para .env (vamos criar isso em breve!)
- Preencha as chaves de acesso.

### 🏃‍♂️ Como Rodar
```bash
uvicorn app.main:app --reload
```

Desenvolvido por Bruna Clares.


