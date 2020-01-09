import cv2
import matplotlib.pyplot as plt
import numpy as np 

#reading the image  
img = cv2.imread("C:\\Users\\nitma\\OneDrive\\Desktop\\Coding\\tkInter_Canvas_Test\\inner_folder\\image.png",0)
 
#cv2.imshow('sample image',img)
plt.imshow(img)
plt.show()
 
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image