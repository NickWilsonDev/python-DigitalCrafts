""" letter_histogram.py
    Program asks user to input a word. It then makes a dictionary with
    unique letters for keys and their number of appearances as the values.
"""

msg = list(raw_input("Please enter a word: "))

histogram = {}

for letter in msg:
    if letter in histogram:
        histogram[letter] = histogram[letter] + 1
    else:
        histogram[letter] = 1
print histogram
