# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 08:55:04 2022

@author: Hp
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 07:15:52 2022

@author: Hp
"""
import cv2
import numpy as np

img = cv2.imread("ali1.png")
img1 = cv2.imread("ali1.png",0)


fil = np.array(([255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255]))


result = np.array(([0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0]))



thresh_value , binary_image = cv2.threshold(img1,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 

rows = img1.shape[0] + 6
columns = img1.shape[1] +6


pad_img = np.zeros((rows , columns) , dtype="uint8")

row= img1.shape[0]
column = img1.shape[1] 
new_img = np.zeros((row , column) , dtype="uint8")

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        pad_img[i+3 , j+3] = binary_image[i,j]
 
                
 
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
       
        for k in range(7):
            for l in range(7):
                if pad_img[k+i , l+j] == fil[k,l]:
                    result[k,l] = 255
                else:
                    result[k,l] = 0
        
        check = np.any(result==255)
        if check:
            new_img[i,j] = 255
        else:
            new_img[i,j] = 0
           
        
cv2.imshow("orignal image", img)

cv2.imshow("filter image", binary_image)
cv2.imshow("newr image", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
