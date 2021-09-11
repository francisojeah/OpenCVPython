import cv2
import numpy as np

img = cv2.imread("Resources/card.jpeg")
#size of a plain card
width,height = 250,350
#define the 4 corner points, use paint to find it
point1 = np.float32([[150,30],[470,65],[415,520],[100,480]])
point2 = np.float32([[0,0],[width,0],[width,height],[0,height],])

matrix = cv2.getPerspectiveTransform(point1,point2)
#Get image output
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)

