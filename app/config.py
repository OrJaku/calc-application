import os
from app import basedir


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'Super_dsfsdsd44(*#&@(($##@++power_w3t(*#()_KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
                    basedir, "data.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'dev': DevelopmentConfig,
}
