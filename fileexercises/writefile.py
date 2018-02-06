# writefile.py
"""Write a program that prompts the user to enter a file name, then prompts the user to enter the contents of the file, and then saves the content to the file."""

filename = raw_input("Filename to write to? ")

data = raw_input("Data to write?.. ")

f = open(filename, 'w')
f.write(data)

