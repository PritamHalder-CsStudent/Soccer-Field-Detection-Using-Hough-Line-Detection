import cv2 as cv
import numpy as np
import matplotlib

#from glob import glob

frame = cv.imread('sample1.png')

frame = cv.resize(frame, (640, 480))

hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_green = np.array([36,0,0])
upper_green = np.array([86,255,255])
# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_green, upper_green)
# Bitwise-AND mask and original image
res = cv.bitwise_and(frame,frame, mask= mask)
#cv.imshow('frame',frame)
#cv.imshow('mask',mask)
cv.imshow('res',res)
cv.imwrite("samout1.png",res)
 #segmented image


cv.waitKey(0)
cv.destroyAllWindows()