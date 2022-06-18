#BASIC FUNCTIONS

import cv2
import numpy as np

img = cv2.imread('Resources/Nezuko.jpg')
kernel = np.ones((5,5), np.uint8)

#Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#Blur image
imgBlur = cv2.GaussianBlur(img, (7,7), 0) 
#Edge detector
imgCanny = cv2.Canny(img, 150, 200)  
#Image Dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
#Image Erosion (opposite of dilation)
imgErode = cv2.erode(imgDilation, kernel, iterations= 1)

cv2.imshow('Original Image', img)
cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilation Image', imgDilation)
cv2.imshow('Erosion Image', imgErode)
cv2.waitKey(0)
