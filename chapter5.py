#WARP PERSPECTIVE

import numpy as np
import cv2

img = cv2.imread("Resources/cards.png")

width, height = 250,350

pts1 = np.float32([[1221,478], [1472,446], [1267,854], [1518,820]])
pts2 = np.float32([[0,0],[width,0],[0, height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow('Image', img)
cv2.imshow('Output Image', imgOutput)
cv2.waitKey(0)