# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 19:29:15 2022

@author: Hp
"""

import numpy as np
import cv2

class pad:
    def __init__(self ,gray_img, k_size , padding):
        self.k_size = k_size
        self.padding = padding
        self.gray_img = gray_img
        
    
    def pad_img(self):
        if self.padding=="zero":
            
            
            fil = self.k_size
            img = self.gray_img
            fil_size_row = fil[0]
            fil_size_col = fil[1]
           
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
            fil_size=self.k_size
            fil = fil_size//2
            
            img = self.gray_img
            
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





class filtering(pad):
    
    def __init__(self , gray_img , k_size , padding):
        super().__init__(gray_img , k_size , padding)
        self.gray_img = gray_img
        
    def mean_filter(self):
        img = self.gray_img
        pad = self.k_size[0]
        fil = np.array(([255,0,0],
                       [0,255,0],
                       [0,0,255]))*1/9
        padding_img = super().pad_img()
        
        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                mean=0
                for k in range(3):
                    for l in range(3):
                        
                        mul = padding_img[img_row+k , img_col+l] * fil[k , l]
                        mean = mean+mul
        
                img[img_row][img_col] = mean    
    
        return img
        
img = cv2.imread("ali.jpg")
grayscale_img = cv2.imread("ali.jpg",0)      



result = filtering(grayscale_img, (3,3), "zero")   #(img , kernel , padding)    arguments take
result_img = result.mean_filter()



cv2.imshow("orignal image", img) 
cv2.imshow("result image", result_img)



cv2.waitKey(0)
cv2.destroyAllWindows()

