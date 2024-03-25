

import cv2

import numpy as np

#surface padding......

img = cv2.imread("saa.jpeg")
img1 = cv2.imread("saa.jpeg",0)

fil = np.array(([0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]))

rows = img.shape[0] +4
columns = img.shape[1] +4



zero_padding_img = np.zeros((rows , columns))

for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        zero_padding_img[img_row+2][img_col+2] = img1[img_row][img_col]
    


for img_row in range(img.shape[0]):
    for img_col in range(img.shape[1]):
        
        for k in range(5):
            for l in range(5):
                
                fil[k][l] = zero_padding_img[img_row+k , img_col+l]
                

        img1[img_row][img_col] = np.median(fil)    
    
print(img.shape)
print(img)


cv2.imshow("orignal image", img)
cv2.imshow("zero image", zero_padding_img)
cv2.imshow("filtered image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
