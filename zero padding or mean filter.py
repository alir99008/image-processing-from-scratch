# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:34:43 2022

@author: Hp
"""

import cv2

import numpy as np


img = cv2.imread("ali.jpg")
img2 = cv2.imread("ali.jpg",0)
img1 = img2.copy()
"""
fil = np.array(([1,1,1],
               [1,1,1],
               [1,1,1]))*1/9
"""
fil = np.array(([1,0,0],
               [0,1,0],
           [0,0,1]))*1/9
"""
fil = np.array(([1,1,1],
               [0,0,0],
               [0,0,0]))*1/9

fil = np.array(([1,0,0],
               [1,0,0],
               [1,0,0]))*1/9
#  ..... 1=255
# sobel......
# laplacian....
"""
rows = img.shape[0] +2
columns = img.shape[1] +2

zero_padding_img = np.zeros((rows , columns))

for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        zero_padding_img[img_row+1][img_col+1] = img1[img_row][img_col]
    


for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        mean=0
        for k in range(3):
            for l in range(3):
                
                mul = zero_padding_img[img_row+k , img_col+l] * fil[k , l]
                mean = mean+mul

        img1[img_row][img_col] = mean    
    
print(img.shape)
print(img)


cv2.imshow("orignal image", img)
cv2.imshow("zero image", zero_padding_img)
cv2.imshow("filter image", img1)
cv2.imshow("gray image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
