import cv2 as cv
# Read an image
img = cv.imread("irum.jpg")
cv.imshow("Original Image",img)
cv.waitKey(0)
# Write an image
#cv.imwrite("Output.jpg",img )

#Info of image
#print(img.shape)

# Conversion to Gray Scale

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale Image",gray_img)
#cv.imwrite("Gray Scale Image.jpg",gray_img)
cv.waitKey(0)



# Convert To Binary
ret,bw = cv.threshold(gray_img,120,255,cv.THRESH_BINARY)
cv.imshow("Binary",bw)
cv.waitKey(0)         
cv.destroyAllWindows()