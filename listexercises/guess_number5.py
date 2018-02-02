""" guess_number4.py
    guess a number game with High-Low hint, and randomly generated number
    now limits number of guesses to 5
"""
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def play_game():
    num_of_guesses_left = 5
    secret_number = random.randint(1, 10)
    guess = 0

    print "I am thinking of a number between 1 and 10"

    while guess != secret_number:
        print "You have %d guesses left." % num_of_guesses_left
        guess = int(raw_input("What's the number? "))
        num_of_guesses_left -= 1
        if guess < secret_number:
            print "%s is too low." % guess
        elif guess > secret_number:
            print "%s is too high." % guess
        if guess == secret_number:
            print "Yes! You win!"
        if num_of_guesses_left <= 0:
            print "You ran out of guesses"
            break

play_game()
choice = str(raw_input(bcolors.FAIL + "Do you want to play again " + 
                                    "(Y or N)? " + bcolors.ENDC)).upper()

while choice != 'N':
    play_game()
    choice = str(raw_input(bcolors.FAIL + "Do you want to play again " + 
                                    "(Y or N)? " + bcolors.ENDC)).upper()
print "Bye!"
