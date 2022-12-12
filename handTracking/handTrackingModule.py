import cv2
import mediapipe as mp
import time

# converted the handTrackingmin.py to a module

class handDetector():
    def __init__(self, mode=False, MaxHands=2, complexity=1, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.MaxHands = MaxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence
        self.complexity = complexity


        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.MaxHands, self.complexity, self.detectionConfidence, self.trackConfidence)

        self.mpDraw = mp.solutions.drawing_utils 

    def findHands(self, img, draw=True):
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks: # if there is hand/ hands
            for handLms in self.results.multi_hand_landmarks: #handLms is a single hand
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    
    def findPosition(self, img, handNo=0, draw=True): # defualt is only for 1 hand and handNo points to a particular hand
        
        lmList= []
        
        if self.results.multi_hand_landmarks:
            
            myHand = self.results.multi_hand_landmarks[handNo]
            #gets the landmark and puts them in a list
            for id, lm in enumerate(myHand.landmark):
                #print(id,lm)
          
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h) # position of the center

                lmList.append([id, cx, cy]) 
                
                # print(id, cx,cy) # center for each id
                if draw:
                    cv2.circle(img, (cx,cy), 7, (255, 0, 0), cv2.FILLED)

        return lmList
            

def main():

    pTime = 0 
    cTime = 0
    cap = cv2.VideoCapture(0)

    detector = handDetector() # with default params
    while True:
        
        success, img = cap.read()
        
        img = detector.findHands(img)
        # img = detector.findHands(img) # hide the points of detected points
        lmList = detector.findPosition(img)
        # lmList = detector.findPosition(img, draw=False) # to hide the center
        
        if len(lmList) != 0: # print only when there is something in list
            print(lmList[4]) 
            # will give us the postion of the tip of the thumb #change based on what you need by referring the image
        
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3) 
        
        cv2.imshow("Image", img)
        cv2.waitKey(1) 


if __name__ == "__main__":
    main()
