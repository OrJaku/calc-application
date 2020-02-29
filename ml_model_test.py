from keras.models import model_from_json
from keras.datasets import mnist
from keras.utils import to_categorical
from PIL import Image
import PIL.ImageOps
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
import os
import matplotlib
matplotlib.use('TkAgg')


(train_images, train_labels), (test_images, test_labels_origin) = mnist.load_data()
# train_images = train_images.reshape((60000, 28 * 28))
# train_images = train_images.astype("float32") / 255
# test_images = test_images.reshape((10000, 28 * 28))
# test_images = test_images.astype("float32") / 255
# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels_origin)

basedir = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(basedir, 'data/testing_image')
files_list = os.listdir(data_path)
image_folder_path = "data/testing_image"

img_list = []
img_name_list = []
rgb_list = []
for image in files_list:
    path_to_image = os.path.join(image_folder_path, image)
    img = Image.open(path_to_image).convert('L')
    img = img.resize((28, 28))
    img = PIL.ImageOps.invert(img)
    img = img.point(lambda x: x + 20 if x > 65 else 0)

    # img = ndimage.gaussian_filter(img, sigma=0.8)
    # filter_img = ndimage.gaussian_filter(img, sigma=0.1)
    # alpha = 50
    # img = img + alpha * (img - filter_img)
    # img = Image.fromarray(img)
    # img = img.point(lambda x: x+20 if x > 0 else 0)

    img_array = np.array(img)
    img_array = img_array.reshape(28 * 28)
    img_array = img_array.astype("float32") / 255
    img_list.append(img_array)

    rgb_list.append(img)

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

# plt.hist(rgb_list[2], density=5, bins=10)
# plt.show()
fig1 = plt.figure()
for i in range(5 * 4):
    plt.subplot(5, 4, i + 1)
    plt.tight_layout()
    plt.imshow(rgb_list[i], cmap='gist_yarg')
    plt.title("Digit: {}".format(img_name_list[i]))
    plt.xticks([])
    plt.yticks([])
fig1.show()

fig2 = plt.figure()
for i in range(2 * 2):
    plt.subplot(2, 2, i + 1)
    plt.tight_layout()
    plt.imshow(test_images[i], cmap='gist_yarg')
    plt.title("Digit: {}".format(test_labels_origin[i]))
    plt.xticks([])
    plt.yticks([])
fig2.show()
input("Click enter to stop application")
