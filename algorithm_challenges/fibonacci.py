# fibonacci.py
""" Iterative version of program to generate Fibonacci sequence
    and sum all even valued terms
"""

current = 0
previous = 1
previous_minus_one = 1
total = 0

while current < 4000000:
    current = previous + previous_minus_one
    if current % 2 == 0:
        total += current
    previous_minus_one = previous
    previous = current

print total
