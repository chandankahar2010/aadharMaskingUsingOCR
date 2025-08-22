#Using Haar cascade xml custom object detection
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('object_detection/input/ac.bmp')
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(1,1,1)
plt.imshow(img_rgb)
plt.show()
face=cv2.CascadeClassifier('object_detection/ac_object.xml')
print('face------->',face)
found=face.detectMultiScale(img_rgb,minSize =(20,20))
print('object---------->',found)
amount_found = len(found)
if amount_found != 0:
    for (x, y, width, height) in found:
        # We draw a green rectangle around
        # every recognized sign
        cv2.rectangle(img_rgb, (x, y), 
                      (x + height, y + width), 
                      (0, 255, 0), 5)
          
# Creates the environment of 
# the picture and shows it
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()