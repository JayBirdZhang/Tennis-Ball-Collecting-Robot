#import needed libraries
import cv2
import numpy as np 
import imutils

cap= cv2.VideoCapture(0)
cap.set (3,640)
cap.set (4,480)

#create window for sliders
cv2.namedWindow('sliders')

def slide(val):
  pass
  
#create the sliders
cv2.createTrackbar('red min', 'sliders', 0, 255, slide)
cv2.createTrackbar('green min', 'sliders', 0, 255, slide)
cv2.createTrackbar('blue min', 'sliders', 0, 255, slide)

cv2.createTrackbar('red max', 'sliders', 0, 255, slide)
cv2.createTrackbar('green max', 'sliders', 0, 255, slide)
cv2.createTrackbar('blue max', 'sliders', 0, 255, slide)

while True:
  rMin = cv2.getTrackbarPos('red min', 'sliders')
  gMin = cv2.getTrackbarPos('green min', 'sliders')
  bMin = cv2.getTrackbarPos('blue min', 'sliders')
  
  rMax = cv2.getTrackbarPos('red max', 'sliders')
  gMax = cv2.getTrackbarPos('green max', 'sliders')
  bMax = cv2.getTrackbarPos('blue max', 'sliders')
  
  _,frame= cap.read()
  
  hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)
  
  lower_red = np.array ([rMin,gMin,bMin])
  upper_red = np.array ([rMax,gMax,bMax])
  
  mask = cv2.inRange (hsv,lower_red, upper_red)
  
  cnts = cv2.findContours (mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cnts = imutils.grab_contours (cnts)
  
  for c in cnts:
    area = cv2.contourArea(c)
    if area > 5000:
    
      cv2.drawContours (frame, [c], -1, (0,255,0), 3)
  
      M = cv2.moments(c)
  
      cx = int (M["m10"]/ M["m00"])
      cy = int (M["m01"]/ M["m00"])
  
      cv2.circle (frame, (cx,cy),7, (255,255,255), -1)
  
  cv2.imshow ("result",frame)

  if cv2.waitKey(1) & 0xFF ==ord('q'): 
    break
cap.release()
cv2.destroyAllWindows()
