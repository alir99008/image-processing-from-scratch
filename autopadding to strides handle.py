# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:22:00 2022

@author: Hp
"""

import cv2
import numpy as np

def pad_image(gray_img , upper , lower , left , right , padding):
    if padding=="zero":
        
        
    
        img = gray_img.copy()
        rows = upper+lower
        columns = left+right
        
        fil_size=upper+left
        fil = fil_size//2
        print("fil ", fil)
        
        rows = img.shape[0] +rows
        columns = img.shape[1] +columns
        
        print(img.shape[0]-1)
        pad_img = np.zeros((rows , columns) , dtype="uint8")
        
        row_len = img.shape[0]-1
        col_len = img.shape[1]-1
        
        
        
        
        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                pad_img[upper+img_row , left+img_col] = img[img_row , img_col]
               
              
        return pad_img
    
    else:
        
        
        img = gray_img.copy()
        
        rows = upper+lower
        columns = left+right
        
        fil_size=upper+left
        fil = fil_size//2
        print("fil ", fil)
        
        rows = img.shape[0] +rows
        columns = img.shape[1] +columns
        
        print(img.shape[0]-1)
        pad_img = np.zeros((rows , columns) , dtype="uint8")
        
        row_len = img.shape[0]-1
        col_len = img.shape[1]-1
        
        
        
        
        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                if img_row==0 and img_col==0:
                    pad_img[img_row:upper+1 , img_col:left+1] = img[img_row , img_col]
                    
                    
                if img_row ==0 and img_col!=0:
                    
                    pad_img[img_row:upper , img_col+left] = img[img_row , img_col]
                
                if img_row !=0 and img_col == 0:
                    pad_img[img_row+upper, img_col:left] = img[img_row , img_col]
                    
                
                if img_row != 0 and img_col == col_len:
                    
                    
                    b = pad_img.shape[1]-1
                    
                    pad_img[img_row+upper, img_col+left+1:b+1] = img[img_row , img_col]
                  
                    
                if img_row == row_len and img_col != 0:
                   
                   
                   a = pad_img.shape[0]-1
                   b = pad_img.shape[0]-lower
                   pad_img[b:a+1, img_col+left] = img[img_row , img_col]
                
                
                if img_row == 0 and img_col == col_len:
                   
                   
                   a = pad_img.shape[1]-1
                   b = pad_img.shape[1]-right
                 
                   pad_img[0:img_row+upper+1, b:a+1] = img[img_row , img_col]
                   
                   
                   
                if img_row == row_len and img_col == 0:
                    
                    a = pad_img.shape[0]-lower-1
                    b = pad_img.shape[0]-1
                    pad_img[img_row+upper+1:b+1, 0:left+1] = img[img_row , img_col]
                    print("A", img[img_row , img_col])
                    
                if img_row == row_len and img_col==col_len:
                    a = pad_img.shape[0]-1
                    b = pad_img.shape[1]-right-1
                    c = pad_img.shape[1]
                    pad_img[a, b] = img[img_row , img_col]
                    pad_img[img_row+upper+1:a+1 , b+1:c] = img[img_row , img_col]
                    
                else:
                    pad_img[img_row+upper , img_col+left] = img[img_row , img_col]
                    
               
             
        return pad_img


def maxpooling(gray_img , fil , stride , padding ):
    img = gray_img.copy()
    img_rows = img.shape[0]
    img_columns = img.shape[1]
   
    
   
    
    stride_row = stride[0]
    stride_col = stride[1]


    pad_rows = 0
    kernel_size = 3
    s = 3-1

    total_rows = 0
    for i in range(1,10):
        if (img_rows + i + i - kernel_size)% stride_row ==0:
            total_rows = i+i
            break
        
    upper = total_rows//2
    lower = total_rows - upper
        
        
        
    total_columns =0
    for i in range(1,10):
        if (img_columns + i + i - kernel_size)% stride_col ==0:
            total_columns = i+i
            break
        

    left = total_columns//2
    right = total_columns - left


    surface_pad_img = pad_image(img , upper, lower, left, right , padding)
    
   
    
    
   
    
    
    new_img_rows = surface_pad_img.shape[0] - (kernel_size-1)
    new_img_columns = surface_pad_img.shape[1] - (kernel_size-1)

    new_img = np.zeros((new_img_rows , new_img_columns) , dtype="uint8")

    for_row = kernel_size//2
    for_col = kernel_size//2
    for i in range(new_img_rows):
        for j in range(new_img_columns):
            new_img[i,j] = surface_pad_img[i+for_row  , j+for_col]




    fil = np.array(([0,0,0],
                   [0,0,0],
                   [0,0,0]))

    i=0

    while(i<new_img_rows):
        j=0
        while(j<new_img_columns):
            
            for k in range(kernel_size):
                for l in range(kernel_size):
                    
                    fil[k][l] = surface_pad_img[i+k , j+l]
                    
            new_img[i,j] = np.max(fil)
            
            j=j+stride[1]
        
        i=i+stride[0]
        
        
    return new_img



def minpooling(gray_img , fil , stride , padding ):
    img = gray_img.copy()
    img_rows = img.shape[0]
    img_columns = img.shape[1]
   
    
   
    
    stride_row = stride[0]
    stride_col = stride[1]


    pad_rows = 0
    kernel_size = 3
    s = 3-1

    total_rows = 0
    for i in range(1,10):
        if (img_rows + i + i - kernel_size)% stride_row ==0:
            total_rows = i+i
            break
        
    upper = total_rows//2
    lower = total_rows - upper
        
        
        
    total_columns =0
    for i in range(1,10):
        if (img_columns + i + i - kernel_size)% stride_col ==0:
            total_columns = i+i
            break
        

    left = total_columns//2
    right = total_columns - left


    surface_pad_img = pad_image(img , upper, lower, left, right , padding)
    
   
    
    
   
    
    
    new_img_rows = surface_pad_img.shape[0] - (kernel_size-1)
    new_img_columns = surface_pad_img.shape[1] - (kernel_size-1)

    new_img = np.zeros((new_img_rows , new_img_columns) , dtype="uint8")

    for_row = kernel_size//2
    for_col = kernel_size//2
    for i in range(new_img_rows):
        for j in range(new_img_columns):
            new_img[i,j] = surface_pad_img[i+for_row  , j+for_col]




    fil = np.array(([0,0,0],
                   [0,0,0],
                   [0,0,0]))

    i=0

    while(i<new_img_rows):
        j=0
        while(j<new_img_columns):
            
            for k in range(kernel_size):
                for l in range(kernel_size):
                    
                    fil[k][l] = surface_pad_img[i+k , j+l]
                    
            new_img[i,j] = np.min(fil)
            
            j=j+stride[1]
        
        i=i+stride[0]
        
        
    return new_img


img = cv2.imread("ali.jpg")
grayscale_img = cv2.imread("ali.jpg",0) 
fil = np.array(([0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]))



result_img =minpooling(grayscale_img , fil , (1,1) , "zeros" )

cv2.imshow("orignal image", img) 
cv2.imshow("result image", result_img)
cv2.imshow("gray image", grayscale_img)



cv2.waitKey(0)
cv2.destroyAllWindows()
