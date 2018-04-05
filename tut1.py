import cv2
import matplotlib as plt
import numpy as np
#using cv itself
img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
