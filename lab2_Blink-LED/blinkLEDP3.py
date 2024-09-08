# Part 3 imports
import pigpio

#Part 3 Code:
pi=pigpio.pi()

pin_number = 17
frequency = 10

dutyCycleValue = 255/2

# Desired frequency with PWM
pi.set_PWM_frequency(pin_number, frequency)

# Desired duty cycle and turn on the square wave
pi.set_PWM_dutycycle(pin_number, dutyCycleValue)

# Keep the program running while the LED is blinking
try:
    while True:
        pass  # Empty loop to keep the program running

except KeyboardInterrupt:
    # Once the loop is complete or interrupted
    pi.set_PWM_dutycycle(pin_number, 0)