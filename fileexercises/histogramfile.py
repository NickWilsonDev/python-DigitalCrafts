# histogramfile.py
"""Write a program that prompts the user to enter a file name, then prints the letter histogram and the word histogram of the contents of the file.
"""

filename = raw_input("What file would you like to read....")
f = open(filename)
word_hist = {}
letter_hist = {}
for line in f:
    for letter in line:
        if letter in letter_hist:
            letter_hist[letter] = letter_hist[letter] + 1
        else:
            letter_hist[letter] = 1

    word_line = line.split()
    for word in word_line:
        if word in word_hist:
            word_hist[word] = word_hist[word] + 1
        else:
            word_hist[word] = 1

print "letter histogram"
print letter_hist

print "word histogram"
print word_hist

