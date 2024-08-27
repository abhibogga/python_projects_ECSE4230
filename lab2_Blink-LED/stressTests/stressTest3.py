# Part 3 imports
import pigpio
import time

#Part 3 Code:
pi=pigpio.pi()

pin_number = 17
frequency = 100
dutyCycleValue = 255/2

# Desired frequency with PWM
pi.set_PWM_frequency(pin_number, frequency)

# Desired duty cycle and turn on the square wave
pi.set_PWM_dutycycle(pin_number, dutyCycleValue)

#Handle Timing things
startTime = time.time() #Starts clock
interval = 10 #5 Seconds

# Keep the program running while the LED is blinking
try:
    while True:
        currentTime = time.time() #Starts current time

        if (currentTime - startTime >= interval):
            frequency += 10 #CHANGE THIS WHEN YOU WANT TO CHANGE THE FREQ INTERVAL
            pi.set_PWM_frequency(pin_number, frequency)
            print("Frequency " + str(frequency))
            startTime = currentTime

except KeyboardInterrupt:
    # Once the loop is complete or interrupted
    pi.set_PWM_dutycycle(pin_number, 0)