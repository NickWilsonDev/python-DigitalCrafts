# coins.py

coins = 0



answer = ""
while answer != "no":
    print "You have %d coins." % coins
    answer = raw_input("Do you want another? ")
    if answer == "yes":
        coins += 1
    

print "Bye"
