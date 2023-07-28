import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
#set to function number and not board number
GPIO.setmode(GPIO.BOARD)

#set up the pins
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
#set up pwm
poop1 =  GPIO.PWM(16,100)
poop2 =  GPIO.PWM(18,100)
#start up the pwm pins but at 0%
int speed = 0

poop1.start(speed)
poop2.start(speed)

while True: 
    if GPIO.input(10) == GPIO.HIGH:
        print("INCREASE SPEEEEEED")
        speed = speed + 10
        poop1.ChangeDutyCycle(speed)  
        poop2.ChangeDutyCycle(speed)  

    if GPIO.input(12) == GPIO.HIGH:
        print("STOOOOOOOP")
        break

poop1.ChangeDutyCycle(0)  
poop2.ChangeDutyCycle(0)  
poop1.stop()  
poop2.stop()  
GPIO.cleanup()
