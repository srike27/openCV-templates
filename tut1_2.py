import cv2
import matplotlib.pyplot as plt
import numpy as np
#using cv itself
img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow( img , cmap = 'gray', interpolation  = 'bicubic')
plt.plot([50,100],[80,100], 'c', lineWidth=5)
plt.show()
