"""Flask Configuration"""
from os import environ,path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KET')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI=environ.get('SQLALCHEMY_DATABASE_URI')

class DevConfig(Config):
    FLASK_ENV='development'
    DEBUG=True
    TESTING=True
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False


app_config = {
    'development':DevConfig,
    'production':ProdConfig
}