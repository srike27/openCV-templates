import cv2
import numpy as np

img = cv2.imread('rmilogo.jpg',cv2.IMREAD_COLOR)
# basically the image is a 3 2D signals of variables x and y
# the top corner of the image is the origin down is +ve y and right is +ve x


print(img[100,100])

#img[100:150,100:150] = [0,0,0]
for i in range(6):
    cv2.imshow('image',img)
    img*=img
    cv2.waitKey(0)
    cv2.destroyAllWindows()
