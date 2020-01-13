from RTk import GPIO
from time import sleep
 
Green_LED = 26
Amber_LED = 19
Red_LED = 13

G2LED = 4
A2LED = 3
R2LED = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(Green_LED,GPIO.OUT)
GPIO.setup(Amber_LED,GPIO.OUT)
GPIO.setup(Red_LED,GPIO.OUT)

GPIO.setup(G2LED,GPIO.OUT)
GPIO.setup(A2LED,GPIO.OUT)
GPIO.setup(R2LED,GPIO.OUT)

Doze = 2.0

AllLED = ( Green_LED, Amber_LED, Red_LED, G2LED, A2LED, R2LED)


#def AllOff():
for count in AllLED:
    
    print(count)
    GPIO.output(count,1)
    sleep (Doze)
    GPIO.output(count,0)
    sleep (Doze)
