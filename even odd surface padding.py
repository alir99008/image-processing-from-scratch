# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:55:47 2022

@author: Hp
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:51:12 2022

@author: Hp
"""

import cv2

import numpy as np

img = cv2.imread("ali.jpg")
img1 = cv2.imread("ali.jpg",0)
def create_img(upper , lower , left , right ):
    
    rows = upper+lower
    columns = left+right
    
    fil_size=upper+left
    fil = fil_size//2
    print("fil ", fil)
    
    rows = img.shape[0] +rows
    columns = img.shape[1] +columns
    
    print(img1.shape[0]-1)
    pad_img = np.zeros((rows , columns) , dtype="uint8")
    
    row_len = img1.shape[0]-1
    col_len = img1.shape[1]-1
    
    
    
    
    for img_row in range(img.shape[0]):
        for img_col in range(img.shape[1]):
            if img_row==0 and img_col==0:
                pad_img[img_row:upper+1 , img_col:left+1] = img1[img_row , img_col]
                
                
            if img_row ==0 and img_col!=0:
                
                pad_img[img_row:upper , img_col+left] = img1[img_row , img_col]
            
            if img_row !=0 and img_col == 0:
                pad_img[img_row+upper, img_col:left] = img1[img_row , img_col]
                
            
            if img_row != 0 and img_col == col_len:
                
                
                b = pad_img.shape[1]-1
                
                pad_img[img_row+upper, img_col+left+1:b+1] = img1[img_row , img_col]
              
                
            if img_row == row_len and img_col != 0:
               
               
               a = pad_img.shape[0]-1
               b = pad_img.shape[0]-lower
               pad_img[b:a+1, img_col+left] = img1[img_row , img_col]
            
            
            if img_row == 0 and img_col == col_len:
               
               
               a = pad_img.shape[1]-1
               b = pad_img.shape[1]-right
             
               pad_img[0:img_row+upper+1, b:a+1] = img1[img_row , img_col]
               
               
               
            if img_row == row_len and img_col == 0:
                
                a = pad_img.shape[0]-lower-1
                b = pad_img.shape[0]-1
                pad_img[img_row+upper+1:b+1, 0:left+1] = img1[img_row , img_col]
                print("A", img1[img_row , img_col])
                
            if img_row == row_len and img_col==col_len:
                a = pad_img.shape[0]-1
                b = pad_img.shape[1]-right-1
                c = pad_img.shape[1]
                pad_img[a, b] = img1[img_row , img_col]
                pad_img[img_row+upper+1:a+1 , b+1:c] = img1[img_row , img_col]
                
            else:
                pad_img[img_row+upper , img_col+left] = img1[img_row , img_col]
                
           
          
    return pad_img


zero_pad_img = create_img(4, 2, 3, 2)