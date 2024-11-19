import RPi.GPIO as GPIO
import time

# set up GPIO
GPIO.setmode(GPIO.BCM)

# set up pins
clkPin = 2
dataPin = 3
switchPin = 4
greenLED = 17
redLED = 27

# motor pin
motor_pin = 13
frequency = 10

# IR sensor Pin
irPin = 5

# setting up all pins/GPIO
GPIO.setup(clkPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(motor_pin, GPIO.OUT)
GPIO.setup(irPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# instantiate variables
debounce_delay = 0.05
speed_step = 25  # RPM change per pulse
max_rpm = 5000   # Max speed in RPM
rpm = 0
desired_speed = 0
counter = 0
motor_on = False
last_turn_time = time.time()

# initialize motor PWM
pwm = GPIO.PWM(motor_pin, frequency)
pwm.start(0)  # motor off at 0% duty cycle

# variables for the interrupt
ir_count = 0
blade_count = 3 # number of blades on the fan
rpm_calculation_interval = 1  # in seconds
last_rpm_time = time.time()



# IR sensor interrupt handler when a blade passes (rising edges)
def ir_sensor_callback(channel):
    global ir_count
    ir_count += 1

GPIO.add_event_detect(irPin, GPIO.RISING, callback=ir_sensor_callback)

# update RPM by converting rising edges into RPM ad calculating RPM
def calculate_rpm():
    global ir_count
    current_time = time.time()
    elapsed_time = current_time - last_rpm_time

    if elapsed_time >= rpm_calculation_interval:
        # calculates and accounts for the number of blades on the fan
        measured_rpm = (ir_count / blade_count) * (60 / elapsed_time)
        ir_count = 0
        return measured_rpm
    return None

# converts speed to duty cycle
def set_motor_speed(speed):
    duty_cycle = (speed / max_rpm) * 100
    pwm.ChangeDutyCycle(duty_cycle)

# toggling motor on and off and returning to last speed
def handle_button_press():
    global motor_on
    sw = GPIO.input(switchPin)
    if sw == 0:
        motor_on = not motor_on
        if motor_on:
            set_motor_speed(desired_speed)
            print("Motor ON")
        else:
            set_motor_speed(0)
            print("Motor OFF")
        # debounce for presses
        while GPIO.input(switchPin) == 0:  
            time.sleep(0.1)

# adjusting speed function
def handle_rotary_encoder():
    global desired_speed, last_turn_time
    clk = GPIO.input(clkPin)
    dt = GPIO.input(dataPin)
    current_time = time.time()

    if current_time - last_turn_time < debounce_delay:
        return

    if clk == 0 and dt == 1:
        # incrementing by turning the knob clockwise
        desired_speed += speed_step
    elif clk == 1 and dt == 0:
        # decrementing by turning the knob counterclockwise
        desired_speed -= speed_step

    # makes sure that it doen't go below 0 and the max of the motor
    desired_speed = max(0, min(desired_speed, max_rpm))
    print(f"Desired Speed: {desired_speed} RPM")
    last_turn_time = current_time



# Main Loop
try:
    while True:
        handle_button_press()
        handle_rotary_encoder()

        # adjust motor speed if it's turned on
        if motor_on:
            set_motor_speed(desired_speed)
        
        # calculate and display RPM from the IR sensor
        actual_rpm = calculate_rpm()
        if actual_rpm is not None:
            print(f"Measured RPM: {actual_rpm:.2f}")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting.")
finally:
    pwm.stop()
    GPIO.cleanup()
