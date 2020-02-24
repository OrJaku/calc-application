import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from keras.models import load_model, model_from_json


basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

data_path = os.path.join(basedir, 'data')

with open('data_path/model_config.json', 'r') as f:
    model = model_from_json(f.read())

model.load_weights('model_mnist.h5')

db = SQLAlchemy()


def create_app(app_config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(app_config)
    db.init_app(app)

    from .main import views
    app.register_blueprint(views.main)

    return app
