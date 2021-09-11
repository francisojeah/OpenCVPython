import cv2
import numpy as np
#.zeros for black and .ones for white
img = np.zeros((512,512,3),np.uint8)
#print(img)
#To colour image height by width
#img[200:300, 100:300] = 255,0,0

#For lines. image beginning, end, colour, thickness
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),3)
#draw rectangles, cv2.FILLED is to fill shape
cv2.rectangle(img,(0,0),(350,350),(0,0,255),cv2.FILLED)
#to draw circles
cv2.circle(img, (400,50),30,(255,255,0),5)

#To put text on images
cv2.putText(img, "OpenCv",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imshow("Image",img)


cv2.waitKey(0)