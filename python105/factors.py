# factors.py

num = int(raw_input("Number? "))

i = 1

print "------factors of %d --------" % num
while i < num + 1:
    if num % i == 0:
        print i
    i += 1

