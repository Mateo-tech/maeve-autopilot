import numpy as np
import cv2
import math
import random
from keras.layers import Dense, Activation, Flatten, Conv2D, Lambda
from keras.layers import MaxPooling2D, Dropout
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
import sklearn.utils
import model

img_width = 100
img_height = 100

def process_img(img):
    img = img[-160:-20] # Cut out the useless features
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, (img_width, img_height))
    return img

def load_data():
    X = []
    Y = []
    
    file = open("./data/angles_raw.txt") 
    lines = file.readlines()
    
    i = 200
    while i < 120000:
        file = open("./data/angles_raw.txt") 
        line = str(lines[i])
        img = cv2.imread("data/img/" + line.split()[0])
        processed_img = process_img(img)
        X.append(processed_img)
        Y.append(float(line.split()[1]) * math.pi / 180)
        i += 10
    print("Finished loading data!")

    return np.array(X).astype('float32'), np.array(Y).astype('float32')

def main():
    (X, Y) = load_data()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, test_size=0.2, shuffle=False)
    X_train_flattened = X_train.reshape(X_train.shape[0], img_width, img_height, 1)
    X_test_flattened = X_test.reshape(X_test.shape[0], img_width, img_height)

    # Callback for saving the weights
    checkpoints_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath="checkpoints/checkpoints.ckpt",
        save_weights_only=True,
        verbose=1)

    history = model.model.fit(
        X_train_flattened, Y_train, 
        validation_data=(X_test_flattened, Y_test), 
        epochs=10,
        callbacks=[checkpoints_callback],
        verbose=1)

    # model.model.save("checkpoints/model.h5")
main()