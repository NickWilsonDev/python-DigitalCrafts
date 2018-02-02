""" guess_number3.py
    guess a number game with High-Low hint, and randomly generated number
"""
import random

secret_number = random.randint(1, 10)
guess = 0

print "I am thinking of a number between 1 and 10"

while guess != secret_number:
    guess = int(raw_input("What's the number? "))
    if guess < secret_number:
        print "%s is too low." % guess
    else:
        print "%s is too high." % guess

print "Yes! You win!"
