# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 13:59:44 2022

@author: Hp
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("ali.jpg")
g_img = cv2.imread("ali.jpg" ,0)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

pixel_cal = np.zeros(shape=(1,256))

rows = img.shape[0]
col = img.shape[1]

print(rows*col)
for img_row in range(rows):
    for img_col in range(col):
        k = gray_img[img_row , img_col]
        pixel_cal[0,k] = pixel_cal[0,k]+1


com_sum = np.array([])
com_sum = np.append(com_sum , pixel_cal[0,0])
for i in range(255):
        k= com_sum[i]+pixel_cal[0,i+1]
        com_sum = np.append(com_sum , k)
          
        
com_sum = np.round((com_sum/(rows*col) * (255)))

for img_row in range(rows):
    for img_col in range(col):
        k = gray_img[img_row , img_col]
        gray_img[img_row , img_col] = com_sum[k ]
        
        
#plt.hist(gray_img.flat , bins = 100 , range=(0,255))
plt.hist(g_img.flat , bins = 100 , range=(0,255))
plt.show()
cv2.imshow("orignal img",img)
cv2.imshow("before equalized",g_img)
cv2.imshow("equalized img",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()