from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.Text(40))

    def __repl__(self):
        return f"User {self.name}"


class Images(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    array = db.Column(db.Text())
    predict = db.Column(db.Integer())

    def __repl__(self):
        return f"Image ID{self.id} Predict:{self.predict}"