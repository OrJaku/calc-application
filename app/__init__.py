from flask import Flask, render_template


def create_app():
    app = Flask(__name__, template_folder='templates')
    from .main import views
    app.register_blueprint(views.main)
    return app