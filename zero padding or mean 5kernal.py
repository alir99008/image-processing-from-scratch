# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:38:03 2022

@author: Hp
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:34:43 2022

@author: Hp
"""

import cv2

import numpy as np


img = cv2.imread("ali.jpg")
img1 = cv2.imread("ali.jpg",0)
"""
fil = np.array(([1,1,1],
               [1,1,1],
               [1,1,1]))*1/9

"""
fil = np.array(([1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1]))*1/25

rows = img.shape[0] +4
columns = img.shape[1] +4

zero_padding_img = np.zeros((rows , columns))

for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        zero_padding_img[img_row+2][img_col+2] = img1[img_row][img_col]
    


for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        mean=0
        for k in range(5):
            for l in range(5):
                
                mul = zero_padding_img[img_row+k , img_col+l] * fil[k , l]
                mean = mean+mul

        img[img_row][img_col] = mean    
    
print(img.shape)
print(img)


cv2.imshow("orignal image", img)
cv2.imshow("zero image", zero_padding_img)
cv2.imshow("gray image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
