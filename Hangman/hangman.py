#############################################
#   WELCOME TO HANGMAN PROGRAMMING BY       #
#              GHISLAIN                     #
#############################################
import random
import draw

# Use to concatenate the user's guesses
U_guess = ""
# Append's  the correct guessed letters
correct = []
# Append's  the incorrect guessed letters
incorrect = []
# checks for incorrect guesses
check = []


# Load the words
def wordlist():
    file = open("words.txt", "r")
    line = file.readline()
    word = line.lower().split()
    return word


# Computer make's a choice of the word to be guessed
C_guess = random.choice(wordlist())
# uncomment this if you want to see the word
# print(C_guess)
print(f"The word you are to guess is a {len(C_guess)} character word")


# Take the users input and appends it to a list
def isLetter():
    # checks for errors made by the user
    while True:
        # takes the user's guesses
        guess = input("Please enter a letter: ")
        if len(guess) > 1:
            print("Please enter only one letter at a time")
        elif guess.isnumeric():
            print("Please enter only letters")
        elif (guess in correct) or (guess in incorrect):
            print("This letter had been guessed")
        else:
            break
    # collects all the user's list of correct guessed letters
    if guess in C_guess:
        correct.append(guess)
    else:
        # collects all the user's list of incorrect guessed words
        print("Sorry wrong guess")
        incorrect.append(guess)
        check.append(guess)


# prints out the letters that the user has guessed
def isword(U_guess):
    for letter in C_guess:
        if letter in correct:
            U_guess += letter
        else:
            U_guess += "_ "
    return U_guess


chances = 7
running = True
# main game loop
while running:

    isLetter()
    result = isword(U_guess)
    print(result)
    if result == C_guess:
        print(f"CONGRATULATIONS YOU GUESSED IT: {U_guess}")
        running = False

    if len(check) > 0:
        # draws the hangman diagram which if found in the draw.py file
        print(draw.draw_hangman(chances))
        chances -= 1
        check.pop()
        # verifies if all the chances have been exhausted
        if chances == 0:
            print("Sorry you lost")
            print(f"THE WORD IS: {C_guess}")
            running = False
        else:
            print(f"You are left with {chances} tries\n")