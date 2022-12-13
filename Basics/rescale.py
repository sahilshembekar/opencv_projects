import cv2 as cv

def changeResolution(width, height):
    # only work for live videos
    capture.set(3,width)
    capture.set(4,height)

def rescaleFrame(frame, scale=0.75):
    # Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height) # tuple

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading Images
img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)


resized_image = rescaleFrame(img)

cv.imshow("Resized Image", resized_image)

# Reading videos

capture = cv.VideoCapture('Videos/dog.mp4') #0 for webcam, 1 is external cam 1

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    
    if cv.waitKey(20) & 0xFF==ord('d'): 
        # if key d is pressed then exit
        break

capture.release()
cv.destroyAllWindows()
