# readfile.py

"""Write a program that prompts the user to enter a file name, reads the contents of the file and prints it to the screen. """

filename = raw_input("What file would you like to read....")
f = open(filename)
for line in f:
    print line
