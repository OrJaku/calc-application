from app import ml_model
from data_generator import save_path
import os
import numpy as np

basedir = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(basedir, save_path)
images_path = os.path.join(data_path, "images.npy")
labels_path = os.path.join(data_path, "labels.npy")
test_images_path = os.path.join(data_path, "images.npy")
test_labels_path = os.path.join(data_path, "labels.npy")

images = np.load(images_path)
labels = np.load(labels_path)
test_images = np.load(images_path)
test_labels = np.load(labels_path)


ml_model.learning(images, labels, test_images, test_labels, len(labels), len(test_labels))
