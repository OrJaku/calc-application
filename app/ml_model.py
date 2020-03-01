from keras.models import model_from_json
from PIL import Image
import PIL.ImageOps
import numpy as np

with open('data/model_config.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('data/model_mnist.h5')


def prediction(image):
    img = Image.open(image).convert('L')
    img = img.resize((28, 28))
    img = PIL.ImageOps.invert(img)
    img_array = np.array(img)
    img_array = img_array.reshape(28 * 28)
    image = img_array.astype("float32") / 255
    predict = model.predict_classes(image)
    return predict


