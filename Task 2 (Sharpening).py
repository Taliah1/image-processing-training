import cv2 as cv
import numpy as np

image = cv.imread('irum.jpg')
cv.imshow('Original', image)

kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])

sharpened = cv.filter2D(image, -1, kernel_sharpening)
cv.imshow('Image Sharpening', sharpened)
cv.waitKey(0)
cv.destroyAllWindows()
