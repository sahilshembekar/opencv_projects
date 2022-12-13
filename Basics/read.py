import cv2 as cv

# Reading Images
img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

# # Reading videos

# capture = cv.VideoCapture('Videos/dog.mp4') #0 for webcam, 1 is external cam 1

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'): 
#         # if key d is pressed then exit
#         break

# capture.release()
# cv.destroyAllWindows()

