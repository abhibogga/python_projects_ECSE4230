#import libraries
import RPi.GPIO as GPIO

#Time imports
from time import sleep
from time import perf_counter

#Imports for intterupts
import signal 
import sys



#Initial setup for the GPIO
GPIO.setmode(GPIO.BCM)

#Setup GPIO pin for the motor and use 20Hz for freq
clicker = 12


GPIO.setup(clicker, GPIO.IN)

#Define the dictionaries
morseStringDict = {
    "-.-.-.": "attention:",
    ".-.-.-": "out",
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"
}

#Dot and Dash length variables: 
dot = 0

# Define global variables
startTime = 0
endTime = 0

#Define variables for call words
stringList = "-"

dotTimings = []
dashTimings = []




# Interrupt Callback
def processDotDash(channel):
    global startRest 
    global dash, dot, space, letter
    global dotTimings, dashTimings
    global startTime, endTime
    global stringList
    if not GPIO.input(clicker):
        endTime = perf_counter()
        elapsedTime = endTime - startTime
        
        #print("dash", dash, "dot", dot, "elaspedTime" ,elapsedTime )

        #Here well do all our processing for dots and dashes
        if  elapsedTime < dot *2: 
            print("dot")
            stringList += "."
            dotTimings.append(elapsedTime)
            

             
        
        if elapsedTime > dot * 2:
            print("dash")
            stringList += "-"
            dashTimings.append(elapsedTime)
            


        #We need to start the rest time up again to properly process next interval 
        startRest = perf_counter()
        

    else:
        #This starts the timer for when the key is pressed down
        startTime = perf_counter()

        #We also need to find out the rest that happened in between
        #To do that we will need to end the timer that is counting the down time between rising and falling edges
        
        #This means that we only want to start recording the spaces once we sign the first signal
        if len(stringList) > 0:
            endRest = perf_counter()
            restTime = endRest - startRest
            

            #Now time to calculate the spaces and letters
            if restTime < dot *2: 
                print("space")
                stringList += ""
                
        
            if restTime > dot * 2:
                print("letter")
                analyzeLetter(stringList)
                stringList = ""
                
                
            
#this is an ease of use function meant to update all the values we get an input, either dot or dash        
def updateTimings(elapsedTime):
    global dot, dash, space, letter

    #We need to be taking updated values, so it is more accurate towards
    dot = round((elapsedTime + dot)/2, 5)
    dash = round((dot * 3), 5)
    space = dash
    letter = round((dot * 3), 5)

#the purpose of this funciton is to lookup value that is produced in morsecode decoder and print it to output file
def analyzeLetter(string):
    try: 
        print(morseStringDict[string])
    except KeyError:
        print("?")
#Fisrt approach is that we measure the time inbetween clicks and use that to determine the 
#First step is we need to read the first input: 
print("enter input to sign attention: ")
firstStep = False
while not firstStep: 
    global elapsedTime

    clickInput = GPIO.input(clicker)
    
    if clickInput == 1: #Start timer
        startTime = perf_counter()
        sleep(.005)
        while clickInput == 1: 
            clickInput = GPIO.input(clicker)
            pass

        endTime = perf_counter()

        #This is the time of the dot
        elapsedTime = endTime - startTime

        #break out of loop
        firstStep = True
    
    sleep(.005)

dashTimings.append(elapsedTime)

dot = round((elapsedTime/3), 5)
dash = round(elapsedTime, 5)
space = dash
letter = round(elapsedTime, 5)


print("Dash Length: ", dot)

#Second Step: have the user signal whatever they like for the rest of progam

#use intterupts for main processing to save time and processing power
#Here we want to wait for the risng edge to start a timer
 
GPIO.add_event_detect(clicker, GPIO.BOTH, callback = processDotDash, bouncetime=50)
   

#start time to see rests
startRest = perf_counter()  

#While loop to keep the program running
try: 
    while True: 
        pass
except KeyboardInterrupt: 
    print(stringList)
    print(dotTimings)
    print(dashTimings)

     



