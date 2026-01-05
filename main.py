import cv2
import numpy as np

image = pass
kabba = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale
kabba = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20)
kabba = kabba.astype(np.float32)
cv.circle(kabba, (kabba[0], kabba[1]), kabba[2], (255,0,0), 2)
