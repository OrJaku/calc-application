from app import create_app 
from app.config import app_config


app = create_app(app_config['dev'])


if __name__ == "__main__":
    app.run()