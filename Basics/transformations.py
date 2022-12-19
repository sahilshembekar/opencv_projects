import cv2 as cv

img = cv.imread('Photos/boston.jpg')

cv.imshow('Boston', img)


cv.waitKey(0)