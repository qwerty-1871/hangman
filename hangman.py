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
word = readRandomLine("dict/main.txt")
game = True
won = False
guesses = 0
lindex = 0 
letters = []
wrongletters = []
for letter in word:
    letters.append("_")

#start screen
clear()
print("HANGMAN")
input("Press ENTER to begin.")
clear()

#loop for game
while game == True:
    #hangman screen
    if guesses == 0:
        print("---------------------\n  |  /             |\n  | /              |\n  |/\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n-----")
    elif guesses == 1:
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |\n  |\n  |\n  |\n  |\n  |\n-----")
    elif guesses == 2:
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |                |\n  |                |\n  |                |\n  |\n  |\n  |\n-----")
    elif guesses == 3:
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |                |\n  |               /|\\\n  |              / | \\\n  |\n  |\n  |\n-----")
    elif guesses == 4:
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            /       \\\n  |            \\       /\n  |             -------\n  |                |\n  |               /|\\\n  |              / | \\\n  |               / \\\n  |              /   \\\n  |\n-----")
    elif guesses == 5:
        print("---------------------\n  |  /             |\n  | /              |\n  |/            -------\n  |            / x   x \\\n  |            \\  ---  /\n  |             -------\n  |                |\n  |               /|\\\n  |              / | \\\n  |               / \\\n  |              /   \\\n  |\n-----")
    print(*letters)
    print(*wrongletters)
    if guesses != 4:
        print("You have " + str(5 - guesses) + " wrong guesses left.")
    else:
        print("You have 1 wrong guess left.")
    #checking user input
    if guesses != 5:
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
        print("You won!\nYou had " + str(guesses) + " wrong guesses.\nThe word was " + word + ".\nThank you for playing.")
    else:
        print("You won!\nYou had " + str(guesses) + " wrong guess.\nThe word was " + word + ".\nThank you for playing.")
else:
    print("You have lost.\nThe word was " + word + ".\nThank you for playing.")
input("Press ENTER to exit.")
