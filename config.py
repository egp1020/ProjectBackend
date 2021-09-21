import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "contraseina"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT=True
    DEBUG = True

currentDirectory = os.getcwd()
DATABASE_NAME = "src/database/tables.db"
SQLALCHEMY_DATABASE_URI = "sqlite://"+currentDirectory+DATABASE_NAME