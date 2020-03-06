from keras.models import model_from_json
from PIL import Image
from scipy import ndimage
import numpy as np
import PIL.ImageOps

with open('data/model_config.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('data/model_mnist.h5')


def prediction(image):
    img_list = []
    img = image.convert('L')
    img = img.resize((28, 28))
    img = img.point(lambda x: 230 if x > 1 else 0)
    img = ndimage.gaussian_filter(img, sigma=0.1)
    img_array = np.array(img)
    img_array = img_array.reshape(28 * 28)
    image = img_array.astype("float32") / 255
    img_list.append(image)
    img_list = np.array(img_list)
    predict = model.predict_classes(img_list)
    predict_percent = model.predict(img_list)
    print(predict_percent)

    filtered_image = Image.fromarray(img).resize((5*28, 5*28))
    filtered_image = PIL.ImageOps.invert(filtered_image)

    return predict, img, filtered_image, predict_percent


