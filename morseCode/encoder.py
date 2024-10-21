#Imports with GPIO

#Import for file parsing

#Setup Variables
inputPath = "./input.txt"
outputPath = "./output.txt"

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

#Write to file method
def writeToFile(message, fileName):
    #First thing we need to do is write the attention line
    with open(fileName, "w") as file:
        file.write("- . - . - | attention" + "\n")

    #Now write the rest of the words in the line
    for i in message.split():
        returnString = ""
        letters = list(i)
        for letter in letters:
            returnString += morseCode[letter]

            if letter != letters[-1]:
                returnString += " "
        with open(fileName, "a") as file:
            file.write(returnString + "| " + i + "\n")


#Step 1: Read The file
with open(inputPath) as file:
    lines = [line.rstrip() for line in file.readlines()]


writeToFile(lines[0], outputPath)

#Write to the outputFiles
for index, messages in enumerate(lines):
    writeToFile(messages, "output" + str(index) + ".txt")
