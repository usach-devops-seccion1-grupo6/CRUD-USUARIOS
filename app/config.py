import os


class Config:
    """Parametros base para configuración desde variables de entorno"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    PROPAGATE_EXCEPTIONS = os.getenv('PROPAGATE_EXCEPTIONS')

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SHOW_SQLALCHEMY_LOG_MESSAGES = os.getenv('SHOW_SQLALCHEMY_LOG_MESSAGES')
    ERROR_404_HELP = os.getenv('ERROR_404_HELP')


class Production(Config):
    """Parametros para ambiente de produccion"""


class Development(Config):
    """Parametros para ambiente de desarrollo"""
    DEBUG = True


class Testing(Config):
    """Parametros para ambiente de testing"""
    TESTING = True
