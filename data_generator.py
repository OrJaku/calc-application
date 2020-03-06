import numpy as np
import os
from PIL import Image
import PIL.ImageOps


basedir = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(basedir, "data/test_img")
files_list = os.listdir(data_path)
image_folder_path = "data/test_img"
save_path = "data"

images_list = []
labels_list = []
for image in files_list:
    path_to_image = os.path.join(image_folder_path, image)
    img = Image.open(path_to_image).convert('L')
    img = img.resize((28, 28))
    img = PIL.ImageOps.invert(img)
    img_array = np.array(img)
    images_list.append(img_array)

    lbl = image[-5]
    labels_list.append(lbl)

image_list = np.array(images_list)
labels_list = np.array(labels_list)

images_data_path = os.path.join(save_path, "images")
labels_data_path = os.path.join(save_path, "labels")
np.save(images_data_path, image_list)
np.save(labels_data_path, labels_list)
print("File saved in '/data' folder ")

