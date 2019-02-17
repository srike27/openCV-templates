import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
kernel = np.ones((5,5))
k=0
imgo = np.zeros((480,640))

def deflicker(img):
	global imgo
	kp = 0.5
	i=0
	j=0
	a=np.shape(img)
	thresh = 20
	print a
	w = a[0]
	h = a[1]
	fimg = np.zeros(a)
	print np.shape(fimg)
	d = img - imgo
	if np.sum(d)>1*480*640:
		fimg = img + d/50
	imgo = img
			
	return fimg
			






while(True):
	ret, frame = cap.read()
	frameo = frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(frame, (15,15) , 0)
	frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
	cv2.imshow('flicker',gray)
	gf = deflicker(gray)
	cv2.imshow('df',gf)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()