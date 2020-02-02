from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates')
@main.route('/')
def home():
    return render_template("home.html")


@main.route('/chat_room')
def chat_room():
    return render_template("chat_room.html")
