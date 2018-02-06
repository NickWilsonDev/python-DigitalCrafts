# Character.py
""" Base class from which the hero and goblin classes will inherit """

class Character(object):
    """Class models an abstract Character from which specific characters
       will inherit from. """

    def __init__(self, health, power):
        """Method initializes an object, sets it up ect. """
        self.health = health
        self.power = power

    def attack(self, character):
        """Method directs this object to attack the specified object. """
        character.health -= self.power

    def print_status(self):
        """Returns string representing status of the object. """
        return " %d health and %d power." %(self.health, self.power)

    def alive(self):
        """Method does a quick check to see if this object is still alive.
            returns (boolean) - true if alive, false otherwise
        """
        return self.health > 0
