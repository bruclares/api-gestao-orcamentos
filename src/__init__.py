import os

from flasgger import Swagger
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Importa o dicionário de configurações que criamos no config.py
from src.config import config_by_name

# -----------------------------------------------------------------------------
# INSTANCIAÇÃO DAS EXTENSÕES
# -----------------------------------------------------------------------------
# Instâncias "vazias" das extensões, prontas para serem
# conectadas à aplicação dentro da fábrica.
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()
swagger = Swagger()


# -----------------------------------------------------------------------------
# FÁBRICA DE APLICAÇÃO (APPLICATION FACTORY)
# -----------------------------------------------------------------------------
def create_app():
    """
    Esta é a função principal que constrói e configura a aplicação Flask.
    """
    # Cria a instância principal da aplicação Flask
    # '__name__' diz ao Flask para procurar templates e arquivos estáticos
    # no diretório onde etse arquivo está
    app = Flask(__name__)

    # -------------------------------------------------------------------------
    # CONFIGURAÇÃO DA APLICAÇÃO
    # -------------------------------------------------------------------------
    # Pega o nome do ambiente da variável de ambiente FLASK_ENV
    # Se não encontrar, usa 'default' (que aponta para DevelopmentConfig)
    env_name = os.getenv("FLASK_ENV", "default")
    # Carrega as configurações da classe correspondente de uma só vez.
    app.config.from_object(config_by_name[env_name])

    # -------------------------------------------------------------------------
    # INICIALIZAÇÃO DAS EXTENSÕES COM A APLICAÇÃO
    # -------------------------------------------------------------------------
    # O método .init_app() conecta as extensões à
    # aplicação (app), usando as configurações que acabou de carregar
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)
    swagger.init_app(app)

    # -------------------------------------------------------------------------
    # REGISTRO DAS BLUEPRINTS (ROTAS)
    # -------------------------------------------------------------------------
    # Aqui é onde voi conectar os diferentes módulos da API
    # (autenticação, clientes, propostas, etc.) à aplicação principal.
    # Exemplo de como será:
    # from .routes.auth_routes import auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')

    # -------------------------------------------------------------------------
    # ROTA DE TESTE
    # -------------------------------------------------------------------------
    # Uma rota simples para verificar se a aplicação está rodando.
    @app.route("/health")
    def health_check():
        return {"status": "ok", "message": "API is healthy"}, 200

    return app
