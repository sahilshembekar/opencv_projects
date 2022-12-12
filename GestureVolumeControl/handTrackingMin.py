import cv2
import mediapipe as mp
import time # to check the frame rate

cap = cv2.VideoCapture(0)

# hand detection model

mpHands = mp.solutions.hands
hands = mpHands.Hands() # Default values are taken here if it is blank

# to draw multiple points
mpDraw = mp.solutions.drawing_utils 


# to calculate FPS
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    

    # convert image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # send RGB image to hands
    results = hands.process(imgRGB)

    # prints landmark (x,y,z) when hand is detected
    # print(results.multi_hand_landmarks)

    # extract the info and use it
    # to check if we have multiple hands and extract them 1by1

    if results.multi_hand_landmarks: # if there is hand/ hands
        for handLms in results.multi_hand_landmarks: #handLms is a single hand
            
            # get info within each hand & landmark info via ID number
            for id, lm in enumerate(handLms.landmark): #lm is our landmark and id is index number of the finger landmark 0 bottom 4 tip or something
                #print(id,lm)   
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h) # position of the center
                print(id, cx,cy) # center for each id

                # to use the cx, cy info 
                # can also put in a list and use it
                if id == 4:
                    cv2.circle(img, (cx,cy), 15, (255, 0, 255), cv2.FILLED)


        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) # we are displaying original hence, draw landmarks on that and not thr RGB image
            # .HAND_CONNECTIONS draws the lines connecting them


    # to calculate FPS
    cTime = time.time() # current time
    fps = 1/(cTime - pTime)
    pTime = cTime

    # to display text on the screen
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3) 
    
    # To run the webcam we do the below
    cv2.imshow("Image", img)
    cv2.waitKey(1) 