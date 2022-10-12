def switch(user):

    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(21, GPIO.OUT)

    try:
        while True:

            GPIO.output(21, GPIO.HIGH)
            print("pin is on")

            return "Success"

    finally: 
        GPIO.cleanup()    