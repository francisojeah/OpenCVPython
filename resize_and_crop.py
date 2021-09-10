import cv2
import numpy as np
#Image is an array of pixels
img = cv2.imread("Resources/adanna.jpeg")
#To find the size of image (height, width, number for chanel bgr(3)
print(img.shape)

#To resize image width by height
imgResize = cv2.resize(img,(400,500))
print(imgResize.shape)

#To crop
imgCropped = img[400:800,400:700]
#cv2.imshow("Image",img)
#cv2.imshow("Image Resize", imgResize)
cv2.imshow("Cropped Resize", imgCropped)
cv2.waitKey(0)