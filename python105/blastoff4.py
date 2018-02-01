# blastoff4.py

num = 22
while num > 20:
    num = int(raw_input("Number to count down from? "))

i = num
while i > -1:
    if i == 0:
        print "Boom!"
    else:
        print i
    i -= 1

