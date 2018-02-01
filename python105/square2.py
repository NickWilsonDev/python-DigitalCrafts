# square2.py

n = int(raw_input("How big is the square? "))

row = ""

i = 0
while i < n:
    row = row + "*"
    i += 1

i = 0
while i < n:
    print row
    i += 1
