# Goblin.py
""" Class models the Goblin character, stores things such as health and
    power.
"""
from Character import Character

class Goblin(Character):
    """Class models Goblin character. """

    def print_status(self):
        """Method prints Goblin's status. """
        print "Goblin has" + super(Goblin, self).print_status()
