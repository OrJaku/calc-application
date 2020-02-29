from keras.models import model_from_json

with open('data/model_config.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('data/model_mnist.h5')


def prediction(digit):
    predict = model.predict_classes(digit)
    return predict
