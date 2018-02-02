# prime.py

""" what is the largest prime factor of the number 600851475143
"""

TARGET_NUM = 600851475143

largest = 0
divisors = []

def check_prime(number_to_check):
    if number_to_check & 0b10 != 0:
        return False
    #print "Checking: %d" % number_to_check
    j = 3
    while j < number_to_check:
        if number_to_check % j == 0:
            return False
        j += 1
    return True

lower_bound = 2
upper_bound = TARGET_NUM
while lower_bound < upper_bound:
    if TARGET_NUM % lower_bound == 0:
        divisors.append(lower_bound)
        lower_bound = divisors[-1] + 1
        divisors.append(TARGET_NUM / lower_bound)
        upper_bound = divisors[-1] - 1
        continue
    lower_bound += 1

for element in divisors:
    if check_prime(element):
        largest = element

print "Largest prime cofactor: %d" % largest
