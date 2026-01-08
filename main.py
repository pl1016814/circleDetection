import numpy as np
import cv2 as cv

img = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
img = cv.GaussianBlur(img, (5,5), 0)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1.33, 200,
                          param1=120, param2=100, minRadius=800, maxRadius=2000)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv.imshow('detected circles', cimg)
cv.waitKey(0)
cv.destroyAllWindows()
