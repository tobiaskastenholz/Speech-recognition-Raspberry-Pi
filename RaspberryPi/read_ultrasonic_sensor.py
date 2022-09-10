import RPi.GPIO as GPIO
import time
 
#GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO pin defintion
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#define input/output pins
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set trigger HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set trigger  LOW after 0.01ms
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    starttime = time.time()
    stoptime = time.time()
 
    # save starttime
    while GPIO.input(GPIO_ECHO) == 0:
        starttime = time.time()
 
    # save stoptime
    while GPIO.input(GPIO_ECHO) == 1:
        stoptime = time.time()
 
    # elapsed time
    time_elapsed = stoptime - starttime
    # multiply with speed of sound and divide by 2 (signal traves both directions)
    distance = (time_elapsed * 34300) / 2
 
    return distance


if __name__ == '__main__':
    try:
        while True:
            distance = distance()
            print ("Measured distance = %.1f cm" % distance)
            time.sleep(1)
 
        # Stop Measurement manually
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()
