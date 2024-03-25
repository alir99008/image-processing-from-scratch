
import cv2

import numpy as np

img = cv2.imread("ali.jpg")
img1 = cv2.imread("ali.jpg",0)
img_rows = img1.shape[0]
img_columns = img1.shape[1]

"""
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



"""


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



stride = (3,5)
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


surface_pad_img = create_img(upper, lower, left, right)


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
    
    
cv2.imshow("gray image", img1)
cv2.imshow("new_img", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()