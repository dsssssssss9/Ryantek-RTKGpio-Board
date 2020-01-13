from RTk import GPIO
from time import sleep
 
Green_LED = 26
Amber_LED = 19
Red_LED = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(Green_LED,GPIO.OUT)
GPIO.setup(Amber_LED,GPIO.OUT)
GPIO.setup(Red_LED,GPIO.OUT)

Doze = 2.0

while True:
    GPIO.output(Red_LED,1)
    sleep(Doze)
    GPIO.output(Amber_LED,1)
    sleep(Doze)
    GPIO.output(Red_LED,0)
    GPIO.output(Amber_LED,0)
    GPIO.output(Green_LED,1)
    sleep(Doze * 2)
    GPIO.output(Green_LED,0)
    GPIO.output(Amber_LED,1)
    sleep(Doze)
    GPIO.output(Amber_LED,0)
    
