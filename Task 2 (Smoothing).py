import cv2 as cv
 

img = cv.imread('irum.jpg')
  
# By Averaging
#avging = cv.blur(img,(10,10))
  
#cv.imshow('Averaging',avging)
#cv.waitKey(0)
 
# Gaussian Blurring

gausBlur = cv.GaussianBlur(img, (29,29),0) 
cv.imshow('Gaussian Blurring', gausBlur)
cv.waitKey(0)
 
# Median blurring
medBlur = cv.medianBlur(img,13)
cv.imshow('Media Blurring', medBlur)
cv.imwrite("Output1.jpg",medBlur)
cv.waitKey(0)
 
# Bilateral Filtering
bilFilter = cv.bilateralFilter(img,27,75,75)
cv.imshow('Bilateral Filtering', bilFilter)
cv.imwrite("Output.jpg",bilFilter)
cv.waitKey(0)
cv.destroyAllWindows()