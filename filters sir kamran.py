# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:15:23 2022

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
gray_img = cv2.imread("ali.jpg",0)

fil1 = np.array(([1,1,1],
               [1,1,1],
               [1,1,1]))*1/9

fil2 = np.array(([255,0,0],
               [0,255,0],
               [0,0,255]))*1/9

fil3 = np.array(([1,1,1],
               [0,0,0],
               [0,0,0]))*1/9

fil4 = np.array(([1,0,0],
               [1,1,1],
               [1,0,1]))*1/9

sobel_y = np.array(([1,0,-1],
               [2,0,-2],
               [1,0,-1]))

sobel_x = np.array(([1,2,1],
                [0,0,0],
                [-1,-2,-1]))


laplacian1 = np.array(([0,-1,0],
                       [-1,4,-1],
                       [0,-1,0]))

laplacian2 = np.array(([-1,-1,-1],
                       [-1,4,-1],
                       [-1,-1,-1]))

rows1 = img.shape[0]

columns1 = img.shape[1]


sobel_img = np.zeros((rows1 , columns1))
laplacian_img = np.zeros((rows1 , columns1))

#  ..... 1=255
# sobel......
# laplacian....


def filtering(fil):

    img1 = gray_img.copy()
    fil_size_row = fil.shape[0]
    fil_size_col = fil.shape[1]
    
    fil_row = fil_size_row//2
    fil_col= fil_size_col//2
    
    print(fil)
    rows = img.shape[0] + fil_size_row-1
    columns = img.shape[1] + fil_size_col-1
    
    zero_padding_img = np.zeros((rows , columns))
    
    
    for img_row in range(img.shape[0]):
        for img_col in range(img.shape[1]):
            zero_padding_img[img_row+fil_row][img_col+fil_col] = img1[img_row][img_col]
        
    
    
    for img_row in range(img.shape[0]):
        for img_col in range(img.shape[1]):
            mean=0
            for k in range(3):
                for l in range(3):
                    
                    mul = zero_padding_img[img_row+k , img_col+l] * fil[k , l]
                    mean = mean+mul
    
            img1[img_row][img_col] = mean    
        

    return img1




filter1 = filtering(fil1)
filter2 = filtering(fil2)
filter3 = filtering(fil3)
filter4 = filtering(fil4)
filter5 = filtering(sobel_y)
filter6 = filtering(sobel_x)
filter7 = filtering(laplacian1)
filter8 = filtering(laplacian2)

import math

for img_row in range(img.shape[0]):
     for img_col in range(img.shape[1]):
         sobel_img[img_row , img_col] = int(math.sqrt(filter5[img_row , img_col]**2 + filter6[img_row , img_col]**2))







cv2.imshow("orignal image", img)
cv2.imshow("gray_img", gray_img)
cv2.imshow("filter1", filter1)
cv2.imshow("filter2", filter2)
cv2.imshow("filter3", filter3)
cv2.imshow("filter4", filter4)
cv2.imshow("sobel", filter5)
cv2.imshow("sobel1", filter6)
cv2.imshow("sobel img", sobel_img)
cv2.imshow("laplacianl1", filter7)
cv2.imshow("laplacianl2", filter8)
cv2.waitKey(0)
cv2.destroyAllWindows()
