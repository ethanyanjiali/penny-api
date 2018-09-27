from datetime import timedelta


class BaseConfig:
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_PASSWORD_KEY = 'password'
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRATION_DELTA = timedelta(seconds=3600)
    PROJECT_ID = 'mypennyco'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    NAMESPACE = 'prod'
    PORT = 80


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    NAMESPACE = 'dev'
    PORT = 8000

