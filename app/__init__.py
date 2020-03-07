from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


def create_app(app_config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(app_config)
    db.init_app(app)

    from .main import views
    app.register_blueprint(views.main)

    return app


def find_last_image():
    path_in_app = "captured_image"
    path_to_image = os.path.join(basedir, path_in_app)
    files_list = os.listdir(path_to_image)
    latest_file = max(files_list)
    path_to_latest_file = os.path.join(path_to_image, latest_file)
    return path_to_latest_file, files_list, latest_file
