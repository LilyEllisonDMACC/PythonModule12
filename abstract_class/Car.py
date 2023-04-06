"""
Program: Car.py
Author: Lily Ellison
Last date modified: 04/06/2023

The purpose of this program is to create a subclass for an abstract class and use the abstract class's methods.

"""

from abstract_class.Rider import Rider


class Car(Rider):
    def __init__(self):
        self.power = "Engine"

    def ride(self):
        print(self.power + " powered, enclosed")

    def riders(self):
        print("1 or more comfortably")


#Driver
c = Car()
c.ride()
c.riders()

"""
Testing:
Engine powered, enclosed
1 or more comfortably

Process finished with exit code 0

"""
