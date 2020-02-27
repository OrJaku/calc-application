from keras.models import model_from_json
from keras.datasets import mnist
from keras.utils import to_categorical
from PIL import Image
import numpy as np
import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
data_path = os.path.join(basedir, 'data/testing_image')
files_list = os.listdir(data_path)
image_folder_path = "data/testing_image"

img_list = []
for image in files_list:
    path_to_image = os.path.join(image_folder_path, image)
    rgb = Image.open(path_to_image).convert('L')
    rgb = rgb.point(lambda x: 0 if x > 150 else x)
    rgb = rgb.resize((28, 28))
    img = np.array(rgb)
    img = img.reshape(28 * 28)
    img = img.astype("float32") / 255
    img_list.append(img)
img_list = np.array(img_list)

(train_images, train_labels), (test_images, test_labels_origin) = mnist.load_data()

train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype("float32") / 255
test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype("float32") / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels_origin)

with open('data/model_config.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('data/model_mnist.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam')

predicted_classes = model.predict_classes(test_images)

predict = model.predict_classes(img_list)
print(files_list)
print(predict)








