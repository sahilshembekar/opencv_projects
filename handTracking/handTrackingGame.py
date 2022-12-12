import cv2
import mediapipe as mp
import time
import handTrackingModule as htm


pTime = 0 
cTime = 0
cap = cv2.VideoCapture(0)

detector = htm.handDetector() # with default params
while True:
    
    success, img = cap.read()
    
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0: # print only when there is something in list
        print(lmList[4]) 
        # will give us the postion of the tip of the thumb #change based on what you need by referring the image
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3) 
    
    cv2.imshow("Image", img)
    cv2.waitKey(1) 
