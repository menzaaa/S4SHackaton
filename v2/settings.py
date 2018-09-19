import os

DB_URI='mysql+pymysql://root:mysql@localhost/hackathon'

class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__)) # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    ERROR_404_HELP = False

class DevConfig(Config):
    """Dev configuration"""
    ENV = 'prod'
    DEBUG = False
    DB_NAME = 'hackathon'
    DB_USER = 'root'
    DB_PASSWORD = 'admin'
    DB_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
