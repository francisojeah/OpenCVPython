#For camera
import cv2
#0 is for the default webcam
cap = cv2.VideoCapture(0)
#.set is for size: 3 is for width and 4 is for height
cap.set(3,640)
cap.set(4,480)

#Video is a sequence of images
#Need a while loop to loop through each frame
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    #Used to stop the video when 'q' is pressed
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break