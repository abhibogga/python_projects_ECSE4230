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
            unit_length = float(input("Enter your desired length of a Morse Code unit (in seconds): "))
            if unit_length > 0:
                return unit_length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")

#Function to play Morse Code on speaker and toggle LED
def output_morse_code(symbol, unit_length):
    
    duration = 0
    
    #A dot is one unit and a hash is 3 times the unit
    if symbol == '.':
        duration = unit_length
    else:
        3 * unit_length
    
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
    
    #Start with attention
    print("- . - . - | attention")

    #Sending units based on char
    for char in message:
        if char == '.':
            output_morse_code('.', unit_length)
        elif char == '-':
            output_morse_code('-', unit_length)
        elif char == ' ':
            sleep(3 * unit_length) 

    sleep(7 * unit_length) 

#Write to file method
def writeToFile(messages, fileName, unit_length):
    #First thing we need to do is write the attention line
    with open(fileName, "w") as file:
        file.write("- . - . - | attention\n")
        
        #Writing words in message 
        for message in messages:
            is_first_word = True
            
            #Splits message into words and breaks down into letters
            for word in message.split():
                returnString = ""
                letters = list(word)
                
                #Convert each letter from morseCode and creates the word
                for letter in letters:
                    returnString += morseCode[letter]
                    #Check if letter is not the last in the word
                    if letter != letters[-1]:
                        returnString += " "  

                #Checks if it's not first word, add 7 spaces
                if not is_first_word:
                    file.write("       ")  
                
                #Translation passing the if condition
                file.write(returnString + " | " + word + "\n")

                #Play morse code on speaker
                output_morse_code(returnString, unit_length)
                
                is_first_word = False

            #End message with "out" and move to next line
            file.write(". - . - . | out\n")

#Read input file
with open(inputPath) as file:
    lines = [line.rstrip() for line in file.readlines()]

unit_length = unit_length_input()


#Write messages to output file
try:
    writeToFile(lines, outputPath, unit_length)
finally:
    GPIO.cleanup()
