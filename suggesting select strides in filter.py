# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 18:44:51 2022

@author: Hp
"""

import cv2
import numpy as np


def pad_image(gray_img , fil , padding):
    if padding=="zero":
        
        
    
        img = gray_img.copy()
        fil_size_row = fil.shape[0]
        fil_size_col = fil.shape[1]
       
        fil_row = fil_size_row//2
        fil_col= fil_size_col//2
       
        rows = img.shape[0] + fil_size_row-1
        columns = img.shape[1] + fil_size_col-1
       
        zero_padding_img = np.zeros((rows , columns))
       
       
        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                zero_padding_img[img_row+fil_row][img_col+fil_col] = img[img_row][img_col]
                
        return zero_padding_img
        
    
    else:
        fil_size=fil.shape[0]
        fil = fil_size//2
        
        img = gray_img.copy()
        
        rows = img.shape[0] +fil_size -1
        columns = img.shape[1] +fil_size-1

        
        pad_img = np.zeros((rows , columns) , dtype="uint8")

        row_len = img.shape[0]-1
        col_len = img.shape[1]-1




        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                if img_row==0 and img_col==0:
                    pad_img[img_row:fil+1 , img_col:fil+1] = img[img_row , img_col]
                    
                    
                if img_row ==0 and img_col!=0:
                    
                    pad_img[img_row:fil , img_col+fil] = img[img_row , img_col]
                
                if img_row !=0 and img_col == 0:
                    pad_img[img_row+fil, img_col:fil] = img[img_row , img_col]
                    
                
                if img_row != 0 and img_col == col_len:
                    
                    
                    b = pad_img.shape[1]-1
                    
                    pad_img[img_row+fil, img_col+fil+1:b+1] = img[img_row , img_col]
                  
                    
                if img_row == row_len and img_col != 0:
                   
                   
                   a = pad_img.shape[0]-1
                   b = pad_img.shape[0]-fil
                   pad_img[b:a+1, img_col+fil] = img[img_row , img_col]
                
                
                if img_row == 0 and img_col == col_len:
                   
                   
                   a = pad_img.shape[1]-1
                   b = pad_img.shape[1]-fil-1
                 
                   pad_img[0:img_row+fil+1, b:a+1] = img[img_row , img_col]
                   
                   
                   
                if img_row == row_len and img_col == 0:
                    
                    a = pad_img.shape[0]-fil-1
                    b = pad_img.shape[0]-1
                    pad_img[img_row+fil:b+1, 0:fil+1] = img[img_row , img_col]
                    
                    
                if img_row == row_len and img_col==col_len:
                    a = pad_img.shape[0]-1
                    b = pad_img.shape[1]-fil-1
                    c = pad_img.shape[1]
                    pad_img[a, b] = img[img_row , img_col]
                    pad_img[img_row+fil:a+1 , b:c] = img[img_row , img_col]
                    
                    
                else:
                    pad_img[img_row+fil : row_len+fil+1   , img_col+fil : col_len+fil+1] = img[img_row , img_col]

        return pad_img

def minpooling(gray_img , fil , stride , padding ):
    img = gray_img.copy()
    rows = img.shape[0]
    col = img.shape[1]
    pad = fil.shape[0]
    
    #padding_img = padding()
    
    zero_padding_img = pad_image(gray_img , fil , padding)
    
    print(zero_padding_img)
    
    
    height = (rows+(fil.shape[0]//2)+(fil.shape[0]//2)-fil.shape[0])
    width = (col+(fil.shape[1]//2)+(fil.shape[1]//2)-fil.shape[1])
    
    stride_height = stride[0]
    stride_width = stride[1]
    print(stride_height)
    
    if height%stride_height ==0 and width%stride_width ==0:

        i=0
        
        while(i<rows):
            j=0
            while(j<col):
                
                for k in range(fil.shape[0]):
                    for l in range(fil.shape[1]):
                        
                        fil[k][l] = zero_padding_img[i+k , j+l]
                        
                img[i,j] = np.min(fil)
                
                j=j+stride[1]
            
            i=i+stride[0]
                
    
        return img
    
    else:
        return "No"



def maxpooling(gray_img , fil , stride , padding ):
    img = gray_img.copy()
    rows = img.shape[0]
    col = img.shape[1]
    pad = fil.shape[0]
    
    #padding_img = padding()
    
    zero_padding_img = pad_image(gray_img , fil , padding)
    
    print(zero_padding_img)
    
    
    height = (rows+(fil.shape[0]//2)+(fil.shape[0]//2)-fil.shape[0])
    width = (col+(fil.shape[1]//2)+(fil.shape[1]//2)-fil.shape[1])
    
    stride_height = stride[0]
    stride_width = stride[1]
    print(stride_height)
    
    if height%stride_height ==0 and width%stride_width ==0:

        i=0
        
        while(i<rows):
            j=0
            while(j<col):
                
                for k in range(fil.shape[0]):
                    for l in range(fil.shape[1]):
                        
                        fil[k][l] = zero_padding_img[i+k , j+l]
                        
                img[i,j] = np.max(fil)
                
                j=j+stride[1]
            
            i=i+stride[0]
                
    
        return img
    
    else:
        return "No"


img = cv2.imread("ali.jpg")
grayscale_img = cv2.imread("ali.jpg",0)      
rows = img.shape[0]
col = img.shape[1]


fil = np.array(([0,0,0],
               [0,0,0],
               [0,0,0]))


#result_img = maxpooling(grayscale_img, fil, (2,1) , "zero")
result_img = minpooling(grayscale_img, fil, (2,5) , "zeroxs")

if result_img == "No":
    stride_rows = []
    stride_cols = []

    for i in range(1,10):
        
        height = (rows+(fil.shape[0]//2)+(fil.shape[0]//2)-fil.shape[0])
        width = (col+(fil.shape[1]//2)+(fil.shape[1]//2)-fil.shape[1])
        
        if height%i ==0:
            stride_rows.append(i)
        if width%i ==0:
            stride_cols.append(i)
        
        
    print("stride for rows :",stride_rows)
    print("stride for cols :",stride_cols)   
else:
    cv2.imshow("orignal image", img) 
    cv2.imshow("result image", result_img)
    cv2.imshow("gray image", grayscale_img)



    cv2.waitKey(0)
    cv2.destroyAllWindows()
