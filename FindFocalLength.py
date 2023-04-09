# sudo apt install python3-openc
import cv2
import numpy as np
import imutils

# initialiser
camera1 = cv2.VideoCapture (0)
cv2.namedWindow("track", cv2.WINDOW_NORMAL)
def darken(img, brightness, contrast):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    shadow = 0
    max = 255 + brightness
    al_pha = (max - shadow) / 255
    ga_mma = shadow
    cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma)
    Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
    Gamma = 127 * (1 - Alpha)
    cal = cv2.addWeighted(cal, Alpha, cal, 0, Gamma)
    return cal
#set the minimum and maximum values for the detected colors
rMin = 25
gMin = 50
bMin = 105
  
rMax = 70
gMax = 255
bMax = 255

distance = 30

while True:
    ret1, frame1 = camera1.read()
    effect = darken(frame1, 160, 140)
    hsv = cv2.cvtColor (effect,cv2.COLOR_BGR2HSV)
  
    lower_green = np.array ([rMin,gMin,bMin])
    upper_green = np.array ([rMax,gMax,bMax])
  
    mask = cv2.inRange (hsv,lower_green, upper_green)
  
    cnts = cv2.findContours (mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours (cnts)
  
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 3000:
            cv2.drawContours (effect, [c], -1, (0,255,0), 3)
  
            M = cv2.moments(c)
  
            CenterX = int (M["m10"]/ M["m00"])
            CenterY = int (M["m01"]/ M["m00"])
            coords = (CenterX + 500,CenterY + 50)
            cv2.circle (effect, (CenterX,CenterY),7, (255,255,255), -1)
            cv2.putText(effect, str(coords), (CenterX,CenterY), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(effect,(x,y), (x+w,y+ h), (0,255,0), 4)

            focalLength = (w*distance/7)
            print(str(focalLength))

        cv2.imshow ("track",effect)
        cv2.resizeWindow("track",842,473)
        
    #if 'q' is pressed the created windows are destroyed and the program ends
    if cv2. waitKey(1) & 0xFF ==ord('q') :
        break
camera1.release ()
cv2.destroyAllWindows ()