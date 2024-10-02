#Import Libary
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
from collections import deque
GPIO.setmode(GPIO.BCM)
#Define HashMap
hash = [["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]
pureNumHash = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*"]

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
True
X1 = 2
X2 = 3
X3 = 4
X4 = 17

#Define GPIO's for ssd
A = 11
B = 0
C = 6
D = 13
E = 19
F = 16
G = 12
DOT = 5
CLK1 = 26
CLK2 = 20
CLK3 = 21
CLK4 = 14
led = 15
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
GPIO.setup(CLK2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(CLK3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(CLK4, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

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

clkList = [CLK1, CLK2, CLK3, CLK4]


preVal = []
screenState = True

def clear():
    for i in everyone:
        GPIO.output(i, GPIO.LOW)


queue = []
queueCounter = 0
#load 0's into queue
for i in range(4): 
    queue.append(0)


def loadNums(num): 
    global queue
    global queueCounter
    if not (num == "#"):
        #first we want to pop left
        
        queue[queueCounter%4] = num
        queueCounter += 1
    fourStageLoad("yomama", queue, False)
        #print(queue)

def loadZero(clk): 
    for i in zero:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadOne(clk): 
    for i in one:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadTwo(clk): 
    for i in two:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadThree(clk): 
    for i in three:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadFour(clk): 
    for i in four:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadFive(clk): 
    for i in five:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadSix(clk): 
    for i in six:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadSeven(clk): 
    for i in seven:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadEight(clk): 
    for i in eight:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadNine(clk): 
    for i in nine:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadStar(clk): 
    for i in dot:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadA(clk): 
    for i in a:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)

def loadB(clk): 
    for i in b:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)   

def loadC(clk): 
    for i in c:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)  

def loadD(clk): 
    for i in d:
        GPIO.output(i, GPIO.HIGH)
        GPIO.output(clk, GPIO.LOW)
        sleep(period/2)
        GPIO.output(clk, GPIO.HIGH)
        sleep(period/2)


def readKeypad(rowNum,char, loadValues):
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
                    preVal = four
                    if loadValues: 
                        loadNums(1)    
                elif curVal == "4":
                    clear()
                    preVal = four
                    if loadValues: 
                        loadNums(4)
                    
                elif curVal == "7":
                    clear()
                    preVal = seven
                    if loadValues: 
                        loadNums(7)
                    
                elif curVal == "*":
                    clear()
                    preVal = dot
                    if loadValues: 
                        loadNums(10)
                    
                
        
    if (GPIO.input(Y2)==1):
        while (GPIO.input(Y2)==1):
            if (pressed):
                pass
            else: 
                curVal=char[1]
                print(curVal)
                pressed = True
                clear()
                if curVal == "2":
                    clear()
                    preVal = four
                    if loadValues: 
                        loadNums(2)
                    
                elif curVal == "5":
                    clear()
                    preVal = five
                    if loadValues: 
                        loadNums(5)
                    
                elif curVal == "8":
                    clear()
                    preVal = eight
                    if loadValues: 
                        loadNums(8)
                    
                elif curVal == "0":
                    clear()
                    preVal = zero
                    if loadValues: 
                        loadNums(0)
                    
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
                    if loadValues: 
                        loadNums(3)
                    
                elif curVal == "6":
                    clear()
                    preVal = six
                    if loadValues: 
                        loadNums(6)
                    
                elif curVal == "9":
                    clear()
                    preVal = nine
                    if loadValues: 
                        loadNums(9)
                    
                elif curVal == "#": # WE NEED TO FIX THIS AT SOME POINT DO NOT FORGET!! 
                    global screenState
                    if loadValues: 
                        print(screenState)
                        if screenState:
                            for clk in clkList:
                                for i in everyone:
                                    GPIO.output(i, GPIO.LOW)
                                    GPIO.output(clk, GPIO.LOW)
                                    sleep(period/2)
                                    GPIO.output(clk, GPIO.HIGH)
                                    sleep(period/2)
                            screenState = False
                        else:
                            loadNums("#")
                            screenState = True
                    
                    else: 
                        print(screenState)
                        # Manual clear
                        if screenState: 
                            timeGPIO = [CLK1, CLK2, CLK3, CLK4]
                            for j in timeGPIO: 
                                for i in everyone:
                                    GPIO.output(i, GPIO.LOW)
                                    GPIO.output(j, GPIO.LOW)
                                    sleep(period/2)
                                    GPIO.output(j, GPIO.HIGH)
                                    sleep(period/2)
                            screenState = False
                        else:
                            '''for i in preVal:
                                GPIO.output(i, GPIO.HIGH)
                                GPIO.output(CLK1, GPIO.LOW)
                                sleep(period/2)
                                GPIO.output(CLK1, GPIO.HIGH)
                                sleep(period/2)'''
                            #We need to turn on clock again
                            dateTimeFunction(False)
                            screenState = True
               
    if (GPIO.input(Y4)==1):
        ledON = False
        while (GPIO.input(Y4)==1):
            if (pressed):
                GPIO.output(led, GPIO.HIGH)
                
            else: 
                curVal=char[3]
                print(curVal)
                pressed = True
                if curVal == "A" and not loadValues:
                    clear()
                    preVal = a
                    loadA(CLK1)
                elif curVal == "B" and not loadValues:
                    clear()
                    preVal = b
                    loadB(CLK1)
                elif curVal == "C" and not loadValues:
                    clear()
                    preVal = c
                    loadC(CLK1)
                elif curVal == "D" and not loadValues:
                    clear()
                    preVal = d
                    loadD(CLK1)
    GPIO.output(rowNum,GPIO.LOW)
    GPIO.output(led, GPIO.LOW)


def fourStageLoad(stringTime, loadVals, clockMode): 
    global pureNumHash
    #Boolean to check if hours is pm
    pm = False
    
    #Index for the informaion we need 
    if clockMode : 
        chars = [char for char in stringTime]
        print(chars)
        vals = [11, 12, 14, 15]

        hours = int(str(chars[11] + chars[12]))
        if hours > 12: 
            pm = True
            hours = (hours - 12) #This will keep it not military time
            if hours < 10: 
                hours = "0" + str(hours)
            else: 
                hours = str(hours)
            print(hours)
            chars[11] = hours[0]
            chars[12] = hours[1]
            
    else: 
        chars = pureNumHash
        vals = loadVals
        #vals = list(reversed(loadVals))
        print(vals)
        
    timeGPIO = [CLK1, CLK2, CLK3, CLK4]
    

    
    for j in range(4):
        
        if chars[vals[j]] == "1":
            clear()
            loadOne(timeGPIO[j])
        elif chars[vals[j]] == "4":
            clear()
            loadFour(timeGPIO[j])
        elif chars[vals[j]] == "7":
            clear()
            loadSeven(timeGPIO[j])          
        elif chars[vals[j]] == "2":
            clear()
            loadTwo(timeGPIO[j])
        elif chars[vals[j]] == "5":
            clear()
            loadFive(timeGPIO[j])
        elif chars[vals[j]] == "8":
            clear()
            loadEight(timeGPIO[j])
        elif chars[vals[j]] == "0":
            clear()
            loadZero(timeGPIO[j])
        if chars[vals[j]] == "3":
            clear()
            loadThree(timeGPIO[j])
        elif chars[vals[j]] == "6":
            clear()
            loadSix(timeGPIO[j])
        elif chars[vals[j]] == "9":
            clear()
            loadNine(timeGPIO[j])
        elif chars[vals[j]] == "*":
            clear()
            loadStar(timeGPIO[j])

        #Add dot on second display: 
        if pm and j == 1: 
            loadStar(timeGPIO[j])
    
    
def dateTimeFunction(compare): 
    global timeStart
    global programStart
    global queue
    now = datetime.now()
    now = str(now)

    #If we need to compare: 
    if compare: 
        cmp = [char for char in str(now)]
        cmp = cmp[11:16:1]
    

        #Now lets compare values: 
    
        if cmp != timeStart or programStart:
            #this is what updates the thing 
            fourStageLoad(now, queue, True)
            timeStart = cmp
            programStart = False
    else: 
        #UPdates the clocks
        fourStageLoad(now, queue, True)

    
def manualClock(): 
    global timeStart
    global queueCounter
    global queue
    counter = 0
    queue =  [0 ,0, 0, 0]
    queueCounter = 0
    clkArr = [CLK1, CLK2, CLK3, CLK4]
    returnArr = [0 for x in range(20)]

    while queueCounter < 4:
        readKeypad(rows[counter%4], hash[counter%4], True)
        counter+=1
        if queueCounter < 4: 
            #Do some flash code
            for i in everyone:
                GPIO.output(i, GPIO.LOW)
                GPIO.output(clkArr[queueCounter], GPIO.LOW)
                sleep(period/2)
                GPIO.output(clkArr[queueCounter], GPIO.HIGH)
                sleep(period/2)

            
            #turn it bac on 
            loadZero(clkArr[queueCounter])


    #We need to create variables to handle the math 
    seconds = 0
    minutes = (queue[2:4:1])
    hours = queue[0:2:1]
     
    print("hrs", hours)
    if ((hours[0] > 2) or (hours[0] == 2 and hours[1] > 4) or minutes[0] > 5): 
        print("incorrect input")

        manualClock()

    minutes = int("".join(map(str, minutes)))
    hours = int("".join(map(str, hours)))
    while True:

        #Sleep for 60s
        sleep(1)

        #Now we need to handle the math for this:
        if minutes + 1 == 60:  
            minutes = 0
            hours = (hours + 1)%24
        else: 
            minutes += 1      

        print("hours: ", hours)
        print("mins", minutes)  

        if hours < 10: 
            inputHours = "0" + str(hours)
        else: 
            inputHours = str(hours)
        inputHours = [x for x in inputHours]
        returnArr[11] = inputHours[0]
        returnArr[12] = inputHours[1]
       
        if minutes < 10:  
            inputMinutes = "0" + str(minutes)
        else: 
            inputMinutes = str(minutes)
        inputMinutes = [x for x in inputMinutes]
        returnArr[14] = inputMinutes[0]
        returnArr[15] = inputMinutes[1]

        fourStageLoad(returnArr, queue, True)
        





counter = 0
#Set all ssd to 0
loadZero(CLK1)
loadZero(CLK2)
loadZero(CLK3)
loadZero(CLK4)

#Intialize the time at the beginning of the fucntion 
timeStart = datetime.now()
timeStart = [char for char in str(timeStart)]
timeStart = timeStart[11:16:1]

programStart = True
print(timeStart)



print("starting location")
print(timeStart)

manualClock()


#No need for running while loo while running manual clock
'''while True: 

    if screenState: 
        #dateTimeFunction(True)
        manualClock()
    readKeypad(rows[counter%4], hash[counter%4], False)

    counter += 1'''
        






