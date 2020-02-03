from app import db, create_app
from app.config import app_config

app = create_app(app_config['dev'])


with app.app_context():
    db.drop_all()
    print("Droped db")
    db.create_all()
    print("Created db")
