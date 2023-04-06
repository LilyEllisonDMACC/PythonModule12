"""
Program: Motorcycle.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to create a subclass for an abstract class and use the abstract class's methods.

"""

from abstract_class.Rider import Rider


class Motorcycle(Rider):
    def __init__(self):
        self.power = "Engine"
    def ride(self):
        print(self.power + " powered, not enclosed")

    def riders(self):
        print("1 or 2")


#Driver
m = Motorcycle()
m.ride()
m.riders()

"""
Testing:
Engine powered, not enclosed
1 or 2

Process finished with exit code 0

"""
