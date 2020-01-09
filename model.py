import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical
import cv2
import numpy as np

class ImageNerualNet():

    def __init__(self):
        #load the mnist data
        mnist = tf.keras.datasets.mnist # 28x28 images of numbers 0-9
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        #Scaling and Normalizing
        self.training_images = x_train.reshape((60000, 28, 28, 1)) / 255.0
        #self.training_values = to_categorical(y_train)
        self.training_values = y_train

        self.testing_images = x_test.reshape((10000, 28, 28, 1)) / 255.0
        #self.testing_values = to_categorical(y_test)
        self.testing_values = y_test

        #building the model NN
        self.model = Sequential()
        self.model.add(Flatten())
        self.model.add(Dense(128, activation = 'relu'))
        self.model.add(Dense(128, activation = 'relu'))
        self.model.add(Dense(10, activation = 'softmax'))

        ##self.model = keras.Sequential([
        ##        keras.layers.Flatten(),
        ##        keras.layers.Dense(128, activation = 'relu'),
        ##        keras.layers.Dense(128, activation = 'relu'),
        ##        keras.layers.Dense(10, activation = 'softmax')
        ##    ])
        
        self.model.compile(optimizer='adam', 
            loss='sparse_categorical_crossentropy', 
            metrics=['accuracy'])
        
        self.model.fit(self.training_images, 
                       self.training_values, 
                       validation_split=0.3,
                       callbacks=[keras.callbacks.EarlyStopping(patience=2)],
                       epochs=50)

    def predict(self, image):
        input = cv2.resize(image, (28, 28)).reshape((28, 28, 1)) / 255.0
        return self.model.predict_classes(np.array([input]))
