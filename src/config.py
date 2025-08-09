import os


class Config:
    """
    Configuração base que contém as configurações comuns a todos os ambientes.
    Outras classes de configuração herdarão desta.
    """

    # Chaves secretas para segurança
    SECRET_KEY = os.getenv("SECRET_KEY", "uma_chave_secreta_padrao_para_dev")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "uma_chave_jwt_padrao_para_dev")

    # Configuração para o banco de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações do Flask-Mail
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() in ["true", "1", "t"]
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")


class DevelopmentConfig(Config):
    """Configurações para o ambiente de desenvolvimento."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # Em desenvolvimento, você pode querer ver as queries SQL geradas
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    """Configurações para o ambiente de testes."""

    TESTING = True
    # Para testes, é comum usar um banco de dados separado ou em memória
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")
    # Desativa a proteção CSRF em testes para simplificar as requisições
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Configurações para o ambiente de produção."""

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # Em produção, nunca mostre as queries SQL
    SQLALCHEMY_ECHO = False


# Dicionário para mapear os nomes dos ambientes às suas classes de configuração
config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
