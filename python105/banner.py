# banner.py

msg = raw_input("Text? ")

# * message *
row_width = len(msg) + 4

print "*" * row_width
print "* " + msg + " *"
print "*" * row_width
