#Import Libary
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#Define HashMap
hash = [["1", "2", "3", "A"],
        ["4", "5", "6", "B"],
        ["7", "8", "9", "C"],
        ["*", "0", "#", "D"]]

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

rows = [2,3,4,17]

GPIO.setup(X1, GPIO.OUT)
GPIO.setup(X2, GPIO.OUT)
GPIO.setup(X3, GPIO.OUT)
GPIO.setup(X4, GPIO.OUT)

def readKeypad(rowNum,char):
    curVal = ""
    counter = False
    GPIO.output(rowNum,GPIO.HIGH)
    if (GPIO.input(Y1)==1):
        while (GPIO.input(Y1)==1):
            if (counter):
                pass
            else: 
                curVal=char[0]
                print(curVal)
                counter = True
        
    if (GPIO.input(Y2)==1):
        while (GPIO.input(Y2)==1):
            if (counter):
                pass
            else: 
                curVal=char[1]
                print(curVal)
                counter = True
    if (GPIO.input(Y3)==1):
        while (GPIO.input(Y3)==1):
            if (counter):
                pass
            else: 
                curVal=char[2]
                print(curVal)
                counter = True
    if (GPIO.input(Y4)==1):
        while (GPIO.input(Y4)==1):
            if (counter):
                pass
            else: 
                curVal=char[3]
                print(curVal)
                counter = True
    GPIO.output(rowNum,GPIO.LOW)


counter = 0
while True: 
    
    readKeypad(rows[counter%4], hash[counter%4])

    counter+=1
