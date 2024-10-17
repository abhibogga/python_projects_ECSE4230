#General Setup: 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#Define GPIOS
clkPin = 2
dataPin = 3
switchPin = 4

greenLED = 17
redLED = 27

GPIO.setup(clkPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchPin, GPIO.IN)

GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)

# Initialize variables
encPosCount = 0
dCW = True
lastChanged = 0

# Save inital values for clk and dt
clkLast = GPIO.input(clkPin)
dtLast = GPIO.input(dataPin)

#While loop
while True: 
    # update pin states
    clk = GPIO.input(clkPin)
    dt = GPIO.input(dataPin)
    sw = GPIO.input(switchPin)
    
    '''
    # compare current and previous clk states to see if it changed
    if clk != clkLast:
        if clk != dt: # clk pin changed first, so clockwise, increment position
            encPosCount += 1
            dCW = True
        else: # dt pin changed first, so counter-clockwise, decrement position
            dCW = False
            encPosCount -= 1
    '''

    
    # Attempt 2: testing for both switches being closed
    
    # Store last changed value
    if clk != clkLast:
        lastChanged = "clk"
    if dt != dtLast:
        lastChanged = "dt"

    # Use the last changed variable to determine direction of rotation
    if (clk == 0) & (dt == 0):
        if lastChanged == "dt": # clockwise
            encPosCount += 1
            GPIO.output(redLED, GPIO.HIGH)
            dCW = True
        elif lastChanged == "clk":
            dCw = False
            GPIO.output(greenLED, GPIO.HIGH)
            encPosCount -= 1
    else:
        GPIO.output(redLED, GPIO.LOW)
        GPIO.output(greenLED, GPIO.LOW)
    
    # Print states
    if dCW == True:
        print("Clockwise", encPosCount)
    else: 
        print("Counter-Clockwise", encPosCount)

    print("CLK\t", clk, "\tDT\t", dt)
    print("clkLast\t", clkLast, "\tdtLast\t", dtLast)
    clkLast = GPIO.input(clkPin)
    dtLast = GPIO.input(dataPin)
    