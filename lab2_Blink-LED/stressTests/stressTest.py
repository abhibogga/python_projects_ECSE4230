# Part 1 imports
import RPi.GPIO as GPIO
from time import sleep
import time

# Part 1 Code:
GPIO.setwarnings(False)

# GPIO pin mode (GPIO Numbers)
GPIO.setmode(GPIO.BCM) 

# GPIO pin for output
pin_number = 17  
GPIO.setup(pin_number, GPIO.OUT, initial=GPIO.LOW)

# Loop to turn the LED on and off
period = .0001 
startFrequency = 10000
frequency = 10000


print("Frequency: " + str(startFrequency))

#Handle Timing things
startTime = time.time() #Starts clock
interval = 10 #15 Seconds


try:
    while True:
        currentTime = time.time() #Starts current time

        '''if currentTime - startTime >= interval: 
            #Now add the if statements to control freq
            if (10 < frequency and frequency < 100): #Add 10
                frequency += 10
                period = 1/frequency
                print("Frequency " + frequency)
                print("Period " + period)
            if (100 < frequency and frequency < 1000): #Add 100 
                frequency += 100
                period = 1/frequency
                print("Frequency " + frequency)
                print("Period " + period)
            if (1000 < frequency and frequency < 10000): #Add 1000
                frequency += 1000
                period = 1/frequency
                print("Frequency " + frequency)
                print("Period " + period)
            if (10000 < frequency and frequency < 65000)'''


        if (currentTime - startTime >= interval):
            frequency += 5000 #CHANGE THIS WHEN YOU WANT TO CHANGE THE FREQ INTERVAL
            period = 1/frequency
            print("Frequency " + str(frequency))
            print("Period " + str(period))
            startTime = currentTime

        GPIO.output(pin_number, GPIO.HIGH)  # Turn on the LED
        sleep(period/2)  
        GPIO.output(pin_number, GPIO.LOW)  # Turn off the LED
        sleep(period/2)  
except KeyboardInterrupt:
    GPIO.cleanup()  
