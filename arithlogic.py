import cv2
import numpy as np

# Load two images
img2 = cv2.imread('rmilogo.jpg',cv2.IMREAD_GRAYSCALE)

ret, mask = cv2.threshold(img2, 50, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
img2 = cv2.add(img2,mask_inv,0)
mask2= cv2.bitwise_and(mask,mask_inv,0)
cv2.imshow('img2',mask)
cv2.imshow('mask_inv',mask2)

#cv2.imshow('img2gray',img2gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
