# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:49:52 2022

@author: Hp
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("low contrast.jfif")
g_img = cv2.imread("low contrast.jfif" ,0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


pixel_cal = np.zeros(shape=(1,256))

rows = img.shape[0]
col = img.shape[1]


for img_row in range(rows):
    for img_col in range(col):
        k = gray_img[img_row , img_col]
        pixel_cal[0,k] = pixel_cal[0,k]+1



y = np.zeros(shape=(1,256))

for i in range(256):
    if pixel_cal[0,i]==0:
        y[0,i]=0
    else:
        y[0,i]=i


MAX = np.max(y[np.nonzero(y)])
MIN = np.min(y[np.nonzero(y)])

stretch = np.round(((255-0)/(MAX-MIN))*(y-MIN))
stretch[stretch<0] = 0
stretch[stretch>255] = 255


for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        k = gray_img[img_row , img_col]
        gray_img[img_row , img_col] = stretch[0,k]



convert_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)

#plt.hist(gray_img.flat , bins = 100 , range=(0,255))
#plt.hist(g_img.flat , bins = 100 , range=(0,255))
plt.hist(img.flat , bins = 100 , range=(0,255))
plt.show()
cv2.imshow("orignal img",img)

cv2.imshow("stretch img",gray_img)
cv2.imshow("convert img",convert_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
