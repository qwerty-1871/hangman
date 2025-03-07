#imports
import random
import os
import re

#functions
def readRandomLine(file_name):
    line = random.choice(list(open(file_name)))
    return re.sub(r'\n+', '\n', line).strip('\n')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#variables
start = True
gq = True
nq = True
wq = True
game = True
won = False
guesses = 0
lindex = 0 
letters = []
wrongletters = []
#default variables
wordset = "medium"
countcorrectguesses = False
maxguesses = 5 

#start screen
clear()
print("HANGMAN")
print("Press ENTER to begin or 's' to change the settings:")
while start == True:
    startinput = input()
    if startinput == "":
        start = False
    elif startinput == "s":
        clear()
        print("Do you want correct guesses to count towards the total? (y/N):")
        while True:
            ginput = input().lower()
            if ginput == "y":
                countcorrectguesses = True
                break
            elif ginput == "n" or ginput == '':
                countcorrectguesses == False
                break
            else:
                print("Invalid Input.")
        print("How many guesses would you like to have? (Default is 5):")
        while True:
            ninput = input()
            if ninput.isdigit():
                maxguesses = int(ninput)
                break
            elif ninput == '':
                break
            else:
                print("Value must be an integer.") 
        print("What set of words would you like to use? (easy, medium(default), hard, or countries):")
        while True:
            winput = input()
            if os.path.isfile("dict/" + winput + ".txt"):
                wordset = winput
                break
            elif winput == '':
                break
            else:
                print("Word set does not exist.")
        start = False
    else:
        print("Invalid input.")
clear()

#setword
word = readRandomLine("dict/" + wordset + ".txt")
for letter in word:
    letters.append("_")

#loop for game
while game == True:
    #hangman screen
    if guesses == 0:
        print("---------------------\n  |  /             |\n  | /              |\n  |/\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n-----")
    elif maxguesses > 4 and guesses == 1:
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |\n  |\n  |\n  |\n  |\n  |\n-----")
    elif (maxguesses > 4 and guesses == 2) or (maxguesses < 5 and guesses == 1 and maxguesses != 1) or (maxguesses > 6 and guesses != 1 and guesses < maxguesses - 4):
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |                |\n  |                |\n  |                |\n  |\n  |\n  |\n-----")
    elif (maxguesses > 6 and guesses == maxguesses - 4) or (maxguesses == 6 and guesses == maxguesses - 3):
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |                |\n  |               /|\n  |              / | \n  |\n  |\n  |\n-----")
    elif ((maxguesses == 5 or maxguesses == 6) and guesses == maxguesses - 2) or (maxguesses > 6 and guesses == maxguesses - 3) or (maxguesses == 4 and guesses == 2):
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |                |\n  |               /|\\\n  |              / | \\\n  |\n  |\n  |\n-----")
    elif maxguesses > 6 and guesses == maxguesses - 2:
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |                |\n  |               /|\\\n  |              / | \\\n  |               / \n  |              /   \n  |\n-----")
    elif (maxguesses > 4 and guesses == maxguesses - 1) or ((maxguesses == 3 or maxguesses == 4) and guesses == maxguesses - 1):
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |                |\n  |               /|\\\n  |              / | \\\n  |               / \\\n  |              /   \\\n  |\n-----")
    elif guesses == maxguesses:
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            / x   x \\\n  |            \\  ---  /\n  |             -------\n  |                |\n  |               /|\\\n  |              / | \\\n  |               / \\\n  |              /   \\\n  |\n-----")
    print(*letters)
    print(*wrongletters)
    if guesses != maxguesses - 1:
        print("You have " + str(maxguesses - guesses) + " guesses left.")
    else:
        print("You have 1 guess left.")
    #checking user input
    if guesses != maxguesses:
        guess = input()
        if guess == word:
            won = True
            game = False            
        elif len(guess) == 1:
            if guess in word:
                for letter in word:
                    if guess == letter:
                        letters[lindex] = letter
                    lindex = lindex + 1
                lindex = 0     
                if countcorrectguesses == True:
                    guesses = guesses + 1
                if all([char in letters for char in word]):
                    won = True
                    game = False
            else:
                wrongletters.append(guess)
                guesses = guesses + 1           
        else:
            guesses = guesses + 1
    else:
        won = False
        game = False
        input("Press ENTER to continue.")
    clear()

#end screen
if won == True:
    if guesses != 1:
        print("You won!\nIt took you " + str(guesses) + " guesses.\nThe word was " + word + ".\nThank you for playing.")
    else:
        print("You won!\nIt took you " + str(guesses) + " guess.\nThe word was " + word + ".\nThank you for playing.")
else:
    print("You have lost.\nThe word was " + word + ".\nThank you for playing.")
input("Press ENTER to exit.")
