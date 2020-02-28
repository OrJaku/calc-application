from keras.models import model_from_json
from keras.datasets import mnist
from keras.utils import to_categorical
from PIL import Image
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import os

(train_images, train_labels), (test_images, test_labels_origin) = mnist.load_data()
# train_images = train_images.reshape((60000, 28 * 28))
# train_images = train_images.astype("float32") / 255
# test_images = test_images.reshape((10000, 28 * 28))
# test_images = test_images.astype("float32") / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels_origin)

basedir = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(basedir, 'data/testing_image')
files_list = os.listdir(data_path)
image_folder_path = "data/testing_image"

img_list = []
img_name_list = []
rgb_list = []
for image in files_list:
    path_to_image = os.path.join(image_folder_path, image)
    rgb = Image.open(path_to_image).convert('L')
    rgb = rgb.resize((28, 28))
    rgb = rgb.point(lambda x: 0 if x > 128 else x)
    img = np.array(rgb)
    img = img.reshape(28 * 28)
    img = img.astype("float32") / 255
    img_list.append(img)

    rgb_list.append(rgb)

    img_name = os.path.basename(path_to_image)[:-4]
    img_name_list.append(img_name)

img_list = np.array(img_list)

with open('data/model_config.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('data/model_mnist.h5')

# predicted_classes = model.predict_classes(test_images)

predict = model.predict_classes(img_list)
checking_list = {}
correct = []
incorrect = []
for name, pre in zip(img_name_list, predict):
    checking_list[name] = pre
    if int(name[1]) == pre:
        correct.append(pre)
    else:
        incorrect.append(pre)
result = len(correct) / len(predict) * 100
print(f"\nCorrect prediction: {round(result, 1)}%")
print(checking_list)
print("\n ",)

fig = plt.figure()
for i in range(2 * 2):
    plt.subplot(2, 2, i + 1)
    plt.tight_layout()
    plt.imshow(test_images[i], cmap='gist_yarg')
    plt.title("Digit: {}".format(img_name_list[i]))
    plt.xticks([])
    plt.yticks([])
plt.show()
