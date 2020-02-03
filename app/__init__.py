import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


def create_app(app_config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(app_config)
    db.init_app(app)

    from .main import views
    app.register_blueprint(views.main)

    return app
