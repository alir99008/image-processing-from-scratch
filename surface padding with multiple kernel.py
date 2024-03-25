# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:51:12 2022

@author: Hp
"""

import cv2

import numpy as np

img = cv2.imread("ali.jpg")
img1 = cv2.imread("ali.jpg",0)

fil_size=3
fil = fil_size//2
print("fil ", fil)
rows = img.shape[0] +fil_size -1
columns = img.shape[1] +fil_size-1

print(img1.shape[0]-1)
pad_img = np.zeros((rows , columns) , dtype="uint8")

row_len = img1.shape[0]-1
col_len = img1.shape[1]-1




for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        if img_row==0 and img_col==0:
            pad_img[img_row:fil+1 , img_col:fil+1] = img1[img_row , img_col]
            
            
        if img_row ==0 and img_col!=0:
            
            pad_img[img_row:fil , img_col+fil] = img1[img_row , img_col]
        
        if img_row !=0 and img_col == 0:
            pad_img[img_row+fil, img_col:fil] = img1[img_row , img_col]
            
        
        if img_row != 0 and img_col == col_len:
            
            
            b = pad_img.shape[1]-1
            
            pad_img[img_row+fil, img_col+fil+1:b+1] = img1[img_row , img_col]
          
            
        if img_row == row_len and img_col != 0:
           
           
           a = pad_img.shape[0]-1
           b = pad_img.shape[0]-fil
           pad_img[b:a+1, img_col+fil] = img1[img_row , img_col]
        
        
        if img_row == 0 and img_col == col_len:
           
           
           a = pad_img.shape[1]-1
           b = pad_img.shape[1]-fil-1
         
           pad_img[0:img_row+fil+1, b:a+1] = img1[img_row , img_col]
           
           
           
        if img_row == row_len and img_col == 0:
            
            a = pad_img.shape[0]-fil-1
            b = pad_img.shape[0]-1
            pad_img[img_row+fil:b+1, 0:fil+1] = img1[img_row , img_col]
            print("A", img1[img_row , img_col])
            
        if img_row == row_len and img_col==col_len:
            a = pad_img.shape[0]-1
            b = pad_img.shape[1]-fil-1
            c = pad_img.shape[1]
            pad_img[a, b] = img1[img_row , img_col]
            pad_img[img_row+fil:a+1 , b:c] = img1[img_row , img_col]
            
            
        else:
            pad_img[img_row+fil : row_len+fil+1   , img_col+fil : col_len+fil+1] = img1[img_row , img_col]

