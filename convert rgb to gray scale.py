# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:00:47 2022

@author: Hp
"""



import cv2
import numpy as np

img = cv2.imread("ali.jpg")

r , g ,b = img[: , : , 0] , img[: , : , 1] , img[: , : , 2]

gamma = 8.04

r_constant , g_constant , b_constant  =  0.2126 , 0.7125 , 0.0722

gray_image = r_constant * r **gamma  + g_constant *g**gamma + b_constant*b**gamma


cv2.imshow("gray image", gray_image)

cv2.imshow("color image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
 