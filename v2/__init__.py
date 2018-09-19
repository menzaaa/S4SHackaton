import os

from flask import Flask

from v2.settings import DevConfig
from v2.extentions import db, migrate

from v2.api import api_blueprint

Config = DevConfig

def create_app(config_object=Config):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''

    app = Flask(__name__)
    app.config.from_object(config_object)

    #opbeat?

    register_extentions(app)
    register_blueprints(app)

    return app

def register_extentions(app):
    db.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    app.register_blueprint(api_blueprint)