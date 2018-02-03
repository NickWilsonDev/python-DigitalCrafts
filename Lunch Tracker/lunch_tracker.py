# lunch_tracker.py
from time import sleep

""" name of restaurant: number of times chosen """
restaurant_choices = {
    "Chipotle": 0,
    "Farm Burger": 0,
    "Ru San's": 0
}

def clear_screen():
    #print(chr(27) + "[2J")
    print("\033c")

def exit_program():
    print "Goodbye!"

def print_main_menu():
    print "****************************"
    print "* Welcome to Lunch Tracker *"
    print "****************************"
    print "1. Choose a Restaurant"
    print "2. Manage Restaurants"
    print "3. Clear Screen"

    print "0. Exit"

def add_restaurant():
    new_restaurant = raw_input("Name: ")
    restaurant_choices[new_restaurant] = 0

def remove_restaurant():
    name = raw_input("Restaurant to remove: ")
    if name in restaurant_choices:
        del restaurant_choices[name]
        print "Removing %s..." % name
        sleep(1)
    else:
        print "No restaurant by that name."
        sleep(1)

def choose_restaurant():
    print "*********************"
    print "* Choose Restaurant *"
    print "*********************"
    i = 1
    for key in restaurant_choices:
        print "%d. %s" % (i, key)
        i += 1
    sleep(2)

def manage_restaurants():
    print "Manage Restaurants"
    sleep(2)

def main():
    """Function provides an entry point into the program(basic UI). Uses
       the Command Pattern to take the place of the switch statement."""
    menu = {
        0: exit_program,
        1: choose_restaurant,
        2: manage_restaurants,
        3: clear_screen
    }

    choice = -1
    while choice != 0:
        clear_screen()
        print_main_menu()
        choice = raw_input()
        try:
            choice = int(choice)
        except ValueError:
            print "Please choose from the selected"
            sleep(1)
            continue
        if choice not in menu:
            print "Please choose from the selected"
            sleep(1)
            continue
        else:
            menu[choice]()

main()
