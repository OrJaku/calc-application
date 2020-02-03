from flask import Blueprint, render_template, request
from ..forms import RegisterForm
from ..models import User
from .. import db

main = Blueprint('main', __name__, template_folder='templates')
@main.route('/')
def home():
    return render_template("home.html")


@main.route('/chat_room', methods=["POST", "GET"])
def chat_room():

    return render_template("chat_room.html")


@main.route('/register', methods=["POST"])
def register():
    name = request.form['name']
    email = request.form['email']
    user = User(name=name,
                email=email)
    db.session.add(user)
    db.session.commit()
    print("Registered successfully")

    return render_template("chat_room.html")
