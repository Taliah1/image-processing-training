
import cv2 as cv


cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv.imshow("Frame",frame)
    key = cv.waitKey(0)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()


