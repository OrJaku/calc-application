from keras.models import model_from_json
from PIL import Image
from scipy import ndimage
import numpy as np
import PIL.ImageOps
from keras.utils import to_categorical
import os

with open('data/new__model_config.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('data/new__model_mnist.h5')


def learning(train_images, train_labels, list_len, epochs=10, model=model):
    train_images = train_images.reshape((list_len, 28 * 28))
    train_images = train_images.astype("float32") / 255
    train_labels = to_categorical(train_labels)
    model.compile("adam", "categorical_crossentropy")

    model.fit(
        train_images,
        train_labels,
        epochs=epochs,
        batch_size=128,
        verbose=2,
        )
    save_file = 'data/'
    model_name = 'new__model_mnist.h5'

    json_config = model.to_json()
    with open('data/new__model_config.json', 'w') as json_file:
        json_file.write(json_config)
    model_path = os.path.join(save_file, model_name)
    model.save_weights(model_path)
    print('Saved trained model at %s ' % model_path)


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
