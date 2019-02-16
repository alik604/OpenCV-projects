import cv2 as cv2
import numpy as np

# img = cv2.imread("tetris_blocks.png")
# resized = cv2.resize(img, (900, 900))
# gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #convert to grayScale
# thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
#
# #resized = cv2.Canny(resized, 30, 150) #egde detection
#
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#                         cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# output = gray.copy()
#
# cv2.imshow("Contours", output)
# cv2.waitKey(0)
#
# #cv2.imshow("resized", resized)

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    #ret, img = cap.read()
    img = cv2.imread("i.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()