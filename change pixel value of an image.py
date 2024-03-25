# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:19:59 2022

@author: Hp
"""


import cv2
import numpy as np
import time
import random



img = cv2.imread("ali.jpg")
"""
img = cv2.resize(img, (1280, 720))

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""


#Add New single color pixel in a Image

"""
img[0][0] ## Read pixel

# Add white pixels
img_copy = img.copy()
img_copy[0][0] = np.array([255,255,255])
 
cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Add white, black, Red, Green, Blue pixels
#img_copy = img.copy()
#img_copy[0][0] = np.array([255,255,255]) # White pixel
img_copy[0][1] = np.array([0,0,0]) #  Black pixel
#img_copy[0][2] = np.array([0,0,255]) # Red pixel
#img_copy[0][3] = np.array([0,255,0]) # Green Pixel
#img_copy[0][4] = np.array([255,0,0]) # Blue pixel
 
cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""

#Add New color pixel in a row of Image

"""
img_copy = img.copy()
 
img_width= img_copy.shape[1]
img_height= img_copy.shape[0]
 
print("img_width: ", img_width)
print("img_height: ", img_height)
 
for cols_index in range(img_width):
    img_copy[0][cols_index] = np.array([255,255,255]) # White pixel
    img_copy[1][cols_index] = np.array([0,0,0]) #  Black pixel
    img_copy[2][cols_index] = np.array([0,0,255]) # Red pixel
    img_copy[3][cols_index] = np.array([0,255,0]) # Green Pixel
    img_copy[4][cols_index] = np.array([255,0,0]) # Blue pixel
     
cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""



#Add New color pixel in a row of Image with logic/alternatively

"""

img_copy = img.copy()
 
img_width= img_copy.shape[1]
img_height= img_copy.shape[0]
 
print("img_width: ", img_width)
print("img_height: ", img_height)
 
for cols_index in range(img_width):
    if cols_index%2 == 0:
        img_copy[0][cols_index] = np.array([255,255,255]) # White pixel
        img_copy[1][cols_index] = np.array([0,0,0]) #  Black pixel
        img_copy[2][cols_index] = np.array([0,0,255]) # Red pixel
        img_copy[3][cols_index] = np.array([0,255,0]) # Green Pixel
        img_copy[4][cols_index] = np.array([255,0,0]) # Blue pixel
     
cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""



#Add New color pixel in a Image with logic/alternatively

"""
img_copy = img.copy()
 
img_width= img_copy.shape[1]
img_height= img_copy.shape[0]
 
print("img_width: ", img_width)
print("img_height: ", img_height)
 
for rows_index in range(img_height):
    for cols_index in range(img_width):
        #if cols_index%2 == 0:
        if cols_index%50 == 0:
            #img_copy[rows_index][cols_index] = np.array([255,255,255]) # White pixel
            img_copy[rows_index][cols_index] = np.array([0,0,255]) # Red pixel
 
cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()






img_copy = img.copy()
 
img_width= img_copy.shape[1]
img_height= img_copy.shape[0]
 
print("img_width: ", img_width)
print("img_height: ", img_height)
 
for rows_index in range(img_height):
    if rows_index%2 == 0:
    #if rows_index%20 == 0:
        for cols_index in range(img_width):
            if cols_index%2 == 0:
            #if cols_index%50 == 0:
                img_copy[rows_index][cols_index] = np.array([255,255,255]) # White pixel
                #img_copy[rows_index][cols_index] = np.array([0,0,255]) # Red pixel
 
cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""

#Add New random color pixel randomly in a Image

"""

img_copy = img.copy()
 
img_width= img_copy.shape[1]
img_height= img_copy.shape[0]
 
print("img_width: ", img_width)
print("img_height: ", img_height)
 
for rows_index in range(img_height):
    if rows_index%2 == 0:
    #if rows_index%20 == 0:
        for cols_index in range(random.randint(0,1000)):
            #if cols_index%2 == 0:
            #if cols_index%50 == 0:
                b_pixel = random.randint(0,255)
                g_pixel = random.randint(0,255)
                r_pixel = random.randint(0,255)
                rand_cols_index = random.randint(0,img_width-1)
                img_copy[rows_index][rand_cols_index] = np.array([b_pixel,g_pixel,r_pixel]) # random pixel
                #img_copy[rows_index][cols_index] = np.array([255,255,255]) # white pixel
 
cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""



#Add New color pixels in portion or any location of Image

	
random.randint(0,255)


img_copy = img.copy()
 
img_width= img_copy.shape[1]
img_height= img_copy.shape[0]
 
print("img_width: ", img_width)
print("img_height: ", img_height)
 
for rows_index in range(500,img_width):
    if rows_index%2 == 0:
    #if rows_index%20 == 0:
        for cols_index in range(380, img_height):
            if cols_index%2 == 0:
            #if cols_index%50 == 0:
                b_pixel = random.randint(0,255)
                g_pixel = random.randint(0,255)
                r_pixel = random.randint(0,255)
                #rand_cols_index = random.randint(0,img_width-1)
                #img_copy[rows_index][cols_index] = np.array([b_pixel,g_pixel,r_pixel]) # random pixel
                #img_copy[rows_index][cols_index] = np.array([255,255,255]) # white pixel
                img_copy[rows_index][cols_index] = np.array([255,0,0]) # blue pixel
cv2.imshow("Image", img_copy)
cv2.imwrite("effect_img.png", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
