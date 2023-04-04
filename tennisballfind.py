import cv2
import numpy as np 
import imutils

cap= cv2.VideoCapture (0)
cap.set (3,640)
cap.set (4,480)

while True:
  _frame= cap.read()
  
  hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)
  
  lower_red = np.array ([0,50,120])
  upper_red = np.array ([10,255,255])
  
  mask = cv2.inRange (hsv,lower_red, upper_red)
  
  cnts = cv2.findContours (mask, cv2.RETR_TREE,cV2.CHAIN_APPROX_SIMPLE)
  cnts = imutils.grab_contours (cnts)
  
  for c in cnts:
    area = cv2.contourArea(c)
    if area > 5000:
    
      cv2.drawContours (frame, [c], -1, (0,255,0), 3)
  
      M = cv2.moments(c)
  
      cx = int (M["m10"]/ M["m00"])
      cy = int(M["m01"/ M["m00"])
  
      cv2.circle (frame, (cx,cy),7, (255,255,255), -1)
  
  cv2.imshow ("result",frame)

  k = cv2.waitKey (5)
  if k == 27:
    break
cap.release()
cv2.destroyAllWindows()
