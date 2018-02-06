# Zombie.py
""" Class models the Zombie character, stores things such as health and
    power. The Zombie cannot die.
"""
from Character import Character

class Zombie(Character):
    """Class models Zombie character. """

    def print_status(self):
        """Method prints status of character. """
        print "Zombie has" + super(Zombie, self).print_status()

    def alive(self):
        """Zombie cannot 'die' so this method just returns True."""
        return True
