import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from keras.models import model_from_json
from keras.datasets import mnist
from keras.utils import to_categorical, plot_model


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

data_path = os.path.join(basedir, 'data')


train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype("float32") / 255
test_images = train_images.reshape((60000, 28*28))
test_images = train_images.astype("float32") / 255
print("TEST", test_labels[2])
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
print(test_labels.shape)
with open('data/model_config.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('data/model_mnist.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam')

plot_model(model, to_file='model.png')

# loss_acc = model.evaluate(test_images, test_labels)
# print('loss= ', loss_acc[0])
# print("acc= ", loss_acc[1])

predicted_classes = model.predict_classes(test_images)
print(predicted_classes[2])
db = SQLAlchemy()


def create_app(app_config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(app_config)
    db.init_app(app)

    from .main import views
    app.register_blueprint(views.main)

    return app
