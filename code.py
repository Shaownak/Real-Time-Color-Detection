import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()
    
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    # Red Color
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv.inRange(img_hsv, low_red, high_red)
    red = cv.bitwise_and(img ,img, mask=red_mask)

    # Blue Color
    low_blue = np.array([94,80,2])
    high_blue = np.array([126,255,255])
    blue_mask = cv.inRange(img_hsv, low_blue, high_blue)
    blue = cv.bitwise_and(img, img, mask = blue_mask)

    # Green Color
    low_green = np.array([25,52,72])
    high_green = np.array([102,255,255])
    green_mask = cv.inRange(img_hsv, low_green, high_green)
    green = cv.bitwise_and(img, img, mask = green_mask)



    cv.imshow("Image", img)
    cv.imshow("Red Image", red)
    cv.imshow("Green Image", green)
    cv.imshow("Blue Image", blue)


    cv.imshow("Image", img)
    cv.waitKey(1)
