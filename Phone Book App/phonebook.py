# phonebook.py
"""
got the idea for the quasi switch structure(command pattern) with a dict from this site
https://softwareengineering.stackexchange.com/questions/182093/why-store-a-function-inside-a-python-dictionary
"""

entries = {}

def display_menu():
    """Function simply prints out the menu of options for the user.
    """
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
    """Function checks the entries dictionary to check if a particular
       entry exists, if so then that data is displayed to the user.
    """
    if any(entries):
        name = raw_input("Name: ")
        if name in entries:
            print "Found entry for %s: %s" % (name, entries[name])
        else:
            print "No entry found for %s." % name
    else:
        print "The contact list is empty."

def set_entry():
    """Function creates an entry into the entries dictionary, prompting the
       user for the name and number data.
    """
    name = raw_input("Name: ")
    number = raw_input("Phone Number: ")
    entries[name] = number
    print "Entry stored for %s." % name

def del_entry():
    """Function deletes the specified entry from the dictionary if it
       exists.
    """
    name = raw_input("Name: ")
    if name in entries:
        del entries[name]
        print "Deleted entry for %s." % name
    else:
        print "No entry found for %s." % name

def list_entries():
    """Function displays all data from the dictionary.
    """
    if any(entries):
        for name in entries:
            print "Found entry for %s: %s" % (name, entries[name])
        sort = raw_input("Would you like to sort entries?(y/n) ")
        if sort == 'y':
            sort_key = raw_input("(Name|Number)" )
            entry_list = []
            for key, value in entries.items():
                entry_list.append([key, value])
            if sort_key == "Name":
                entry_list = sorted(entry_list, key=lambda x: x[0])
                for entry in entry_list:
                    print "%s :: %s" %(entry[0], entry[1])
            elif sort_key == "Number":
                entry_list = sorted(entry_list, key=lambda x: x[1])
                for entry in entry_list:
                    print "%s :: %s" %(entry[0], entry[1])
            else:
                pass
    else:
        print "The contact list is empty!"

def exit_phonebook():
    """Function prints 'Bye.', simply needed to work with my command
       pattern.
    """
    print "Bye."

def main():
    """Function provides entry point into program utilizes the
       Command Pattern YaY! It uses this to take the place of a switch
       statement to direct flow of application."""
    options = {
        1: look_up_entry,
        2: set_entry,
        3: del_entry,
        4: list_entries,
        5: exit_phonebook
    }

    choice = 0
    while choice != 5:
        display_menu()
        choice = int(raw_input())
        options[choice]()

main()
