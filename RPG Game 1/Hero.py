# Hero.py
""" Class models the hero character, stores things such as health and
    power.
"""
from Character import Character

class Hero(Character):
    """Class models the hero character. """

    def print_status(self):
        """Prints status of this object. """
        print "You have" + super(Hero, self).print_status()
