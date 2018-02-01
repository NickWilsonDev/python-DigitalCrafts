# triangle_numbers.py
print "Printing the first 100 triangle numbers...."

i = 1

while i < 101:
    print "%d triangle number is :: %d" % (i, (i * (i + 1) / 2))
    i += 1
