


# Import Library

import cv2
import numpy as np
"""
# Read & Show Image
 
img = cv2.imread("aa.jpg")
img = cv2.resize(img,(int(img.shape[1]*0.5), int(img.shape[0]*0.5)))
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
img
 
img.shape
 
959*640
 
img.size
        
"""




#Access Single Pixel of Image

"""
# # Access Single Pixel of Image
 
img[0,0]
 
img[0,0, 0]
 
img[0,0, 1]
 
img[0,0, 2]
 
img[0][0]
 
img[200,100]
 
img[900, 150]
 
img[180, 550]

"""





#Show single pixel of Image as Image

"""

2
3
4
# # Show single pixel of Image as Image
cv2.imshow("image", img[900, 150])
cv2.waitKey(0)
cv2.destroyAllWindows()

"""




#Access the row of Image

"""
img[0]
 
img[0].shape
 
img[0, :]
 
img[700, :]

"""



#Access the row of single & double channel Image

"""
img[700, :, 2]
 
img[700, :, (0,1)]
 
img[700, :, (2,1,0)]
 
cv2.imshow("image", img[:, :, (1,0,2)])
cv2.waitKey(0)
cv2.destroyAllWindows()

"""




#Access the column of Image

"""
img[:, 0]
 
img[:, 200]

"""




#Access the column of single & double channel Image

"""
img[:, 200, 2]
 
img[:, 200, (1,2)]
 
img[:, 200, (1,2)].shape

"""



#Access the part of Image

"""
img[80:400, 100:450] # [y1:y2, x1:x2] #, x1= 100, y1=80, x2= 450   y2= 400
 
cv2.imshow("image", img[80:400, 100:450])
cv2.waitKey(0)
cv2.destroyAllWindows()
 
x1 = 150, y1 = 850, x2 = 550, y2 = 900
 
cv2.imshow("image", img[750:900, 220:400])
cv2.imwrite("img_part.jpg", img[750:900, 220:400])
cv2.waitKey(0)
cv2.destroyAllWindows()

"""


#Show image Row wise

"""
for i in range(img.shape[0]):
    cv2.imshow("image", img[0:i+1, :])
 
    if cv2.waitKey(27) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()


"""




#Show image Column wise

"""
for i in range(img.shape[1]):
    cv2.imshow("image", img[:, 0:i+1])
 
    if cv2.waitKey(27) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()


"""