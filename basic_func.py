import cv2
import numpy as np
img = cv2.imread("Resources/pic.jpg")
'''
Define the kernel
.ones() makes arrays of 1's
'''
kernel = np.ones((5,5),np.uint8)

print(kernel)

#convert to grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
'''
blur image 
(,)ksize has to be odd numbers, as the number increases so does the intensity
sigmaX is 0
'''
imgBlur = cv2.GaussianBlur(img, (11,11),0)
'''
canny edge detector
100,100 is the threshold value; the lower, the more edges
'''
imgCanny = cv2.Canny(img, 100,100)
'''
To dialate images to increase thickness of egdes
kernel is a matrix
iteration is for thickness levels
 '''
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
'''
erosion is the opposite of dialation
makes thinner
'''
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Dialation Image', imgDialation)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)