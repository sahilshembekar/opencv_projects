import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200

while True:
    success, img = cap.read()
    
    # convenient for moving around virtual objects
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList: # hand is available
        cursor = lmList[8] # x,y of tip

        # check if our finger i.e. x and y of cursor is within the rectangle
        # with static values
        #if  cx < cursor[0] < 300 and 100 < cursor[1] < 300: 

        # with dyanmic values
        if  cx - w // 2 < cursor[0] < cx + w // 2and \
            cy - h // 2  < cursor[1] < cy + h // 2:
            colorR = 0, 255, 0 # change the color of rectangle
        else :
            colorR = 255, 0, 255 # change it to default value
    
    # check if we have clicked or not
    
    # static values
    # cv2.rectangle(img, (100,100),(300,300), colorR , cv2.FILLED) 
    
    # dynamic values
    cv2.rectangle(img, (cx - w//2,cy - h//2),(cx + w//2,cy + h//2), colorR , cv2.FILLED)
    
    cv2.imshow("Image", img)

    cv2.waitKey(1)

