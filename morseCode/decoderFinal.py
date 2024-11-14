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
clicker = 20
LEDPin = 16
soundPin = 21


GPIO.setup(clicker, GPIO.IN)
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(soundPin, GPIO.OUT)
speaker_pwm = GPIO.PWM(soundPin, 500)

#Define the dictionaries
morseStringDict = {
    "-.-.-": "attention",
    ".-.-.": "out",
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
outputMorseString = ""
outputEnglishString = ""

dotTimings = []
dashTimings = []




# Interrupt Callback
def processDotDash(channel):
    global startRest 
    global dash, dot, space, letter
    global dotTimings, dashTimings
    global startTime, endTime
    global stringList, outputEnglishString, outputMorseString
    if not GPIO.input(clicker):
        endTime = perf_counter()
        elapsedTime = endTime - startTime
        
        #Here well do all our processing for dots and dashes
        if  elapsedTime < dot *2: 
            print("dot")
            stringList += "."
            outputMorseString += "."
            dotTimings.append(elapsedTime)
            

             
        
        if elapsedTime > dot * 2:
            print("dash")
            stringList += "-"
            outputMorseString += "-"
            dashTimings.append(elapsedTime)
            


        #We need to start the rest time up again to properly process next interval 
        startRest = perf_counter()

        #now we need to turn off the led and sound
        speaker_pwm.stop()
        GPIO.output(LEDPin, GPIO.LOW)
        

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
            if restTime < space *2: 
                stringList += ""
                
        
            if space * 7 > restTime > space * 2:
                print("letter")
                if len(stringList) > 0: 
                    analyzeLetter(stringList)
                    stringList = ""

            #Now we need to analyze the word
            if space * 7 < restTime: 
                analyzeLetter(stringList)
                #Here we will be doing all the printing to outputfile
                print("word")
                #First we need to print the word itself
                if len(stringList) > 0: 
                    with open('./output.txt', "a") as file:
                        file.write(outputEnglishString  + " | " + outputMorseString + "\n")
                    print(outputEnglishString  + " | " + outputMorseString + "\n")
                
                outputEnglishString = ""
                outputMorseString = ""
                stringList = ""
                

            
        #Turn on LED and run the sound
        speaker_pwm.start(50)
        GPIO.output(LEDPin, GPIO.HIGH)
        
        

                
                
            


#the purpose of this funciton is to lookup value that is produced in morsecode decoder and print it to output file
def analyzeLetter(string):
    global dot, dash, space, letter, outputEnglishString, outputMorseString, stringList
    try: 
        print(morseStringDict[string])
        
        #If message is attention, we need to start taking the averages
        if morseStringDict[string] == 'attention':
            
            #Now we have recognized the attention, so we need to take the averages of the dots and dashes
            dotElapsed = 0
            for i in dotTimings:
                dotElapsed += i
            dotElapsed = round(dotElapsed/len(dotTimings), 5)
            dashElapsed = 0
            for i in dashTimings: 
                dashElapsed += i
            dashElapsed = round((dashElapsed/len(dashTimings)), 5)
            #We need to be taking updated values, so it is more accurate towards
            dot = round(dotElapsed, 5)
            dash = round(dashElapsed, 5)
            space = dash/3
            letter = dash

            #We need to add a line after attention
            with open('./output.txt', "a") as file:
                file.write("attention | -.-.- \n")

            outputEnglishString = ""
            outputMorseString = ""
            stringList = ""
        
        elif morseStringDict[string] == 'out':
            #We need to add a line after attention
            with open('./output.txt', "a") as file:
                file.write("out | .-.-. \n")
            file.close()
            sys.exit(0)
        
        else: #This means that it is not attention or out, just a regular word
            outputEnglishString += morseStringDict[string]
 
    except KeyError:
        print("?"  + string)
        outputEnglishString += "?"




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
            #Turn off PWM
            speaker_pwm.start(50)
            GPIO.output(LEDPin, GPIO.HIGH)
            

        endTime = perf_counter()

        #This is the time of the dot
        elapsedTime = endTime - startTime

        #break out of loop
        firstStep = True

        #Turn off PWM
        speaker_pwm.stop()
        GPIO.output(LEDPin, GPIO.LOW)
    
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

     



