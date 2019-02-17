import cv2
import numpy as np

# Load two images
img2 = cv2.imread('whiteinblack.png',cv2.IMREAD_GRAYSCALE)


mask_inv = cv2.bitwise_not(img2)
cv2.imshow('mask_inv',mask_inv)

#cv2.imshow('img2gray',img2gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
