#RESIZING AND CROPPING


import cv2


img = cv2.imread("Resources/Uzui.jpg")
print(img.shape) #(512, 512, 3) (height, width, layers) 

imgResize = cv2.resize(img, (250, 300)) #need to follow (width, height) order
print(imgResize.shape)

imgCropped = img[: , 100:400] #This is just like cropping matrix

cv2.imshow("Original Output", img)
cv2.imshow("Resize Output", imgResize)
cv2.imshow("Cropped Output", imgCropped)
cv2.waitKey(0)