import numpy as np
import os
from PIL import Image
import PIL.ImageOps


basedir = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(basedir, "data/learning_images")
files_list = os.listdir(data_path)
image_folder_path = "data/learning_images"
save_path = "data/learning_data"


def generator():
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
        # Sign "+"
        if lbl == 'p':
            lbl = 11
        # Sign "-"
        elif lbl == "m":
            lbl = 12
        # Sign "/"
        elif lbl == "d":
            lbl = 13
        # Sign "*"
        elif lbl == "n":
            lbl = 14
        # Sign "="
        elif lbl == "e":
            lbl = 15
        else:
            pass
        labels_list.append(lbl)

    images_list = np.array(images_list)
    labels_list = np.array(labels_list)
    return images_list, labels_list


images_list_generated = generator()[0]
labels_list_generated = generator()[1]

images_data_path = os.path.join(save_path, "images")
labels_data_path = os.path.join(save_path, "labels")
np.save(images_data_path, images_list_generated)
np.save(labels_data_path, labels_list_generated)
print("File saved as 'images.npy' and 'labels.npy' in '/data' folder ")


