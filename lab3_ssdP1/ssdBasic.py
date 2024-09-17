import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
GPIO.setmode(GPIO.BCM)
#Define GPIO's
A = 19
B = 13
C = 6
D = 5
E = 0
F = 11
G = 16
DOT = 12
CLK1 = 26
period = .005

GPIO.setup(A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(B, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(C, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(D, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(E, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(F, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(G, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DOT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(CLK1, GPIO.OUT, initial=GPIO.HIGH)

zero = [A,B,C,D,E,F] 
one = [B, C]
two = [A, B, G, E, D]
three = [A, B, G, C, D]
four = [F, G, B, C]
five = [A, F, G, C, D]
six = [A, F, G, C, D, E]
seven = [A, B, C]
eight = [A, B, C, D, E, F, G]
nine = [A, B, C, D, F, G]
dot = [DOT]

a = [A, B, C, E, F, G]
b = [C, D, E, F, G]
c = [G, E, D]
d = [B, C, D, E, G]


try: 
    while (True):
        for i in zero:
            GPIO.output(i, GPIO.HIGH)
            GPIO.output(CLK1, GPIO.LOW)
            sleep(period/2)
            GPIO.output(CLK1, GPIO.HIGH)
            sleep(period/2)
except KeyboardInterrupt:
    GPIO.cleanup()

