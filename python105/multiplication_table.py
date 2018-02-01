# multiplication_table.py

lst = range(1, 11)

for element in lst:
    for element2 in lst:
        print "%d x %d = %d" % (element, element2, element * element2)

