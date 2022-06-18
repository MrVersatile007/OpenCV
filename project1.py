import cv2
import numpy as np


frameHeight = 480
frameWidth = 640
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth) #3 is Width in terms of ID
cap.set(4,frameHeight) #4 is Height in terms of ID
cap.set(10, 100) #10 is Brightness in terms of ID

myColors = [#[156,122,0,179,209,255],             #Pink
            #[97,106,0,106,255,255],              #Blue
            #[174, 179, 162, 252, 162, 252],      #Red
            [163, 168, 123, 251, 123, 251]]        #Pink

myColorvalues = [#[255, 0, 255],
                #[255,0,0],
                #[0,0,255],
                [255,0,255]]

def findColor(img, myColors, myColorvalues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV, lower, upper)
        #cv2.imshow(str(color[0]), mask)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorvalues[count], cv2.FILLED)
        count +=1

def getContours(img):

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # Retrival method gives external details (contours), Approximation reduces the values like filtering
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
         
        if area > 50:  #This is good idea to do when there are small area contours they shall be neglected and focus on larger areas
            cv2.drawContours(imgResult, cnt, -1, (255,250,0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2, y

while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors, myColorvalues)
    cv2.imshow('Video', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break