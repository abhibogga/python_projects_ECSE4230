# Part 2 imports
import wiringpi
import time

# Part 2 Code:
# Setup the GPIO pins (GPIO Numbers)
wiringpi.wiringPiSetupGpio()  

pin_number = 17  

# Pin to output a square wave
wiringpi.softToneCreate(pin_number)

# Write the desired frequency to the pin
frequency = 10000  
wiringpi.softToneWrite(pin_number, frequency)

#Handle Timing things
startTime = time.time() #Starts clock
interval = 10 #10 Seconds


# Keep the program running while the LED is blinking
try:
    while True:
        currentTime = time.time() #Starts current time

        if (currentTime - startTime >= interval):
            frequency += 5000 #CHANGE THIS WHEN YOU WANT TO CHANGE THE FREQ INTERVAL
            wiringpi.softToneWrite(pin_number, frequency)
            print("Frequency " + str(frequency))
            startTime = currentTime

except KeyboardInterrupt:
    # Once the loop is complete or interrupted, set the pin frequency to 0 to shut it off
    wiringpi.softToneWrite(pin_number, 0)