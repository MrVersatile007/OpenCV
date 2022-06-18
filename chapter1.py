#IMAGES - VIDEOS - WEBCAMS

import cv2

print('package imported')

## reading and showing image

img = cv2.imread("Resources/Rengoku.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)

## reading and showing video

# cap = cv2.VideoCapture("Resources/DemoVideo.mp4")

# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


## reading webcam and showing video

#frameHeight = 480
#frameWidth = 640
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth) #3 is Width in terms of ID
# cap.set(4,frameHeight) #4 is Height in terms of ID
# cap.set(10, 100) #10 is Brightness in terms of ID

# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break