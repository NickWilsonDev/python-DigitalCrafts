""" guess_number4.py
    guess a number game with High-Low hint, and randomly generated number
    now limits number of guesses to 5
"""
import random

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
