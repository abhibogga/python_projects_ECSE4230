# Part 2 imports
import wiringpi

# Part 2 Code:
# Setup the GPIO pins (GPIO Numbers)
wiringpi.wiringPiSetupGpio()  

pin_number = 17  

# Pin to output a square wave
wiringpi.softToneCreate(pin_number)

# Write the desired frequency to the pin
frequency = 100  
wiringpi.softToneWrite(pin_number, frequency)

# Keep the program running while the LED is blinking
try:
    while True:
        pass  # Empty loop to keep the program running

except KeyboardInterrupt:
    # Once the loop is complete or interrupted, set the pin frequency to 0 to shut it off
    wiringpi.softToneWrite(pin_number, 0)