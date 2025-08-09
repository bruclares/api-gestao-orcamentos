# API de Gestão de Orçamentos e Propostas para Freelancers

**Status: Em desenvolvimento**

### Descrição

API RESTful desenvolvida em Flask para gerenciamento completo de orçamentos e propostas para freelancers.
Permite CRUD de clientes, propostas, geração de PDFs, autenticação JWT, e integração com fila para tarefas assíncronas.


### Qual problema este projeto resolve?

Freelancers autônomos (principalmente na área criativa ou técnica) enfrentam dificuldades para:

- Controlar versões de propostas enviadas a diferentes clientes
- Armazenar os dados de forma segura
- Gerar documentos de forma rápida e padronizada
- Automatizar envios ou lembretes sem depender de plataformas pagas


### Qual a solução proposta?

Uma **API RESTful** organizada em arquitetura limpa (MVC), que oferece:

- Autenticação via JWT
- Cadastro e gerenciamento de clientes e propostas
- Geração automática de PDFs com design limpo
- Envio de e-mails com as propostas anexadas
- Tarefas assíncronas com Celery e Redis
- Documentação automática com Swagger (via Flasgger)

### Tecnologias e Ferramentas Planejadas

| Camada | Ferramentas / Bibliotecas |
|--------|-----------------------------|
| Backend | Python + Flask |
| Autenticação | JWT (Flask-JWT-Extended) |
| Banco de Dados | PostgreSQL (via SQLAlchemy) |
| Testes | Pytest |
| Documentação | Flasgger |
| Mail | Flask-Mail (para envio de propostas por e-mail) |
| Background tasks | Celery + Redis |
| PDF Generator | WeasyPrint (para geração de orçamentos em PDF) |
| Containerização | Docker |

### Escolhas técnicas (em construção)

- **PostgreSQL** foi escolhido por sua robustez e familiaridade prévia (já utilizado em outros projetos).
- **SQLAlchemy** como ORM para facilitar abstração das queries e permitir futura troca de banco se necessário.
- **Arquitetura com Blueprints** para manter modularidade e separação de responsabilidades.
- **JWT** para autenticação segura, evitando sessions em APIs REST.
- **Celery** e **Redis** pensados desde o início para suportar tarefas como agendamento de envio de propostas e geração de PDF sem travar a API.

### O que quero aprender com esse projeto

- Estruturar APIs REST com Flask de forma modular e escalável
- Dominar o fluxo de autenticação com JWT
- Trabalhar com tarefas assíncronas e filas (Celery/Redis)
- Criar e enviar PDFs dinamicamente por e-mail
- Escrever testes automatizados com Pytest
- Documentar APIs com Swagger (via Flasgger)
- Criar e utilizar containers com Docker


### Visão futura

- Construção de um frontend com React e Tailwind
- Adição de dashboards com visualização de propostas enviadas e taxa de conversão
- Interface adaptada para freelancers de diferentes nichos (designers, devs, fotógrafos, etc.)

### Como rodar localmente

### Pré-requisitos

- Python 3.11+
- Redis rodando localmente (ou via Docker)
- (Opcional) Docker e Docker Compose para ambiente isolado

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/bruclares/api-gestao-orcamentos.git
   cd api-gestao-orcamentos

2. Crie e ative um ambiente virtual:
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/WSL
    venv\Scripts\activate     # Windows PowerShell

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt

4. Configure variáveis de ambiente no arquivo .env (exemplo abaixo):
    ```bash
    FLASK_APP=run.py
    FLASK_ENV=development
    SECRET_KEY=uma_chave_secreta
    JWT_SECRET_KEY=uma_chave_jwt
    MAIL_SERVER=smtp.exemplo.com
    MAIL_USERNAME=seu_email@exemplo.com
    MAIL_PASSWORD=sua_senha
    REDIS_URL=redis://localhost:6379/0

5. Inicie o Redis (localmente ou via Docker):
    ```bash
    redis-server

6. Rode a aplicação:
    ```bash
    flask run

### Rodando com Docker
(Em construção)

### Documentação da API
Será gerada automaticamente com Flasgger e estará disponível em breve

### Como contribuir
+ Faça um fork do projeto

+ Crie uma branch com a feature: git checkout -b minha-feature

+ Commit suas mudanças: git commit -m "feat: descrição da feature"

+ Faça push para sua branch: git push origin minha-feature

+ Abra um Pull Request
