# triangle.py

i = 1
stars = 1
spaces = 7 - stars

def make_row(stars, spaces):
    row = ""
    row += " " * (spaces / 2)
    row += "*" * stars
    row += " " * (spaces / 2)
    return row

# print out all rows
while i < 5:
    print make_row(stars, spaces)
    stars += 2
    spaces = 7 - stars
    i += 1

