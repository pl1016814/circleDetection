# import cv2
# import numpy as np
# imagePath = "./image.png"
# jabba = cv2.imread(imagePath, 0)
# #jabba = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale
# kabba = cv2.HoughCircles(jabba, cv2.HOUGH_GRADIENT, 1, 20)
# print(kabba)
# kabba = kabba.astype(np.float32)
# cv2.circle(kabba, (kabba[0], kabba[1]), kabba[2], (255,0,0), 2)
# cv2.imshow("Display", jabba)
# cv2.waitKey(0)
