import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200

class DragRect():
    def __init__(self, posCenter, size=[200,200]) :
        self.posCenter = posCenter
        self.size = size


    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size 
        
        # check if our finger i.e. x and y of cursor is within the rectangle
        # with static values
        #if  cx < cursor[0] < 300 and 100 < cursor[1] < 300: 

        # with dyanmic values
        if  cx - w // 2 < cursor[0] < cx + w // 2 and \
            cy - h // 2  < cursor[1] < cy + h // 2:
            colorR = 0, 255, 0 # change the color of rectangle

            # Drag operation
            self.posCenter = cursor

# to make multiple rectangles
rectList = []

for x in range(5):
    rectList.append(DragRect([x*250+150,150]))


while True:
    success, img = cap.read()
    
    # convenient for moving around virtual objects
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList: # hand is available
        
        # distance between tip of index and tip of middle finger
        l, _, _ = detector.findDistance(8, 12, img, draw=False) 
        
        if l < 30 : # click operation
            cursor = lmList[8] # x,y of tip
            for rect in rectList:
                rect.update(cursor)

    # # to draw Solid
    # for rect in rectList:
    #     cx, cy = rect.posCenter
    #     w, h = rect.size 
        
    #     # check if we have clicked or not
        
    #     # static values
    #     # cv2.rectangle(img, (100,100),(300,300), colorR , cv2.FILLED) 
        
    #     # dynamic values
    #     cv2.rectangle(img, (cx - w//2,cy - h//2),
    #                 (cx + w//2,cy + h//2), colorR , cv2.FILLED)
    #     cvzone.cornerRect(img, (cx - w//2,cy - h//2, w, h), 20, rt = 0)

    # Draw with transparent rectangle

    imgNew = np.zeros_like(img, np.uint8)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size 
        
        # check if we have clicked or not
        
        # static values
        # cv2.rectangle(img, (100,100),(300,300), colorR , cv2.FILLED) 
        
        # dynamic values
        cv2.rectangle(imgNew, (cx - w//2,cy - h//2),
                    (cx + w//2,cy + h//2), colorR , cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx - w//2,cy - h//2, w, h), 20, rt = 0)
    
    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]



    cv2.imshow("Image", out)

    cv2.waitKey(1)

