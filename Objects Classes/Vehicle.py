#Vehicle.py

class Vehicle(object):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print "%d %s %s" % (year, make, model)


