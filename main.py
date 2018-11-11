from cv2 import *
import tempfile
from cfR import *
from time import sleep

camera = VideoCapture(0)

threatScore = 0
while True:
    valid, img = camera.read()
    if valid:
        imwrite("tmpimg.jpg", img)
        
        with open("tmpimg.jpg", 'rb') as i:
            data = i.read()
        imgScore = frCheck(data)
        print("Frame Score: "+str(imgScore))
        threatScore += imgScore
        
        if imgScore == 0:
            if threatScore > 0:
                threatScore -= 1
            if threatScore < 0:
                threatScore += 1
            
        if threatScore < -50:
            threatScore = -50
        elif threatScore > 100:
            threatScore = 100
        
        print("Threat Score: "+str(threatScore))

    else:
        print("Image error")

    sleep(1)
