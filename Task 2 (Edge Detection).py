# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 01:10:14 2018

@author: Taliah Chitti
"""

import cv2 as cv
# Using Sobel 
img = cv.imread('irum.jpg',cv.IMREAD_GRAYSCALE)
rows,cols = img.shape
 
sobel_horizontal = cv.Sobel(img,cv.CV_64F,1,0,ksize = 5)
sobel_vertical = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
 
cv.imshow('Original',img)
cv.imshow('Sobel Horizontal Filter',sobel_horizontal)
cv.imshow('Sobel Vertical Filter',sobel_vertical)
cv.waitKey(0)

#Using Laplacian
 
#img = cv.imread('GIG.png',cv.IMREAD_GRAYSCALE)
rows,cols = img.shape
 
denoised = cv.GaussianBlur(img,(5,5),0)
filter = cv.Laplacian(denoised,cv.CV_64F)
 
cv.imshow('Original',img)
cv.imshow('Laplacian Filter',filter)
cv.waitKey(0)

#Using Canny
#img = cv.imread('GIG.png',cv.IMREAD_GRAYSCALE)
filter = cv.Canny(img,100,200)
cv.imshow('Original',img)
cv.imshow('Canny Filter',filter) 
cv.waitKey(0)
 
cv.destroyAllWindows()
