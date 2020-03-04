from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models import User
from ..ml_model import prediction
import tempfile
import os
from .. import db

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    return render_template("home.html")


@main.route('/chat_room', methods=["POST", "GET"])
def chat_room():
    user_list = db.session.query(User.name).all()
    user_list =([x[0] for x in user_list])
    return render_template("chat_room.html", userlist=user_list)


@main.route('/register', methods=["POST"])
def register():
    nickname = request.form['name']
    email = request.form['email']
    try:
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
    except AttributeError:
        user = User(name=nickname,
                    email=email)
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully")
    return redirect(url_for('main.chat_room'))


@main.route('/writing')
def writing():
    return render_template("sheet.html")


@main.route('/image', methods=["POST"])
def image():
    data = request.json
    print(data)

    img_path = data.get('img_path')
    print(img_path)

    r = request.get(img_path)
    print(r)

    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, 'w') as f:
        f.write(img)

    new_file, filename = tempfile.mkstemp()
    print(filename)
    os.close(new_file)
    print("TEST", img)
    return render_template("sheet.html")
