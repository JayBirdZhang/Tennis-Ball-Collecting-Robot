import cv2
import numpy as np


class TennisBalle:
    def __init__(self):
        self.ballCam = cv2.VideoCapture(1)
        self.basketCam = cv2.VideoCapture(0)
        self.framex = 1280/2
        self.framey = 720/2

    def detect(self):
        while True:
            ret, frame = self.ballCam.read()

            brightness_matrix = np.ones(frame.shape, dtype="uint8") * 60 #adjust this value for darkening and find the best option
                                                                         #hopefully raspberry pis do not have auto brightening camera features
            frame = cv2.subtract(frame, brightness_matrix)

            blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)

            filtered_frame = cv2.bilateralFilter(blurred_frame, 9, 75, 75)

            hsv = cv2.cvtColor(filtered_frame, cv2.COLOR_BGR2HSV)

            lower_green = np.array([25, 50, 105]) #changing the values to suit the tennis ball would be necessary
            upper_green = np.array([70, 255, 255]) #same

            mask = cv2.inRange(hsv, lower_green, upper_green)
            mask = cv2.dilate(mask, None, iterations=2)
            mask = cv2.erode(mask, None, iterations=1)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, param1=50, param2=30, minRadius=10, maxRadius=100)


            else:
                detected = {}


                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area > 100:
                        perimeter = cv2.arcLength(contour, True)
                        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
                        
                        if len(approx) > 6: #change this value for detected verticies
                            k = cv2.isContourConvex(approx)
                            if k:
                                (x, y), radius = cv2.minEnclosingCircle(contour)
                                center = (int(x), int(y))
                                radius = int(radius)
                                dist = actualBallWidth * focalLength / (2 * radius)
                                detected[dist] = contour
                                cv2.circle(frame, center, radius, (0, 255, 0), 2)

                            else:
                                (x, y), radius = cv2.minEnclosingCircle(contour)
                                center = (int(x), int(y))
                                radius = int(radius)
                                dist = actualBallWidth * focalLength / (2 * radius)
                                detected[dist] = contour
                                cv2.circle(frame, center, radius, (0, 255, 0), 2)


            if(len(detected) > 1):
                myKeys = list(detected.keys())
                myKeys.sort()
                key = myKeys[0]
                bigBall = detected[key]
                (x, y), radius = cv2.minEnclosingCircle(bigBall)
                dist = actualBallWidth * focalLength / (2 * radius)
                centerx = x + radius
                centery = y + radius
                #insert alignment code once again use frame

            elif(len(detected) == 1):
                d = detected[0]
                (x, y), radius = cv2.minEnclosingCircle(d)
                dist = actualBallWidth * focalLength / (2 * radius)
                centerx = x + radius
                centery = y + radius
                #insert alignment code same as above
            else:
                #no balls are detected and idle spinning thingy starts

            cv2.imshow('tennisdetect', frame)

            ret, frame = self.basketCam.read()

            brightness_matrix = np.ones(frame.shape, dtype="uint8") * 60
            frame = cv2.subtract(frame, brightness_matrix)

            blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)

            filtered_frame = cv2.bilateralFilter(blurred_frame, 9, 75, 75)

            hsv = cv2.cvtColor(filtered_frame, cv2.COLOR_BGR2HSV)

            lower_color = np.array([0, 0, 0]) #basket lower color
            upper_color = np.array([0, 0, 0]) #basket upper color

            mask = cv2.inRange(hsv, lower_color, upper_color)
            mask = cv2.dilate(mask, None, iterations=2)
            mask = cv2.erode(mask, None, iterations=1)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                area = cv2.contourArea(contour)
                if area > 100:
                    perimeter = cv2.arcLength(contour, True)
                    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
                    
                    if len(approx) == 4:
                        x,y,w,h = cv2.boundingRect(contour)
                        centerx = x + (w/2)
                        centery = y + (h/2)
                        #alignment code here to access the frame just use frame


            cv2.imshow('basketdetect', frame)

            if cv2.waitKey(1) & 0xFF ==ord('q') :
                break



        cv2.destroyAllWindows()

if __name__ == "__main__":
    tb = TennisBalle()
    tb.detect()
