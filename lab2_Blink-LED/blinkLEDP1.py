# Part 1 imports
import RPi.GPIO as GPIO
from time import sleep

# Part 1 Code:
GPIO.setwarnings(False)

# GPIO pin mode (GPIO Numbers)
GPIO.setmode(GPIO.BCM) 

# GPIO pin for output
pin_number = 17  
GPIO.setup(pin_number, GPIO.OUT, initial=GPIO.LOW)

# Loop to turn the LED on and off
try:
    while True:
        GPIO.output(pin_number, GPIO.HIGH)  # Turn on the LED
        sleep(.005)  
        GPIO.output(pin_number, GPIO.LOW)  # Turn off the LED
        sleep(.005)  
except KeyboardInterrupt:
    GPIO.cleanup()  
