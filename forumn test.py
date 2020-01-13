from RTk import GPIO
import time
 
LED_PIN = 4


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN,GPIO.OUT)

while True:

    print ("LED on")
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(1)
    print ("LED off")
    GPIO.output(LED_PIN,GPIO.LOW)
    time.sleep(1)
