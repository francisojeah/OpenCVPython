#For images
import cv2
print("Package Imported")

#imread is to read image
im = cv2.imread("Resources/pic.jpg")

'''
.imshow is to display
It takes in 2 arguments, The name of the window and the variable name
'''
cv2.imshow('output', im)

'''
To delay the image .waitKey is used
parameter is in milliseconds so 1000 is for a second
0 is for infinity
'''
cv2.waitKey(0)

