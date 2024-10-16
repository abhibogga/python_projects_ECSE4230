import RPi.GPIO as GPIO
import time

# General Setup
GPIO.setmode(GPIO.BCM)
counter = 0


# Define GPIOs
clkPin = 2
dataPin = 3
switchPin = 4
greenLED = 17
redLED = 27

# Debounce settings
debounce_delay = 0.05  # 5 ms debounce time
last_turn_time = time.time()
minuteTime = time.time()
noneTime = time.time()

GPIO.setup(clkPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchPin, GPIO.IN)
GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)

# Initial states
clk = GPIO.input(clkPin)
dt = GPIO.input(dataPin)
sw = GPIO.input(switchPin)

currentState = (clk, dt)
pastState = (clk, dt)
printState = "none"
tps = counter/20
while True:
    # Read the current inputs
    clk = GPIO.input(clkPin)
    dt = GPIO.input(dataPin)
    sw = GPIO.input(switchPin)
    tps = counter/20
    
    # Update the current state to compare with pastState
    currentState = (clk, dt)

    # Debounce logic
    current_time = time.time()
    if current_time - last_turn_time < debounce_delay:
        continue
    
    if current_time - minuteTime > 1:  # 1 second time delay
        counter = 0
        minuteTime = current_time 

    if current_time - noneTime > 2:  # 1 second time delay
        print("none")
        noneTime = current_time
        
    # Rotary Encoder Logic
    if sw == 0: 
        print("Pressed")
        while sw == 0:
            sw = GPIO.input(switchPin)
            pass
    
    
        
    if pastState == (0, 0) or pastState == (1, 1):
        if pastState == (0, 0) and currentState == (0, 1):
            printState = "Counter Clockwise"
            counter += 1
            print(printState, tps)
            noneTime = current_time
            last_turn_time = current_time

            GPIO.output(greenLED, GPIO.HIGH)
            GPIO.output(redLED, GPIO.LOW)

        elif pastState == (1, 1) and currentState == (1, 0):
            printState = "Counter Clockwise"
            counter += 1
            print(printState, tps)
            noneTime = current_time
            last_turn_time = current_time


            GPIO.output(greenLED, GPIO.HIGH)
            GPIO.output(redLED, GPIO.LOW)

        elif pastState == (0, 0) and currentState == (1, 0):
            printState = "Clockwise"
            counter += 1
            print(printState, tps)
            noneTime = current_time
            last_turn_time = current_time

            GPIO.output(redLED, GPIO.HIGH)
            GPIO.output(greenLED, GPIO.LOW)


        elif pastState == (1, 1) and currentState == (0, 1):
            printState = "Clockwise"
            counter += 1
            print(printState, tps)
            noneTime = current_time
            last_turn_time = current_time

            GPIO.output(redLED, GPIO.HIGH)
            GPIO.output(greenLED, GPIO.LOW)

        else: 
            GPIO.output(redLED, GPIO.LOW)
            GPIO.output(greenLED, GPIO.LOW)
            
            
            
   
    # Update past state
    pastState = currentState

    
