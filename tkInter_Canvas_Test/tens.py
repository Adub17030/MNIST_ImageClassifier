import tensorflow as tf
from tensorflow import keras

mnist = tf.keras.datasets.mnist # 28x28 images of numbers  0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train/255.0
x_test = x_test/255.0

model = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(10, activation = 'softmax')
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

prediction = model.predict([x_test])
print(prediction)


import matplotlib.pyplot as plt
#first image in x_train
#print(x_train[0])
#plt.imshow(x_train[0], cmap = plt.cm.binary)


import numpy as np

print(np.argmax(prediction[0]))

plt.imshow(x_test[0])
plt.show()


#########################################################
print("####################88i8##########################")
#import new as drawtest
import cv2

#drawtest.newmain()

#reading the image  
img = cv2.imread("C:\\Users\\nitma\\OneDrive\\Desktop\\Coding\\tkInter_Canvas_Test\\inner_folder\\image28x28.png",0)
#img = img/255.0
#ANN predicting what number the image is
my_prediction = model.predict([[img]])
print(np.argmax(my_prediction[0]))

#ANN guess and your image 
#print(prediction)
plt.imshow(img)
plt.show()
########################################################33