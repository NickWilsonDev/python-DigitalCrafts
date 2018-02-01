# box.py

width = int(raw_input("Width? "))
height = int(raw_input("Height? "))

top = "*" * width
bottom = "*" * width

# make a middle row string
i = width - 2
middle = "*"
middle += " " * i
middle += "*"


# print box
i = 0
print top
while i < height - 2:
    print middle
    i += 1
print bottom
