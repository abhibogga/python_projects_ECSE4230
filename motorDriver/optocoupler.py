import RPi.GPIO as GPIO

#Initial setup for the GPIO
GPIO.setmode(GPIO.BCM)

#Setup GPIO pin for the motor and use 20Hz for freq
motor_pin = 13
frequency = 10

GPIO.setup(motor_pin, GPIO.OUT)

#Initialize the pwm GPIO with the motor pin and freq
pwm = GPIO.PWM(motor_pin, frequency)
pwm.ChangeFrequency(frequency)

#Start the pwm signal
pwm.start(50)

#Open loop
while True: 
    pass
