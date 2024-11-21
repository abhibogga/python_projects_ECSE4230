import RPi.GPIO as GPIO
import time

# General Setup
GPIO.setmode(GPIO.BCM)
counter = 0


# Define GPIOs
clkPin = 2
dataPin = 3
switchPin = 4
irPin = 5
motor_pin = 13

irled = 17

#Setup variables and start freq to 2500 Hz
frequency = 2500
dutyCycle = 20
prevDuty = 20
fanOn = True

GPIO.setup(motor_pin, GPIO.OUT)

#Initialize the pwm GPIO with the motor pin and freq
pwm = GPIO.PWM(motor_pin, frequency)
pwm.ChangeDutyCycle(dutyCycle)

#Start the pwm signal
pwm.start(dutyCycle)

# Debounce settings
debounce_delay = 0.05  # 5 ms debounce time
last_turn_time = time.time()
minuteTime = time.time()
noneTime = time.time()

GPIO.setup(clkPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchPin, GPIO.IN)
GPIO.setup(irPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(irled, GPIO.OUT)

# Initial states
clk = GPIO.input(clkPin)
dt = GPIO.input(dataPin)
sw = GPIO.input(switchPin)
ir = GPIO.input(irPin)

# Init encoder variable
currentState = (clk, dt)
pastState = (clk, dt)
currentIR = ir
pastIR = ir
ircount = 0
# Init IR Feedback variables
feedback = 0
startTime = time.perf_counter()
desiredRPM = 1500
actualRPM = 0

while True:
    #Changing the frequency constantly
    pwm.start(dutyCycle)

    # Read the current inputs
    clk = GPIO.input(clkPin)
    dt = GPIO.input(dataPin)
    sw = GPIO.input(switchPin)
    
    # Update the current state to compare with pastState
    currentState = (clk, dt)

    # Debounce logic
    current_time = time.time()
    if current_time - last_turn_time < debounce_delay:
        continue
    
    if current_time - minuteTime > 1:  # 1 second time delay
        minuteTime = current_time 

    if current_time - noneTime > 2:  # 1 second time delay
        noneTime = current_time
        
    # Rotary Encoder Logic
    if sw == 0: 
        print("Switch Pressed")
        if fanOn == True:
            fanOn = False
            print("Paused. Saved Value:", dutyCycle, "% Duty Cycle")
        else:
            fanOn = True
            dutyCycle = prevDuty
            print("Resume to", dutyCycle, "% Duty Cycle")
        while sw == 0:
            sw = GPIO.input(switchPin)
            pass
        time.sleep(.1)
    
    # Read encoder states t detect turns
    
    if pastState == (0, 0) or pastState == (1, 1):
        if pastState == (0, 0) and currentState == (0, 1):
            printState = "Counter Clockwise"
            if dutyCycle > 0 and desiredRPM > 0: 
                desiredRPM -= 25
        elif pastState == (1, 1) and currentState == (1, 0):
            printState = "Counter Clockwise"
            if dutyCycle > 0 and desiredRPM > 0: 
                desiredRPM -= 25
        elif pastState == (0, 0) and currentState == (1, 0):
            printState = "Clockwise"
            if dutyCycle < 100: 
                desiredRPM += 25
        elif pastState == (1, 1) and currentState == (0, 1):
            printState = "Clockwise"
            if dutyCycle < 100: 
                desiredRPM += 25
    
    # Update past state
    pastState = currentState


    # IR SENSOR CODE
    currentIR = GPIO.input(irPin)
    # Detect a falling edge from IR Sensor
    if currentIR == 0 and pastIR == 1:
        ircount += 1
        #print("IR Count:", ircount)
        #time.sleep(.1)
    # Update past IR Sensor state
    pastIR = currentIR

    # Calculate rpm every
    currentTime = time.perf_counter()
    
    if currentTime - startTime > .5: #This is one sencond
        startTime = currentTime

        # Calculate rpm
        rps = ircount/3.0
        #print(rps)
        actualRPM = float(rps*60*2)
        ircount = 0
        print("Actual RPM: ", round(actualRPM, 3), "\tExpected RPM:", desiredRPM)
        # Feedback to update duty cycle from rpm
        if fanOn == True:
            if not (.9 * actualRPM < desiredRPM and desiredRPM < 1.1 * actualRPM):
                diff = abs(desiredRPM - actualRPM)
                if (desiredRPM > actualRPM) and (dutyCycle<99.9):
                    if diff > 1000 and (dutyCycle<94):
                        dutyCycle += 6
                    elif diff > 500 and (dutyCycle<97):
                        dutyCycle += 3
                    elif diff > 100 and (dutyCycle<99.5):
                        dutyCycle += 0.5
                    else:
                        dutyCycle += 0.25
                elif (desiredRPM < actualRPM) and (dutyCycle > 0.1):
                    if diff > 1000 and (dutyCycle < 6):
                        dutyCycle -= 6
                    elif diff > 500 and (dutyCycle < 3):
                        dutyCycle -= 3
                    elif diff > 100 and (dutyCycle < 0.5):
                        dutyCycle -= 0.5
                    else:
                        dutyCycle -= 0.25
        else:
            if dutyCycle != 0:
                prevDuty = dutyCycle
                dutyCycle = 0
