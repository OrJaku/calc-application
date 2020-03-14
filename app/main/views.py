from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models import User, Equation
from ..ml_model import prediction
from app import basedir, find_last_image
import sqlalchemy.exc
import numpy as np
from .. import db
from PIL import Image
import urllib.request
import os
import time

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
    data = request.form['img']
    img = Image.open(urllib.request.urlopen(data))
    result = prediction(img)
    predict = result[0][0]
    filtered_image = result[2]
    img_name = time.strftime("%Y%m%d-%H%M%S")
    img_name = "".join([img_name, "_", str(predict), ".jpg"])
    try:
        path_image = "/".join([basedir, "captured_image", img_name])
        filtered_image.save(path_image)
    except FileNotFoundError:
        info = "Files problem"
        return render_template("sheet.html", predict=predict, info=info)
    predict = int(predict)

    value_db = Equation(value=predict)
    db.session.add(value_db)
    db.session.commit()
    values = get_db_values()
    value_1 = values[0]
    value_2 = values[1]
    sign = values[2]

    return render_template("sheet.html", value=predict, sign=sign, value_1=value_1, value_2=value_2)


@main.route('/buttons', methods=["POST"])
def buttons():
    result = None
    values = get_db_values()
    value_1 = values[0]
    value_2 = values[1]

    if "plus" in request.form:
        data = request.form['plus']
        sign = "+"
        sign_db = Equation(value=sign)
        db.session.add(sign_db)
        db.session.commit()
    elif "minus" in request.form:
        data = request.form['minus']
        sign = "-"
        sign_db = Equation(value=sign)
        db.session.add(sign_db)
        db.session.commit()
    elif "multi" in request.form:
        data = request.form['multi']
        sign = "*"
        sign_db = Equation(value=sign)
        db.session.add(sign_db)
        db.session.commit()
    elif "divis" in request.form:
        data = request.form['divis']
        sign = "/"
        sign_db = Equation(value=sign)
        db.session.add(sign_db)
        db.session.commit()
    elif "equate" in request.form:
        data = request.form['equate']
        sign = values[2]
        Equation.query.delete()
        db.session.commit()
        if sign == "+":
            result = int(value_1) + int(value_2)
        elif sign == "-":
            result = int(value_1) - int(value_2)
        elif sign == "*":
            result = int(value_1) * int(value_2)
        elif sign == "/":
            print("va1", value_1)
            print("va2", value_2)
            print("si", sign)
            if value_2 == "0":
                result = "You can not division by 0"
            else:
                result = int(value_1) / int(value_2)
        else:
            result = "Incorrect"
    else:
        data = None
        sign = "Incorrect"

    return render_template("sheet.html", value=sign, result=result, sign=sign, value_1=value_1, value_2=value_2)


@main.route('/clear_equation', methods=["POST"])
def clear_equation():
    Equation.query.delete()
    db.session.commit()
    return render_template("sheet.html")


@main.route('/delete_image', methods=["POST"])
def delete_image():
    path_to_latest_file = find_last_image()
    os.remove(path_to_latest_file[0])

    labels_list = []
    for img in path_to_latest_file[1]:
        lbl = img[-5]
        labels_list.append(lbl)
    i = 0
    count_labels = {}
    while i != 10:
        count = labels_list.count(str(i))
        count_labels[i] = count
        i += 1
    Equation.query.delete()
    db.session.commit()
    print(count_labels)
    return render_template("sheet.html", latest_file=path_to_latest_file[2])


def get_db_values():
    values_from_db = db.session.query(Equation.value).all()
    values_from_db_list = list(values_from_db)
    values_from_db_list = ([x[0] for x in values_from_db_list])
    try:
        value_1 = values_from_db_list[0]
    except IndexError:
        value_1 = None
    try:
        value_2 = values_from_db_list[2]
    except IndexError:
        value_2 = None
    try:
        sign = values_from_db_list[1]
    except IndexError:
        sign = None
    return value_1, value_2, sign
