#Main Homography

import cv2
import numpy as np

source = cv2.imread('sample1.png')
source = cv2.resize(source, (640, 480))
cv2.imshow("Source Image", source)
pts_src = np.array([ [186,424],[412,510],[327,187],[128,250]])


destination = cv2.imread('FieldDiagram.png')
cv2.imshow("Destination Image", destination)
pts_dst = np.array([[12,397],[125, 397],[125,125],[12,135]])

h,status = cv2.findHomography(pts_src, pts_dst)
im_out = cv2.warpPerspective(source, h, (destination.shape[1],destination.shape[0]))
cv2.imshow("Warped Source Image", im_out)
cv2.imwrite("homo1.png",im_out)
#cv2.imwrite('outputD2.jpg',im_out)

cv2.waitKey(0)