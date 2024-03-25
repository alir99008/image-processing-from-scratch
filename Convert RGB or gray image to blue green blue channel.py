# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:29:45 2022

@author: Hp
"""

import cv2
import numpy as np




"""

img = cv2.imread("ali.jpg")
img = cv2.resize(img, (1280, 720))
cv2.imshow("Color Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
# In[2]:
img.shape
 
 
# # Blue Image
# In[4]:
 
b, g, r = cv2.split(img)
zeros_ch = np.zeros(img.shape[0:2], dtype="uint8")
blue_img = cv2.merge([b, zeros_ch, zeros_ch])
cv2.imshow("Blue Image", blue_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
# # Green Image
# In[5]:
green_img = cv2.merge([zeros_ch, g, zeros_ch])
cv2.imshow("Green Image", green_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# # Red Image
# In[6]:
 
red_img = cv2.merge([zeros_ch, zeros_ch, r])
cv2.imshow("Red Image", red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# # Show Image using Index spliting and 4 image in One Window
# In[7]:
 
img = cv2.resize(img, (400,300))
red_array = np.zeros(img.shape, dtype="uint8")
red_array[:,:,2] = img[:,:,2]
green_array = np.zeros(img.shape, dtype="uint8")
green_array[:,:,1] = img[:,:,1]
blue_array = np.zeros(img.shape, dtype="uint8")
blue_array[:,:,0] = img[:,:,0]
ht1 = np.hstack((red_array, green_array))
ht2 = np.hstack((blue_array, img))
img_4 = np.vstack((ht1, ht2))
 
cv2.imshow("4 images", img_4)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""
from matplotlib import pyplot as plt

img = cv2.imread("ali.jpg")

b , g , r = cv2.split(img)


#mean of image

zero_channel = np.zeros(img.shape[0:2] , dtype = "uint8")
blue_channel = cv2.merge([b , zero_channel , zero_channel])

new_img = np.zeros(img.shape[0:2] , dtype="float")

print("orignal image" , img.shape)
print("new image" , new_img.shape)

for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        
        pixel = img[img_row][img_col]
        
        mean = (pixel[0]+pixel[1]+pixel[2])//3
        new_img[img_row][img_col] = mean
        

plt.imshow(new_img)
plt.show()
cv2.imshow("orignal image" , img)
cv2.imshow("blue channel image" , blue_channel)
cv2.imshow("3 channel mean image" , new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()