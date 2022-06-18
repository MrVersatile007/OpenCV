## COLOR DETECTION


from unittest import result
import cv2
import numpy as np


frameHeight = 480
frameWidth = 640
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth) #3 is Width in terms of ID
cap.set(4,frameHeight) #4 is Height in terms of ID
cap.set(10, 100) #10 is Brightness in terms of ID

def empty(a):
    pass


cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:

    _, img = cap.read()
    

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSV : HUE SATURATION VALUE

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")

    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")

    v_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Sat Max", "TrackBars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask= mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, imgResult])

    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()