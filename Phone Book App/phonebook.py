# phonebook.py
"""
got the idea for the quasi switch structure(command pattern) with a dict from this site
https://softwareengineering.stackexchange.com/questions/182093/why-store-a-function-inside-a-python-dictionary
"""

entries = {}

def display_menu():
    print ""
    print "Electronic Phone Book"
    print "====================="
    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Quit"
    print "What do you want to do (1-5)?"

def look_up_entry():
    if any(entries):
        name = raw_input("Name: ")
        if name in entries:
            print "Found entry for %s: %s" % (name, number)
        else:
            print "No entry found for %s." % name
    else:
        print "The contact list is empty."

def set_entry():
    name   = raw_input("Name: ")
    number = raw_input("Phone Number: ")
    entries[name] = number
    print "Entry stored for %s." % name

def del_entry():
    name   = raw_input("Name: ")
    if name in entries:
        del entries[name]
        print "Deleted entry for %s." % name
    else:
        print "No entry found for %s." % name

def list_entries():
    if any(entries):
        for name in entries:
            print "Found entry for %s: %s" % (name, entries[name])
    else:
        print "The contact list is empty!"

def exit():
    print "Bye."

def main():
    """ Command Pattern YaY! """
    options = {
        1: look_up_entry,
        2: set_entry,
        3: del_entry,
        4: list_entries,
        5: exit
    }

    choice = 0
    while choice != 5:
        display_menu()
        choice = int(raw_input())
        options[choice]()

main()

