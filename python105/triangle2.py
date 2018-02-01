# triangle2.py

height = int(raw_input("Height? "))

base_length = (2 * height) - 1
i = 0
stars = 1
spaces = base_length - stars
def make_row(stars, spaces):
    row = ""
    row += " " * (spaces / 2)
    row += "*" * stars
    row += " " * (spaces / 2)
    return row

# print out all rows
while i < height:
    print make_row(stars, spaces)
    stars += 2
    spaces = base_length - stars
    i += 1

