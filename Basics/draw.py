import cv2 as cv
import numpy as np

# create blank image to draw on
blank = np.zeros((500,500,3), dtype='uint8') # uint8 datatype is an image

# cv.imshow('Blank', blank)

# # Paint the image certain colour

# blank[:] = 0,255,0
# blank[200:300, 300:400] = 0,0,255 # insert another color for particular area

# cv.imshow('Green', blank)

# Draw a rectangle
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)

# to fill the rectangle with color
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)

#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)



# Check draw a circle, line,

# text on image

cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow('Text', blank)

cv.waitKey(0)

