#For videos
import cv2
#.VideoCapture is used to capture video
cap = cv2.VideoCapture("Resources/vid.mp4")

#Video is a sequence of images
#Need a while loop to loop through each frame
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    #Used to stop the video when 'q' is pressed
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
