# n_to_m.py

start = 0
end   = 0

while start >= end:
    start = int(raw_input("Start from: "))
    end   = int(raw_input("End on: "))

list = range(start, end + 1)

for element in list:
    print element

