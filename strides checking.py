# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 18:10:30 2022

@author: Hp
"""

import numpy as np
import cv2



img = cv2.imread("low contrast.jfif")
grayscale_img = cv2.imread("low contrast.jfif",0)      



rows = grayscale_img.shape[0]
col = grayscale_img.shape[1]

fil = np.array(([255,255,255],
               [0,0,0],
               [0,0,0]))*1/9

fil_size_row = fil.shape[0]
fil_size_col = fil.shape[1]
pad_rows = img.shape[0] + fil_size_row-1
pad_columns = img.shape[1] + fil_size_col-1

zero_padding_img = np.zeros((pad_rows , pad_columns))


stride_rows = []
stride_cols = []

for i in range(1,10):
    
    height = (rows+(fil.shape[0]//2)+(fil.shape[0]//2)-fil.shape[0])
    width = (col+(fil.shape[1]//2)+(fil.shape[1]//2)-fil.shape[1])
    
    if height%i ==0:
        stride_rows.append(i)
    if width%i ==0:
        stride_cols.append(i)
    
    
print(stride_rows)
print(stride_cols)   

    




