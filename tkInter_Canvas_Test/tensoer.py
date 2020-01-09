import tensorflow as tf
from tensorflow import keras
import cv2
import matplotlib.pyplot as plt
import numpy as np 


mnist = tf.keras.datasets.mnist # 28x28 images of numbers  0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()


#######################################
print(x_train[0])

plt.imshow(x_train[0])
plt.show()

#########################################
img = cv2.imread("C:\\Users\\nitma\\OneDrive\\Desktop\\Coding\\tkInter_Canvas_Test\\inner_folder\\image28x28.png",0)
 
print(img)
plt.imshow(img)
plt.show()


cv2.imwrite("saved.png",x_train[0])
