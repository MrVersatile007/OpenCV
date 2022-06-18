#SHAPES AND TEXTS

#SHAPES

import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)


#print(img.shape)
#img[100:200, 100:300] = 255,200,0 #B,G,R

#DRAWING LINE

# cv2.line(img,(0,0), (34,340), (0,150,120),3) #(image, startpoint, end point, color, thickness)
# cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255,0,0), 2)

# cv2.rectangle(img,(25,250), (250,35), (0,0,255), cv2.FILLED) #(image, starting point of diagonal, end point of diagonal, color, thickness or fill)

# cv2.circle(img, (250, 350), 90, (250,255,0), 5)

# cv2.imshow('Image', img)
# cv2.waitKey(0)

#TEXTS

cv2.putText(img, " OPEN CV", (200,100), cv2.FONT_HERSHEY_COMPLEX, 1, (150,150,120), 3) #(image, text to print, starting point, font, scale, color, thickness)
cv2.imshow('Image', img)
cv2.waitKey(0)
