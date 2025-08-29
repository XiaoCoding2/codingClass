
import numpy as np
import cv2 as cv

 
cap = cv.VideoCapture(0)
 
while(1):
 
    # Take each frame
    _, frame = cap.read()
 
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lower_green = np.array([40, 100, 50])
    upper_green = np.array([80, 255, 255])
    #
    lower_blue = np.array([100,40,40])
    upper_blue = np.array([130,255,255])
 
    # Threshold the HSV image
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv.inRange(hsv, lower_green, upper_green)

    blue_and_green=cv.bitwise_or(mask, mask2)
 
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    res2 = cv.bitwise_and(frame, frame, mask= mask2)
    res3=cv.bitwise_and(frame, frame, mask=blue_and_green)
 
    cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    cv.imshow('res',res)
    cv.imshow('res2',res2)
    cv.imshow('res3', res3)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv.destroyAllWindows()