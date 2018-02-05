# OOPhoneBook.py
"""
Now taking advantage of the Object Oriented style.
got the idea for the quasi switch structure(command pattern) with a dict from this site
https://softwareengineering.stackexchange.com/questions/182093/why-store-a-function-inside-a-python-dictionary
"""
from Contact import Contact

entries = []

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
    if len(entries) > 0:
        name = raw_input("Name: ")
        for person in entries:
            if person.first == name or person.last == name:
                print_contact(person)
    else:
        print "The contact list is empty."

def set_entry():
    """Function creates an entry into the entries dictionary, prompting the
       user for the name and number data.
    """
    first_name = raw_input("First Name: ")
    last_name = raw_input("Last Name: ")
    number = raw_input("Phone Number: ")
    email = raw_input("Email address: ")

    temp_contact = Contact(first_name, last_name, number, email)
    entries.append(temp_contact)
    print "Entry stored for %s." % first_name

def del_entry():
    """Function deletes the specified entry from the dictionary if it
       exists.
    """
    global entries
    first_name = raw_input("First Name: ")
    last_name  = raw_input("Last Name: ")
    new_list = []
    for person in entries:
        if person.first == first_name and person.last == last_name:
            pass
        else:
            new_list.append(person)
    print "Listing for %s %s was deleted." %(first_name, last_name)
    entries = new_list

def print_contact(person):
    print "Found entry for %s %s %s %s" %(person.first, person.last, person.phone, person.email)

def list_entries():
    """Function displays all data from the dictionary.
    """
    if any(entries):
        for person in entries:
            print_contact(person)
        sort = raw_input("Would you like to sort entries?(y/n) ")
        if sort == 'y':
            sort_key = raw_input("(Name|Number)" )
            if sort_key == "Name":
                entries.sort(key=lambda x: (x.last, x.first))
                for person in entries:
                    print_contact(person)
            elif sort_key == "Number":
                sorted(entries, key=lambda x: x.phone)
                for person in entries:
                    print_contact(person)
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
