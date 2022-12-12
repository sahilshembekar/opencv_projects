import cv2
import time
import numpy as np
import handTrackingModule as htm
import math

# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

####################
wCam, hCam = 640, 480
####################

cap = cv2.VideoCapture(0)

# To change the value of cap
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionConfidence=0.7)



# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# #volume.GetMute()
# #volume.GetMasterVolumeLevel()
# print(volume.GetVolumeRange())
# volume.SetMasterVolumeLevel(-20.0, None)

'''
For people working on Linux use:
from subprocess import call
volume = int(volume)
call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
'''

while True:
    
    success, img = cap.read()
    img = detector.findHands(img)

    # to get the positions
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) !=0:
        #print(lmList[4], lmList[8]) #tip of thumb, index finger

        x1, y1 = lmList[4][1], lmList[4][2] #x,y of thumb tip
        x2, y2 = lmList[8][1], lmList[8][2] #x,y of index tip
        cx, cy = (x1+x2)//2, (y1+y2)//2 # center of the line # floor division


        cv2.circle(img, (x1,y1), 7, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 7, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255, 0, 255), 3)
        
        cv2.circle(img, (cx,cy), 7, (255, 0, 255), cv2.FILLED)
         
        length = math.hypot(x2-x1,y2-y1)
        
        print(length)
        
        if length < 50:
            cv2.circle(img, (cx,cy), 7, (0, 255, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1) 

