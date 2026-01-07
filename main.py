import cv2
import numpy as np

imagePath = "image.png"
iabba = cv2.imread(imagePath, 0)
jabba = cv2.GaussianBlur(iabba, (5, 5), 0)
#jabba = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale
kabba = cv2.HoughCircles(jabba, cv2.HOUGH_GRADIENT, 1, 20)
#labba = kabba.reshape(-1,2)
labba = np.squeeze(kabba)
mabba = labba.astype(int)
cv2.circle(mabba, (int(mabba[0]), int(mabba[1])), int(mabba[2]), (255,0,0), 2)
cv2.imshow("Display", mabba)
cv2.waitKey(0)
