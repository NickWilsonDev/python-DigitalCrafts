# RPG_Game.py
"""
In this simple RPG game, the hero fights the zombie. He has the options to:

1. fight zombie
2. do nothing - in which case the zombie will attack him anyway
3. flee

"""
from Hero import Hero
from Goblin import Goblin
from Zombie import Zombie

def main():
    """Entry point into program. """
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
    zombie = Zombie(1, 2)

    while zombie.alive() and hero.alive():
        hero.print_status()
        zombie.print_status()
        print "What do you want to do?"
        print "1. fight zombie"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks zombie
            hero.attack(zombie)
            print "You do %d damage to the zombie." % hero.power
            if not zombie.alive():
                print "The zombie is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if zombie.alive():
            # Goblin attacks hero
            zombie.attack(hero)
            print "The zombie does %d damage to you." % zombie.power
            if not hero.alive():
                print "You are dead."

main()
