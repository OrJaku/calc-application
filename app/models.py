from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.Text(40))

    def __repl__(self):
        return f"User {self.name}"


class Equation(db.Model):
    __tablename__ = "equation"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(10))


    def __repl__(self):
        return f"Image ID{self.id} Predict:{self.predict}"