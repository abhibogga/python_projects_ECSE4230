#Import Libary
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
GPIO.setmode(GPIO.BCM)
#Define HashMap
hash = [["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]

#Setup GPIOs for SSD

#Define Rows, rows will be input: 
Y1 = 27
Y2 = 22
Y3 = 10
Y4 = 9

GPIO.setup(Y1, GPIO.IN)
GPIO.setup(Y2, GPIO.IN)
GPIO.setup(Y3, GPIO.IN)
GPIO.setup(Y4, GPIO.IN)

#Define Columns, columns will be output
X1 = 2
X2 = 3
X3 = 4
X4 = 17

#Define GPIO's for ssd
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

rows = [2,3,4,17]

GPIO.setup(X1, GPIO.OUT)
GPIO.setup(X2, GPIO.OUT)
GPIO.setup(X3, GPIO.OUT)
GPIO.setup(X4, GPIO.OUT)


#GPIO Setup for ssd

GPIO.setup(A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(B, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(C, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(D, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(E, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(F, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(G, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DOT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(CLK1, GPIO.OUT, initial=GPIO.HIGH)

#Arrays for display on ssd
everyone = [A, B, C, D, E, F, G, DOT]
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

preVal = []
screenState = True

def clear():
    for i in everyone:
        GPIO.output(i, GPIO.LOW)




def readKeypad(rowNum,char):
    curVal = ""
    global preVal
    pressed = False
    GPIO.output(rowNum,GPIO.HIGH)
    if (GPIO.input(Y1)==1):
        while (GPIO.input(Y1)==1):
            if (pressed):
                pass
            else: 
                
                curVal=char[0]
                print(curVal)
                pressed = True
                if curVal == "1":
                    clear()
                    preVal = one
                    for i in one:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "4":
                    clear()
                    preVal = four
                    for i in four:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "7":
                    clear()
                    preVal = seven
                    for i in seven:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "*":
                    clear()
                    preVal = dot
                    for i in dot:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                
        
    if (GPIO.input(Y2)==1):
        while (GPIO.input(Y2)==1):
            if (pressed):
                pass
            else: 
                curVal=char[1]
                print(curVal)
                pressed = True
                if curVal == "2":
                    clear()
                    preVal = two
                    for i in two:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "5":
                    clear()
                    preVal = five
                    for i in five:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "8":
                    clear()
                    preVal = eight
                    for i in eight:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "0":
                    clear()
                    preVal = zero
                    for i in zero:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
    if (GPIO.input(Y3)==1):
        while (GPIO.input(Y3)==1):
            if (pressed):
                pass
            else: 
                curVal=char[2]
                print(curVal)
                pressed = True
                if curVal == "3":
                    clear()
                    preVal = three
                    for i in three:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "6":
                    clear()
                    preVal = six
                    for i in six:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "9":
                    clear()
                    preVal = nine
                    for i in nine:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "#":
                    global screenState
                    
                    # Manual clear
                    if screenState:
                        for i in everyone:
                            GPIO.output(i, GPIO.LOW)
                            GPIO.output(CLK1, GPIO.LOW)
                            sleep(period/2)
                            GPIO.output(CLK1, GPIO.HIGH)
                            sleep(period/2)
                        screenState = False
                    else:
                        for i in preVal:
                            GPIO.output(i, GPIO.HIGH)
                            GPIO.output(CLK1, GPIO.LOW)
                            sleep(period/2)
                            GPIO.output(CLK1, GPIO.HIGH)
                            sleep(period/2)
                        screenState = True


                    


                    
    if (GPIO.input(Y4)==1):
        while (GPIO.input(Y4)==1):
            if (pressed):
                pass
            else: 
                curVal=char[3]
                print(curVal)
                pressed = True
                if curVal == "A":
                    clear()
                    preVal = a
                    for i in a:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "B":
                    clear()
                    preVal = b
                    for i in b:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "C":
                    clear()
                    preVal = c
                    for i in c:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
                elif curVal == "D":
                    clear()
                    preVal = d
                    for i in d:
                        GPIO.output(i, GPIO.HIGH)
                        GPIO.output(CLK1, GPIO.LOW)
                        sleep(period/2)
                        GPIO.output(CLK1, GPIO.HIGH)
                        sleep(period/2)
    GPIO.output(rowNum,GPIO.LOW)


counter = 0
while True: 
    
    (readKeypad(rows[counter%4], hash[counter%4]) )
        

    counter+=1









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

