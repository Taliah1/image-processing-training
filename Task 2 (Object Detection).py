import cv2 as cv
import numpy as np
 
cap = cv.VideoCapture(0)
 
while True:
    _, frame = cap.read()
    blurred_frame = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)
 
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)
 
    _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
 
    for contour in contours:
        area = cv.contourArea(contour)
 
        if area > 500:
            cv.drawContours(frame, contour, -1, (0, 255, 0), 3)
 
 
    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
 
    key = cv.waitKey(0)
    if key == 27:
        break
 
cap.release()
cv.destroyAllWindows()