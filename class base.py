# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:56:25 2022

@author: Hp
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

class padding:
    def zero_padding(gray_img , pad):
        fil = pad
        img = gray_img
        fil_size_row = fil
        fil_size_col = fil
       
        fil_row = fil_size_row//2
        fil_col= fil_size_col//2
       
        rows = img.shape[0] + fil_size_row-1
        columns = img.shape[1] + fil_size_col-1
       
        zero_padding_img = np.zeros((rows , columns))
       
       
        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                zero_padding_img[img_row+fil_row][img_col+fil_col] = img[img_row][img_col]
                
        return zero_padding_img
    
    
    def surface_padding(gray_img , pad):
        
        fil_size=pad
        fil = fil_size//2
        
        img = gray_img
        
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
           

class correlation:
    def mean_filter(gray_img , fil):
        
        img = gray_img.copy()
        pad = fil.shape[0]
        
        #padding_img = padding()
        
        zero_padding_img = padding.zero_padding(gray_img , pad)
        
        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                mean=0
                for k in range(3):
                    for l in range(3):
                        
                        mul = zero_padding_img[img_row+k , img_col+l] * fil[k , l]
                        mean = mean+mul
        
                img[img_row][img_col] = mean    
    
        return img
        
    


    def median_filter(gray_img , fil):
        img = gray_img.copy()
        pad = fil.shape[0]
        
        #padding_img = padding()
        
        zero_padding_img = padding.zero_padding(gray_img , pad)
        


        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                
                for k in range(5):
                    for l in range(5):
                        
                        fil[k][l] = zero_padding_img[img_row+k , img_col+l]
                        

                img[img_row][img_col] = np.median(fil)    

        return img
    
    
    
    def other_filters(gray_img , fil):
        img = gray_img.copy()
        pad = fil.shape[0]
        
        #padding_img = padding()
        
        zero_padding_img = padding.zero_padding(gray_img , pad)
        
        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                mean=0
                for k in range(3):
                    for l in range(3):
                        
                        mul = zero_padding_img[img_row+k , img_col+l] * fil[k , l]
                        mean = mean+mul
        
                img[img_row][img_col] = mean    
    
        return img

    
    def erosion_filters(gray_img , fil):
        img = gray_img.copy()
        pad = fil.shape[0]
        pad_img = padding.zero_padding(gray_img , pad)
        
        #padding_img = padding()
        result = np.array(([0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0]))

        thresh_value , binary_image = cv2.threshold(img,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        
        
        row= img.shape[0]
        column = img.shape[1] 
        new_img = np.zeros((row , column) , dtype="uint8")
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
               
                for k in range(7):
                    for l in range(7):
                        if pad_img[k+i , l+j] == fil[k,l]:
                            result[k,l] = 255
                        else:
                            result[k,l] = 0
                
                check = np.all(result==255)
                if check:
                    new_img[i,j] = 255
                else:
                    new_img[i,j] = 0
                   
                    
        return new_img
    
    
    
    def dialation_filters(gray_img , fil):
        img = gray_img.copy()
        pad = fil.shape[0]
        pad_img = padding.zero_padding(gray_img , pad)
        
        #padding_img = padding()
        result = np.array(([0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0]))

        thresh_value , binary_image = cv2.threshold(img,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        
        
        row= img.shape[0]
        column = img.shape[1] 
        new_img = np.zeros((row , column) , dtype="uint8")
        
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
               
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
                   
                    
        return new_img
    
    
    
    
    def maxpooling(gray_img , fil):
        img = gray_img.copy()
        pad = fil.shape[0]
        
        #padding_img = padding()
        
        zero_padding_img = padding.zero_padding(gray_img , pad)
        


        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                
                for k in range(5):
                    for l in range(5):
                        
                        fil[k][l] = zero_padding_img[img_row+k , img_col+l]
                        

                img[img_row][img_col] = np.max(fil)  
                

        return img
    
    
    def minpooling(gray_img , fil):
        img = gray_img.copy()
        pad = fil.shape[0]
        
        #padding_img = padding()
        
        zero_padding_img = padding.zero_padding(gray_img , pad)
        


        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                
                for k in range(5):
                    for l in range(5):
                        
                        fil[k][l] = zero_padding_img[img_row+k , img_col+l]
                        

                img[img_row][img_col] = np.min(fil)  
                

        return img
    
    
    
    
    
class convolution:
    def mean_filter(gray_img , fil):
        rows = fil.shape[0]
        col = fil.shape[1]
        
        conv_fil = np.zeros(shape=(rows , col))
        for i in range(rows):
            for j in range(col):
                
                r = (rows-1)-i
                c = (col-1)-j
                conv_fil[i,j] = fil[r,c]
                
        mean_img = correlation.mean_filter(gray_img, conv_fil)
        return mean_img
    
    
    def other_filters(gray_img , fil):
        rows = fil.shape[0]
        col = fil.shape[1]
        
        conv_fil = np.zeros(shape=(rows , col))
        for i in range(rows):
            for j in range(col):
                
                r = (rows-1)-i
                c = (col-1)-j
                conv_fil[i,j] = fil[r,c]
                
        mean_img = correlation.mean_filter(gray_img, conv_fil)
        return mean_img
    
    
    
    
    

class histogram:
    def histogram_equalization(gray_img):
        img = gray_img.copy()
        
        pixel_cal = np.zeros(shape=(1,256))

        rows = img.shape[0]
        col = img.shape[1]

        for img_row in range(rows):
            for img_col in range(col):
                k = gray_img[img_row , img_col]
                pixel_cal[0,k] = pixel_cal[0,k]+1


        com_sum = np.array([])
        com_sum = np.append(com_sum , pixel_cal[0,0])
        for i in range(255):
                k= com_sum[i]+pixel_cal[0,i+1]
                com_sum = np.append(com_sum , k)
                  
                
        com_sum = np.round((com_sum/(rows*col) * (255)))

        for img_row in range(rows):
            for img_col in range(col):
                k = img[img_row , img_col]
                img[img_row , img_col] = com_sum[k ]
    
        return img


    

    def contrast_stretching(gray_img):
        img = gray_img.copy()
        
        pixel_cal = np.zeros(shape=(1,256))

        rows = img.shape[0]
        col = img.shape[1]


        for img_row in range(rows):
            for img_col in range(col):
                k = gray_img[img_row , img_col]
                pixel_cal[0,k] = pixel_cal[0,k]+1



        y = np.zeros(shape=(1,256))

        for i in range(256):
            if pixel_cal[0,i]==0:
                y[0,i]=0
            else:
                y[0,i]=i


        MAX = np.max(y[np.nonzero(y)])
        MIN = np.min(y[np.nonzero(y)])

        stretch = np.round(((255-0)/(MAX-MIN))*(y-MIN))
        stretch[stretch<0] = 0
        stretch[stretch>255] = 255


        for img_row in range(img.shape[0]):
            for img_col in range(img.shape[1]):
                k = img[img_row , img_col]
                img[img_row , img_col] = stretch[0,k]

        
        return img
    
    
    
    
        
    
    
    
img = cv2.imread("ali.jpg")
img2 = cv2.imread("ali.jpg",0)


#mean / Averaging filter

"""
mean_fil = np.array(([255,255,255],
               [255,255,255],
               [255,255,255]))*1/9

mean_img = correlation.mean_filter(img2 ,mean_fil)

cv2.imshow("orignal image", img)
cv2.imshow("mean image", mean_img)

"""


#median filter
"""
median_fil = np.array(([0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]))

median_img = correlation.median_filter(img2, median_fil)
cv2.imshow("orignal image", img)
cv2.imshow("median image", median_img)

"""



#others filters...

"""
fil2 = np.array(([255,0,0],
               [0,255,0],
               [0,0,255]))*1/9

fil3 = np.array(([255,255,255],
               [0,0,0],
               [0,0,0]))*1/9

fil4 = np.array(([255,0,0],
               [255,255,255],
               [255,0,255]))*1/9

sobel_y = np.array(([1,0,-1],
               [2,0,-2],
               [1,0,-1]))

sobel_x = np.array(([1,2,1],
                [0,0,0],
                [-1,-2,-1]))


laplacian1 = np.array(([0,-1,0],
                       [-1,4,-1],
                       [0,-1,0]))

laplacian2 = np.array(([-1,-1,-1],
                       [-1,4,-1],
                       [-1,-1,-1]))




filter2 = correlation.other_filters(img2,fil2)
filter3 = correlation.other_filters(img2,fil3)
filter4 = correlation.other_filters(img2,fil4)
filter5 = correlation.other_filters(img2,sobel_y)
filter6 = correlation.other_filters(img2,sobel_x)
filter7 = correlation.other_filters(img2,laplacian1)
filter8 = correlation.other_filters(img2,laplacian2)




conv_filter2 = convolution.other_filters(img2,fil2)
conv_filter3 = convolution.other_filters(img2,fil3)
conv_filter4 = convolution.other_filters(img2,fil4)
conv_filter5 = convolution.other_filters(img2,sobel_y)
conv_filter6 = convolution.other_filters(img2,sobel_x)
conv_filter7 = convolution.other_filters(img2,laplacian1)
conv_filter8 = convolution.other_filters(img2,laplacian2)


cv2.imshow("filter2", filter2)
cv2.imshow("filter3", filter3)
cv2.imshow("filter4", filter4)
cv2.imshow("sobel", filter5)
cv2.imshow("sobel1", filter6)
cv2.imshow("laplacianl1", filter7)
cv2.imshow("laplacianl2", filter8)

cv2.imshow("convolution filter2", conv_filter2)
cv2.imshow("convolution filter3", conv_filter3)
cv2.imshow("convolution filter4", conv_filter4)
cv2.imshow("convolution sobel", conv_filter5)
cv2.imshow("convolution sobel1", conv_filter6)
cv2.imshow("convolution laplacianl1", conv_filter7)
cv2.imshow("convolution laplacianl2", conv_filter8)
"""


#erosion filter.........
"""
erosion_fil = np.array(([255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255]))

binary_img = cv2.imread("ali1.png")
binary_gray_img = cv2.imread("ali1.png",0)

erosion_img = correlation.erosion_filters(binary_gray_img , erosion_fil)
cv2.imshow("orignal erosion image", binary_img)
cv2.imshow("erosion image", erosion_img)
"""


#dialation filter.........
"""
dialation_fil = np.array(([255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255],
               [255,255,255,255,255,255,255]))

binary_img = cv2.imread("ali1.png")
binary_gray_img = cv2.imread("ali1.png",0)

dialation_img = correlation.dialation_filters(binary_gray_img , dialation_fil)
cv2.imshow("orignal dialtion image", binary_img)
cv2.imshow("dialated image", dialation_img)
"""






#histogram equalization...
"""
equlized_img = histogram.histogram_equalization(img2)
plt.hist(img2.flat , bins = 100 , range=(0,255))
#plt.hist(equlized_img.flat , bins = 100 , range=(0,255))
plt.show()
cv2.imshow("equalized image", equlized_img)
cv2.imshow("orignal image", img2)
"""


#contrast stretching................

"""
low_contrast_img = cv2.imread("low contrast.jfif")
gray_low_contrast_img = cv2.imread("low contrast.jfif" ,0)

contrast_stretching_img = histogram.contrast_stretching(gray_low_contrast_img)
cv2.imshow("low contrast image", gray_low_contrast_img)
cv2.imshow("contrast_stretching_img", contrast_stretching_img)

#plt.hist(gray_low_contrast_img.flat , bins = 100 , range=(0,255))
plt.hist(contrast_stretching_img.flat , bins = 100 , range=(0,255))
plt.show()
  
"""

#maxpooling.....
max_fil = np.array(([0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]))

maxpooling_img = correlation.maxpooling(img2, max_fil)
cv2.imshow("orignal image", img)
cv2.imshow("gray image", img2)
cv2.imshow("maxpooling image", maxpooling_img)




#minpooling.....
min_fil = np.array(([0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]))

minpooling_img = correlation.minpooling(img2, max_fil)
cv2.imshow("orignal image", img)
cv2.imshow("gray image", img2)
cv2.imshow("minpooling image", minpooling_img)




cv2.waitKey(0)
cv2.destroyAllWindows()