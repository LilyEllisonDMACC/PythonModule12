"""
Program: Bicycle.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to create a subclass for an abstract class and use the abstract class's methods.

"""

from abstract_class.Rider import Rider


class Bicycle(Rider):
    def __init__(self):
        self.power = "Human"

    def ride(self):
        print(self.power + " powered, not enclosed")

    def riders(self):
        print("1 or 2 if tandem or a daredevil")


#Driver
b = Bicycle()
b.ride()
b.riders()

"""
Testing:
Human powered, not enclosed
1 or 2 if tandem or a daredevil

Process finished with exit code 0

"""