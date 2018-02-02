# sum_mult_3_5.py

total = 0

for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        total = total + num

print total
