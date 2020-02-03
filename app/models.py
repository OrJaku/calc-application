from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    email = db.Column(db.Text())

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repl__(self):
        return f"User {self.name}"
