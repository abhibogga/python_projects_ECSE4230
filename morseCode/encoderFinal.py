#Imports with GPIO
import RPi.GPIO as GPIO
from time import sleep, perf_counter
#Import for file parsing

#Setup Variables
inputPath = "./input.txt"
outputPath = "./output.txt"

#Setup pins
led_pin = 18  
speaker_pin = 24  
frequency = 500  

global morseString
morseString = ""

morseCode = {
    'a': '.-',     # .-
    'b': '-...',   # -...
    'c': '-.-.',   # -.-.
    'd': '-..',    # -..
    'e': '.',      # .
    'f': '..-.',   # ..-.
    'g': '--.',    # --.
    'h': '....',   # ....
    'i': '..',     # ..
    'j': '.---',   # .---
    'k': '-.-',    # -.-
    'l': '.-..',   # .-..
    'm': '--',     # --
    'n': '-.',     # -.
    'o': '---',    # ---
    'p': '.--.',   # .--.
    'q': '--.-',   # --.-
    'r': '.-.',    # .-.
    's': '...',    # ...
    't': '-',      # -
    'u': '..-',    # ..-
    'v': '...-',   # ...-
    'w': '.--',    # .--
    'x': '-..-',   # -..-
    'y': '-.--',   # -.--
    'z': '--..',   # --..
    '0': '-----',  # -----
    '1': '.----',  # .----
    '2': '..---',  # ..---
    '3': '...--',  # ...--
    '4': '....-',  # ....-
    '5': '.....',  # .....
    '6': '-....',  # -....
    '7': '--...',  # --...
    '8': '---..',  # ---..
    '9': '----.',  # ----.
    
}

morseStringDict = {
    'a': '. -',       # .-
    'b': '- . . .',   # -...
    'c': '- . - .',   # -.-.
    'd': '- . .',     # -..
    'e': '.',         # .
    'f': '. . - .',   # ..-.
    'g': '- - .',     # --.
    'h': '. . . .',   # ....
    'i': '. .',       # ..
    'j': '. - - -',   # .---
    'k': '- . -',     # -.-
    'l': '. - . .',   # .-..
    'm': '- -',       # --
    'n': '- .',       # -.
    'o': '- - -',     # ---
    'p': '. - - .',   # .--.
    'q': '- - . -',   # --.-
    'r': '. - .',     # .-.
    's': '. . .',     # ...
    't': '-',         # -
    'u': '. . -',     # ..-
    'v': '. . . -',   # ...-
    'w': '. - -',     # .--
    'x': '- . . -',   # -..-
    'y': '- . - -',   # -.--
    'z': '- - . .',   # --..
    '0': '- - - - -', # -----
    '1': '. - - - -', # .----
    '2': '. . - - -', # ..---
    '3': '. . . - -', # ...--
    '4': '. . . . -', # ....-
    '5': '. . . . .', # .....
    '6': '- . . . .', # -....
    '7': '- - . . .', # --...
    '8': '- - - . .', # ---..
    '9': '- - - - .', # ----.
}

#Setup GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(speaker_pin, GPIO.OUT)
speaker_pwm = GPIO.PWM(speaker_pin, frequency)

#Function for user input for unit length
def unit_length_input():
    while True:
        try:
            unit_length = float(input("Enter your desired length of a Morse Code unit (.001 to 2 seconds): "))
            if unit_length >= 0.001 and unit_length <= 2:
                return unit_length
            else:
                print("Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")

#Function to play Morse Code on speaker and toggle LED
def output_morse_code(symbol, unit_length):
    
    duration = 0
    
    #A dot is one unit and a hash is 3 times the unit
    if symbol == '.':
        duration = unit_length
    else:
        duration = 3 * unit_length
    
    GPIO.output(led_pin, GPIO.HIGH)
    speaker_pwm.start(50)  #50% duty cycle for speaker
    
    #Verify actual unit length using perf_counter()
    start = perf_counter()
    sleep(duration)
    end = perf_counter()
    actual_duration = end - start

    print(f"Expected duration: {duration:.3f}s, Actual duration: {actual_duration:.3f}s")

    #Turn off LED and speaker
    GPIO.output(led_pin, GPIO.LOW)
    speaker_pwm.stop()
    #Space between symbols
    sleep(unit_length)

#Sending morse code to be outputted on speaker
def send_morse_code(message, unit_length):
    #WE NEED TO HARD CODE ATTENTION AND OUT 
    #Sending units based on char
    for char in message:
        if char == '.':
            #Turn it on for one unit
            speaker_pwm.start(50)
            GPIO.output(led_pin, GPIO.HIGH)
            sleep(unit_length)
            speaker_pwm.stop()
            GPIO.output(led_pin, GPIO.LOW)
        elif char == '-':
            speaker_pwm.start(50)
            GPIO.output(led_pin, GPIO.HIGH)
            sleep(unit_length * 3)
            speaker_pwm.stop()
            GPIO.output(led_pin, GPIO.LOW)
        elif char == '|' or char == '@':
            GPIO.output(led_pin, GPIO.LOW)
            sleep(7 * unit_length)
        elif char == '!':
            GPIO.output(led_pin, GPIO.LOW)
            sleep(unit_length * 3)
        elif char == " ":
            GPIO.output(led_pin, GPIO.LOW)
            sleep(unit_length)
            
        
            

#Write to file method
def writeToFile(messages, fileName, unit_length, morseString):
    #First thing we need to do is write the attention line
    with open(fileName, "w") as file:
        file.write("- . - . - | attention\n")
        
        #Writing words in message 
        for message in messages:
            is_first_word = True
            messageLen = len(message.split(" "))
            #Splits message into words and breaks down into letters
            for index, word in enumerate(message.split()):
                
                returnString = ""
                letters = list(word)

                
                #Convert each letter from morseCode and creates the word
                for number, letter in enumerate(letters):
                    returnString += morseCode[letter]
                    morseString += morseStringDict[letter]
                    #Check if letter is not the last in the word
                    if number != len(letters) -1 :
                        returnString += " "
                        morseString += "!"
                    
                    



                #Checks if it's not first word, add 7 spaces
                if not is_first_word:
                    file.write("       ")  

                is_first_word = False
                
                #Translation passing the if condition
                file.write(returnString + " | " + word + "\n")

                if index != messageLen - 1:
                    morseString += "@"
                else:     
                    morseString += "|"
            #End message with "out" and move to next line
            file.write(". - . - . | out\n")
            
            
    return morseString

#Read input file
with open(inputPath) as file:
    lines = [line.rstrip() for line in file.readlines()]

unit_length = unit_length_input()

#Write messages to output file
try:
    string = (writeToFile(lines, outputPath, unit_length, morseString))
    print(string)
    send_morse_code(string, unit_length)
    
finally:
    GPIO.cleanup()

