import numpy as np
import cv2

img = cv2.imread('rmilogo.jpg',cv2.IMREAD_COLOR)


#draw line (obj,pt1,pt2,(r,g,b),linethickness)
cv2.line(img,(0,0),(200,300),(255,255,255),50)


#draw rectangle (obj,diagvert1,diagvert2,(r,g,b),line thickness)
cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)


#draw circle (obj, centre,  radius, (r,g,b), linethickness(-1 for fill))
cv2.circle(img,(447,63), 63, (0,255,0), -1)


#drawing a polygon
#creating an array of points using numpy and specifying datatype
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2)) #not sure about this line
#draw poly    (obj, arrayofpts, true, (r,g,b), linethickness)
cv2.polylines(img, [pts], True, (0,255,255), 3)


#writing on cv
#setting font
font = cv2.FONT_HERSHEY_SIMPLEX
#(obj,'text tobe inserted', (lextcornerx,leftcornery), fontsize, fontcolor, linethickness, idk)
cv2.putText(img,'OpenCV Tuts!',(10,500), font, 5, (200,255,155),10, cv2.LINE_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
