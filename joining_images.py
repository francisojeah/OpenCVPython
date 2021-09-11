import cv2
import numpy as np
img = cv2.imread('Resources/Adanna.jpeg')
'''
Downside of this method
It does not resize, uses orignial size if you want to stack more
it would not work if the images are not in the same chanel, eg. greyscale and bgr
'''
# #horizontal stacking
# imgHor = np.hstack((img,img))
# #vertical stacking
# imgVer = np.vstack((img,img))
# #solution
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shaape[0]
    if rowsAvailable:
        for x in range(0,rows):
            for y in range(o,cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0,0), None)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0]))
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.colorChange
        imageBlank = np.zeros((height,width,3), np.uint8)


# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)