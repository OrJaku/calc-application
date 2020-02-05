from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models import User
from .. import db

main = Blueprint('main', __name__, template_folder='templates')
@main.route('/')
def home():
    return render_template("home.html")


@main.route('/chat_room', methods=["POST", "GET"])
def chat_room():
    userlist = db.session.query(User.name).all()
    return render_template("chat_room.html", userlist=userlist)


@main.route('/register', methods=["POST"])
def register():
    nickname = request.form['name']
    email = request.form['email']
    get_user = User.query.filter_by(name=nickname).first()
    user_name = get_user.name
    user_email = get_user.email
    if nickname == user_name or email == user_email:
        flash("This email or nick name is already use in chat")
    else:
        user = User(name=nickname,
                    email=email)
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully")
    return redirect(url_for('main.chat_room'))
