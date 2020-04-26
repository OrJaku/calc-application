from keras.models import model_from_json
from PIL import Image
from scipy import ndimage
import numpy as np
import PIL.ImageOps
from keras.utils import to_categorical
import os

with open('data/ml_model_files/model_config.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('data/ml_model_files/model_mnist.h5')


def learning(
        train_images,
        train_labels,
        test_images,
        test_labels,
        list_len_train,
        list_len_test,
        epochs=10,
        save_file_path='data/ml_model_files',
        model=model,
        ):

    train_images = train_images.reshape((list_len_train, 28 * 28))
    train_images = train_images.astype("float32") / 255

    test_images = test_images.reshape((list_len_test, 28 * 28))
    test_images = test_images.astype("float32") / 255

    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)

    model.compile("adam", "categorical_crossentropy")

    model.fit(
        train_images,
        train_labels,
        epochs=epochs,
        batch_size=128,
        verbose=2,
        )
    loss_acc = model.evaluate(test_images, test_labels)
    print('loss= ', loss_acc)

    model_name_json = 'model_config.json'
    model_path = os.path.join(save_file_path, model_name_json)
    json_config = model.to_json()
    with open(model_path, 'w') as json_file:
        json_file.write(json_config)

    model_name_weights = 'model_mnist.h5'
    model_path = os.path.join(save_file_path, model_name_weights)
    model.save_weights(model_path)
    print('Saved trained model at %s ' % model_path)


def prediction(image):
    img_list = []
    img = image.convert('L')
    img = img.resize((28, 28))
    img = img.point(lambda x: 230 if x > 1 else 0)
    img = ndimage.gaussian_filter(img, sigma=0.1)
    img_array = np.array(img)
    img_array = img_array.reshape(28, 28, 1)
    image = img_array.astype("float32") / 255
    img_list.append(image)
    img_list = np.array(img_list)
    predict = model.predict_classes(img_list)

    filtered_image = Image.fromarray(img).resize((5*28, 5*28))
    filtered_image = PIL.ImageOps.invert(filtered_image)

    return predict, img_list, filtered_image
